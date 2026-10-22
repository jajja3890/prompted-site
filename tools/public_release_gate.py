"""Fail-closed public marketing release preparation. Never deploys, merges or edits DNS.

--check generates a truthful BLOCKED/ELIGIBLE report for the protected preview.
--prepare assembles an isolated static public package only after explicit,
evidence-bearing release approvals and removal of all open legal placeholders.
The source preview (noindex/SSO/draft labels) remains unchanged.
"""
import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path
from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
GATES=('privacy_legal','image_rights','commercial_copy','preview_http',
       'visual_device','domain_rollback','owner_release')
ROUTES={'fi':['','literacy','capability','transformation','yritys',
              'yhteys','tietosuoja','ehdot','tutustu'],
        'en':['','literacy','capability','transformation','company',
              'contact','privacy','terms','explore']}
ASSET_ALLOWLIST={'apple-touch-icon.png','buyer-experience.css','buyer-experience.js',
                 'concept.css','concept.js','favicon.ico','hero-daylight.webp',
                 'pages.css','product-first.css','product-system.css',
                 'share-prompted.jpg','wordmark-dark.svg'}
LEGAL_OPEN=('vahvistettava','ennen julkaisua','to verify','before publication',
            'tietosuojaluonnos','this draft notice')
MARKERS=('LUONNOS','DRAFT','PREVIEW · NOT PUBLISHED','KUVALUONNOS H01',
         'H01 ART STUDY')

def pages():
    return [ROOT/lang/route/'index.html' for lang,rr in ROUTES.items() for route in rr]

def read_approvals(path):
    try:
        data=json.loads(path.read_text(encoding='utf-8'))
        if not isinstance(data,dict):
            raise ValueError('approval manifest must be a JSON object')
        return data, []
    except (OSError,ValueError) as exc:
        return {}, [f'approval manifest not readable: {exc}']

def check(approval_path):
    data,problems=read_approvals(approval_path)
    for gate in GATES:
        approval=data.get(gate)
        if not isinstance(approval,dict) or approval.get('status')!='approved':
            problems.append(f'{gate}: accountable approval missing')
            continue
        for field in ('approver','approved_on','evidence'):
            if not isinstance(approval.get(field),str) or not approval[field].strip():
                problems.append(f'{gate}: {field} missing')
        if gate=='owner_release' and approval.get('explicit_public_release') is not True:
            problems.append('owner_release: explicit_public_release must be true')
    try:
        content=json.loads((ROOT/'content.json').read_text(encoding='utf-8'))
        for lang in ('fi','en'):
            c=content['C'][lang]
            privacy=' '.join([c['privacy_intro']]+[h+' '+body for h,body in c['privacy_sections']])
            for token in LEGAL_OPEN:
                if token in privacy.lower():
                    problems.append(f'{lang}: unresolved legal placeholder: {token}')
            if len(c['privacy_sections'])<8:
                problems.append(f'{lang}: incomplete marketing privacy notice')
            if len(c.get('terms_sections',[]))<9:
                problems.append(f'{lang}: incomplete marketing-only terms')
            if any(any(token in (h+' '+body).lower() for token in LEGAL_OPEN) for h,body in c.get('terms_sections',[])):
                problems.append(f'{lang}: unresolved terms placeholder')
            if 'datadiscovery' in c['terms_body'].lower() or 'design va' in c['terms_body'].lower():
                problems.append(f'{lang}: historical third-party terms present')
    except (OSError,ValueError,KeyError,TypeError) as exc:
        problems.append('content file invalid: '+str(exc))
    for p in pages():
        if not p.is_file():
            problems.append('missing generated route: '+str(p.relative_to(ROOT)))
            continue
        soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
        if soup.find('meta',attrs={'name':'robots','content':'noindex,nofollow'}) is None:
            problems.append('preview safety missing, refusing to package: '+str(p.relative_to(ROOT)))
        for node in soup.find_all(['img','link','script','source']):
            href=node.get('src') or node.get('href','')
            if href.startswith('/assets/'):
                asset=href.split('/assets/',1)[1].split('?',1)[0]
                if asset not in ASSET_ALLOWLIST:
                    problems.append('unreviewed asset referenced: '+asset)
    return list(dict.fromkeys(problems))

