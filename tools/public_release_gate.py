"""Fail-closed public marketing release preparation. Never deploys, merges or edits DNS.

--check generates a truthful BLOCKED/ELIGIBLE report for the protected preview.
--prepare assembles an isolated static public package only after explicit,
evidence-bearing release approvals and removal of all open legal placeholders.
The source preview (noindex/SSO/draft labels) remains unchanged.
"""
import argparse
import hashlib
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
            'tietosuojaluonnos','this draft notice',
            'suunniteltu säilytyskäytäntö','our proposed retention practice')
MARKERS=('LUONNOS','DRAFT','PREVIEW · NOT PUBLISHED','KUVALUONNOS H01',
         'H01 ART STUDY')
IMAGE_APPROVAL_ASSETS={
    'assets/hero-daylight.webp', 'assets/share-prompted.jpg',
    'assets/wordmark-dark.svg', 'assets/favicon.ico',
    'assets/apple-touch-icon.png',
}

PRIVACY_APPROVAL_ASSETS={
    'content.json', 'fi/tietosuoja/index.html', 'en/privacy/index.html',
    'LEGITIMATE_INTEREST_BALANCING.md', 'MARKETING_ENQUIRY_RETENTION_SOP.md',
}
PRIVACY_PRELAUNCH_SAFEGUARDS=('rights_request_absence_continuity', 'provider_transfer_operations')
PREVIEW_HTTP_ASSETS={
    'index.html','robots.txt','vercel.json',
    'assets/buyer-experience.css','assets/buyer-experience.js',
    'assets/concept.css','assets/concept.js','assets/pages.css',
    'assets/product-first.css','assets/product-system.css',
} | {f'{lang}/{route}/index.html' if route else f'{lang}/index.html'
     for lang,rr in ROUTES.items() for route in rr}


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
        if gate=='privacy_legal':
            blobs=approval.get('approved_privacy_blobs')
            if not isinstance(blobs,dict) or set(blobs)!=PRIVACY_APPROVAL_ASSETS:
                problems.append('privacy_legal: approved privacy file list is missing or changed')
            else:
                for relpath,expected in blobs.items():
                    if not isinstance(expected,str) or not re.fullmatch(r'[0-9a-f]{40}',expected):
                        problems.append(f'privacy_legal: invalid approved SHA: {relpath}')
                        continue
                    try:
                        content=(ROOT/relpath).read_bytes()
                        actual=hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()
                        if actual!=expected:
                            problems.append(f'privacy_legal: approved privacy file changed: {relpath}')
                    except OSError:
                        problems.append(f'privacy_legal: approved privacy file absent: {relpath}')
            safeguards=approval.get('prelaunch_safeguards')
            for key in PRIVACY_PRELAUNCH_SAFEGUARDS:
                item=safeguards.get(key) if isinstance(safeguards,dict) else None
                if not isinstance(item,dict) or item.get('status')!='verified' or not isinstance(item.get('evidence'),str) or not item['evidence'].strip():
                    problems.append(f'privacy_legal: prelaunch safeguard not verified: {key}')
        if gate=='preview_http':
            blobs=approval.get('approved_preview_blobs')
            if not isinstance(blobs,dict) or set(blobs)!=PREVIEW_HTTP_ASSETS:
                problems.append('preview_http: reviewed file set differs from approved preview snapshot')
            else:
                for relpath,expected in blobs.items():
                    if not isinstance(expected,str) or not re.fullmatch(r'[0-9a-f]{40}',expected):
                        problems.append(f'preview_http: invalid Git blob for {relpath}')
                        continue
                    try:
                        content=(ROOT/relpath).read_bytes()
                        actual=hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()
                        if actual!=expected:
                            problems.append(f'preview_http: reviewed preview file changed: {relpath}')
                    except OSError:
                        problems.append(f'preview_http: reviewed preview file missing: {relpath}')
        if gate=='image_rights':
            blobs=approval.get('approved_asset_blobs')
            if not isinstance(blobs,dict) or set(blobs)!=IMAGE_APPROVAL_ASSETS:
                problems.append('image_rights: expected exact five approved image/brand asset blobs')
            else:
                for relpath,expected in blobs.items():
                    if not isinstance(expected,str) or not re.fullmatch(r'[0-9a-f]{40}',expected):
                        problems.append(f'image_rights: invalid Git blob SHA for {relpath}')
                        continue
                    try:
                        content=(ROOT/relpath).read_bytes()
                        actual=hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()
                        if actual!=expected:
                            problems.append(f'image_rights: asset changed since approval: {relpath}')
                    except OSError:
                        problems.append(f'image_rights: approved asset missing: {relpath}')
        if gate=='owner_release':
            if approval.get('explicit_public_release') is not True:
                problems.append('owner_release: explicit_public_release must be true')
            approved_sha=approval.get('approved_commit_sha','')
            if not isinstance(approved_sha,str) or not re.fullmatch(r'[0-9a-f]{40}',approved_sha):
                problems.append('owner_release: approved_commit_sha must be an exact 40-character Git SHA')
            else:
                try:
                    current_sha=subprocess.run(
                        ['git','rev-parse','HEAD'],cwd=ROOT,
                        text=True,capture_output=True,check=True
                    ).stdout.strip()
                    if approved_sha!=current_sha:
                        problems.append('owner_release: approved_commit_sha differs from current source HEAD')
                except (OSError,subprocess.CalledProcessError):
                    problems.append('owner_release: source Git commit not available to verify approval')
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
    parser.add_argument('--approval-file',type=Path,default=ROOT/'PUBLIC_RELEASE_APPROVALS.json')
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
