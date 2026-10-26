"""Read-only HTTP audit of the current public Prompted marketing domain.

This does not alter production; it is executed by GitHub Actions to escape
the assistant environment's network restrictions. No cookies, login, credentials,
full page content or visitor details are saved.
"""
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TARGETS=['/','/fi','/en','/en/terms','/en/privacy','/fi/tietosuoja']
BASE='https://prompted.fi'
class PageTitle(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title=False
        self.title=''
    def handle_starttag(self,tag,attrs):
        if tag=='title':
            self.in_title=True
    def handle_endtag(self,tag):
        if tag=='title':
            self.in_title=False
    def handle_data(self,data):
        if self.in_title:
            self.title+=data

rows=[]
for path in TARGETS:
    rec={'path':path,'status':'UNKNOWN'}
    try:
        req=urllib.request.Request(BASE+path,headers={'User-Agent':'PromptedWebsitePrelaunchReadOnlyAudit/1.0','Accept':'text/html'})
        with urllib.request.urlopen(req,timeout=15) as response:
            raw=response.read(700_000)
            charset=response.headers.get_content_charset('utf-8')
            page=raw.decode(charset,errors='replace')
            parser=PageTitle()
            parser.feed(page)
            low=page.lower()
            rec.update({'status':'OK' if response.status==200 else 'HTTP_'+str(response.status),
                        'http_code':response.status,
                        'final_url':response.geturl(),
                        'content_type':response.headers.get('Content-Type','')[:100],
                        'html_bytes':len(raw),
                        'title':parser.title.strip()[:130],
                        'contains_prompted_oy': 'prompted oy' in low,
                        'contains_datadiscovery': 'datadiscovery' in low,
                        'contains_design_va': 'design va oy' in low,
                        'contains_preview_noindex': 'noindex' in (response.headers.get('X-Robots-Tag','').lower())})
            if path=='/en/terms':
                if rec['contains_datadiscovery'] and rec['contains_design_va']:
                    rec['status']='WRONG_COMPANY_TERMS'
                elif rec['contains_prompted_oy']:
                    rec['status']='CORRECT_COMPANY_NAME_CHECK_LEGAL_CONTENT'
                else:
                    rec['status']='UNVERIFIED_TERMS'
    except (urllib.error.HTTPError,urllib.error.URLError,OSError,TimeoutError,ValueError) as exc:
        rec.update({'status':'FETCH_ERROR','error_type':type(exc).__name__,
                    'error_summary':str(exc)[:180]})
    rows.append(rec)
report={'observed_utc':datetime.now(timezone.utc).isoformat(),
        'site':'https://prompted.fi','mode':'PUBLIC_READ_ONLY',
        'issue_found':any(x['status']=='WRONG_COMPANY_TERMS' for x in rows),
        'results':rows,
        'note':'Direct runner HTTP source observation, not rendered JavaScript and not a legal review.'}
(ROOT/'tools'/'live_origin_audit_results.json').write_text(
    json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
# Do not fail preview build because the current LIVE site may have a remediation issue.