def make_public(out):
    if out.exists():
        raise ValueError('refusing to overwrite existing output directory')
    if out.resolve()==ROOT.resolve() or ROOT.resolve().is_relative_to(out.resolve()):
        raise ValueError('output cannot contain source repository')
    out.mkdir(parents=True)
    try:
        for lang,rr in ROUTES.items():
            for route in rr:
                source=ROOT/lang/route/'index.html'
                soup=BeautifulSoup(source.read_text(encoding='utf-8'),'html.parser')
                for tag in soup.find_all('meta',attrs={'name':'robots'}):
                    tag.decompose()
                for tag in soup.select('.legal-draft'):
                    tag.decompose()
                for figure in soup.select('figure.art-figure'):
                    for cap in figure.select('figcaption'):
                        if 'KUVALUONNOS H01' in cap.get_text() or 'H01 ART STUDY' in cap.get_text():
                            cap.decompose()
                for node in soup.select('.footer *'):
                    if node.string and 'PREVIEW · NOT PUBLISHED' in node.string:
                        node.string=node.string.replace('PREVIEW · NOT PUBLISHED · ','')
                html=str(soup)
                if 'noindex' in html.lower() or any(s in html for s in MARKERS):
                    raise ValueError('unresolved preview/draft marker: '+str(source))
                target=out/lang/route/'index.html'
                target.parent.mkdir(parents=True,exist_ok=True)
                target.write_text(html,encoding='utf-8')
        root=BeautifulSoup((ROOT/'index.html').read_text(encoding='utf-8'),'html.parser')
        for tag in root.find_all('meta',attrs={'name':'robots'}):
            tag.decompose()
        (out/'index.html').write_text(str(root),encoding='utf-8')
        (out/'assets').mkdir()
        for name in sorted(ASSET_ALLOWLIST):
            src=ROOT/'assets'/name
            if not src.is_file():
                raise ValueError('approved asset not found: '+name)
            shutil.copy2(src,out/'assets'/name)
        config=json.loads((ROOT/'vercel.json').read_text(encoding='utf-8'))
        for group in config['headers']:
            group['headers']=[h for h in group['headers'] if h['key'].lower()!='x-robots-tag']
        (out/'vercel.json').write_text(json.dumps(config,indent=2)+'\n',encoding='utf-8')
        (out/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://prompted.fi/sitemap.xml\n',encoding='utf-8')
        ns='http://www.sitemaps.org/schemas/sitemap/0.9'
        tree=ET.Element('urlset',xmlns=ns)
        for lang,rr in ROUTES.items():
            for route in rr:
                url=ET.SubElement(tree,'url')
                ET.SubElement(url,'loc').text='https://prompted.fi/'+lang+'/'+(route+'/' if route else '')
        ET.ElementTree(tree).write(out/'sitemap.xml',encoding='utf-8',xml_declaration=True)
        if len(list(out.glob('*/**/index.html')))!=18:
            raise ValueError('release must contain exactly 18 FI/EN pages')
        # Intentionally exclude source Python files, node_modules, approval evidence and unused artwork.
    except Exception:
        shutil.rmtree(out,ignore_errors=True)
        raise

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',action='store_true',help='Evaluate only, expected BLOCKED preapproval')
    parser.add_argument('--prepare',action='store_true',help='Assemble private output, never deploy')
    parser.add_argument('--approval-file',type=Path,default=ROOT/'PUBLIC_RELEASE_APPROVALS.example.json')
    parser.add_argument('--commit-sha',default='')
    parser.add_argument('--out',type=Path,default=ROOT/'public_release_out')
    args=parser.parse_args()
    if args.prepare==args.check:
        parser.error('Choose exactly one of --check or --prepare')
    problems=check(args.approval_file)
    if args.prepare:
        sha=subprocess.run(['git','rev-parse','HEAD'],cwd=ROOT,text=True,
                           capture_output=True,check=True).stdout.strip()
        if not args.commit_sha or args.commit_sha!=sha:
            problems.append('explicit --commit-sha does not equal checked-out source SHA')
    report={'status':'BLOCKED' if problems else 'ELIGIBLE','public_artifact_created':False,
            'gates':list(GATES),'blockers':problems,'checks':'approval evidence, legal placeholders, preview safety, reviewed asset list'}
    (ROOT/'tools'/'public_release_gate_results.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False))
    if args.prepare:
        if problems:
            raise SystemExit('Public release packaging BLOCKED; no publishable artifact emitted')
        make_public(args.out)
        print('Assembled PRIVATE release folder:',args.out)
    # --check deliberately returns 0 even when BLOCKED: pending legal sign-off is expected
if __name__=='__main__':
    main()
