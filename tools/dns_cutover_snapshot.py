"""Read-only DNS observation directly from delegated Domainhotelli nameservers.

Best-effort pre-cutover evidence. Never writes DNS or sends credentials. A public
GitHub Actions artifact contains no raw TXT record values or tenant secrets.
Missing answers/partial reachability are NOT authority to change or restore DNS.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import dns.resolver
import dns.query
import dns.message
import dns.flags
import dns.rcode
import dns.rdatatype

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'tools' / 'dns_cutover_snapshot_results.json'
HOSTS = ('prompted.fi', 'www.prompted.fi', 'app.prompted.fi', '_dmarc.prompted.fi')
TYPES = ('A','AAAA','CNAME','MX','NS','CAA','SOA','TXT')
DELEGATED_NS = ('ns1.domainhotelli.fi', 'ns2.domainhotelli.fi')

def lookup_ip(name):
    r = dns.resolver.Resolver()
    r.lifetime = 4
    for rt in ('A','AAAA'):
        try:
            return str(next(iter(r.resolve(name,rt))).address)
        except (dns.exception.DNSException, StopIteration):
            continue
    return None

def sanitize_txt(content):
    s = str(content).replace('\\\"','').replace('"','').strip()
    if s.lower().startswith('v=spf1'):
        return 'SPF policy present (value redacted)'
    if s.lower().startswith('v=dmarc1'):
        return 'DMARC policy present (value redacted)'
    return 'TXT present (value redacted)'

def query(nsip, name, rectype):
    q = dns.message.make_query(name, dns.rdatatype.from_text(rectype))
    result = dns.query.udp(q, nsip, timeout=2.0, ignore_unexpected=True)
    if result.flags & dns.flags.TC:
        result = dns.query.tcp(q,nsip,timeout=2.0)
    if not result.flags & dns.flags.AA:
        return None, 'response not authoritative'
    code = result.rcode()
    if code not in (dns.rcode.NOERROR, dns.rcode.NXDOMAIN):
        return None, 'server replied '+dns.rcode.to_text(code)
    output=[]
    for rrset in result.answer:
        # A query for a CNAME can yield both; include the actual returned type.
        rt = dns.rdatatype.to_text(rrset.rdtype)
        for rr in rrset:
            data = sanitize_txt(rr.to_text()) if rt=='TXT' else rr.to_text()
            output.append({'owner':rrset.name.to_text(),'type':rt,'ttl':rrset.ttl,'value':data})
    return output, None

def main():
    addresses = {}
    for ns in DELEGATED_NS:
        addresses[ns] = lookup_ip(ns)
    observations={}
    errors=[]
    for host in HOSTS:
        bytype={}
        for rt in TYPES:
            success=False
            for ns,ip in addresses.items():
                if not ip: continue
                try:
                    data,issue=query(ip, host,rt)
                    if issue:
                        errors.append(host+' '+rt+' '+ns+': '+issue)
                        continue
                    bytype[rt]={'authority':ns,'records':data}
                    success=True
                    break
                except (OSError,dns.exception.DNSException) as exc:
                    errors.append(host+' '+rt+' '+ns+': '+type(exc).__name__)
            if not success:
                bytype[rt]={'authority':None,'records':[],'unverified':True}
        observations[host]=bytype
    required=[('prompted.fi','A'),('www.prompted.fi','A'),
              ('app.prompted.fi','CNAME'),('prompted.fi','MX')]
    complete=all(observations[h][t]['authority'] is not None for h,t in required)
    report={
       'collected_at_utc':datetime.now(timezone.utc).isoformat(),
       'status':'AUTHORITATIVE_OBSERVED' if complete else 'PARTIAL_NOT_AUTHORITY_FOR_CUTOVER',
       'delegated_nameservers':addresses,
       'hosts':observations,
       'required_queries_verified':sum(observations[h][t]['authority'] is not None for h,t in required),
       'required_queries_total':len(required),
       'query_issue_count':len(errors),
       'query_issues':errors[:24],
       'security':'TXT values redacted; no authenticated service access or DNS writes',
       'limitation':'This public record observation is not a complete Domainhotelli zone export; obtain original TTL and all records from the owner-managed DNS panel before cutover. No change to app.prompted.fi, MX, SPF, DKIM or DMARC is permitted.'
    }
    OUTPUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\\n',encoding='utf-8')
    print(json.dumps({'dns_snapshot':report['status'],'required':report['required_queries_verified'],'of':len(required),
                      'query_issues':len(errors),'report':str(OUTPUT.relative_to(ROOT))},ensure_ascii=False))

if __name__=='__main__':
    main()
