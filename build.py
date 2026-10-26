from pathlib import Path
import json, html
from bs4 import BeautifulSoup, NavigableString
from buyer_experience import experience_main

# Self-contained, PRELAUNCH-ONLY generator.
# Do not remove noindex/robots without separate legal, design and publishing sign-off.
OUT = Path(__file__).resolve().parent
CFILE = OUT/'content.json'
values=json.loads(CFILE.read_text(encoding='utf-8'))
C,SERVICES,SEO=values['C'],values['SERVICES'],values['SEO_TITLES']

trans = {
'Autamme yrityksiä kehittämään tekoälylukutaitoa, uusia työtapoja ja todellista kyvykkyyttä. Digitaalinen valmennus ja näyttö muutoksesta yhdistyvät ihmisen asiantuntemukseen.':'We help organisations build AI literacy, new ways of working and lasting capability. Digital coaching and evidence of change complement human expertise.',
'Alustava pilottimalli kattaa noin 20 osallistujaa. Organisaation arviointijakso on noin 90 päivää, mutta osallistujan oppimista ei sidota pakolliseen valmistumispäivään.':'The initial pilot model is designed for around 20 participants. The organisational evaluation period is approximately 90 days, but individual learning is not tied to a mandatory completion deadline.',
'Arkkitehtoninen valo, massiivinen tila ja pieni ihminen mittakaavana':'Architectural daylight, monumental space and a small human figure for scale',
'Teknologia on täällä.':'Technology is here.',
'Muutos syntyy ihmisissä.':'Change happens through people.',
'Tutustu Capabilityyn':'Explore Capability',
'Kolme tapaa aloittaa ↗':'Three ways to begin ↗',
'TOIMINTAMALLI — EI OHJELMISTONÄKYMÄ':'METHOD VISUALISATION — NOT A SOFTWARE SCREEN',
'Työstä havaintoihin.':'From work to evidence.',
'Havainnoista uuteen kyvykkyyteen.':'From evidence to new capability.',
'Todellinen työ':'Real work',
'Tunnistetaan tehtävä ja nykyinen tapa tehdä se.':'Identify the actual task and how it is done today.',
'Uusi toimintatapa':'A new way of working',
'Harjoitellaan, toistetaan ja sovelletaan digitaalisesti tuettuna.':'Practise, repeat and transfer with digital support.',
'Todennettava muutos':'Evidence of change',
'Arvioidaan, mitä työssä todella muuttui ja miten itsenäisesti se onnistuu.':'Assess what changed in the work and how independently it can be done.',
'EI PELKKÄÄ OSALLISTUMISEN MITTAAMISTA':'NOT JUST ATTENDANCE METRICS',
'Yksi päämäärä.':'One ambition.',
'Kolme tapaa aloittaa.':'Three ways to begin.',
'Yhteinen perusta vastuulliseen tekoälyn käyttöön.':'A shared foundation for responsible AI use.',
'Uudet työtavat ja niiden muutoksen todentaminen.':'New ways of working, with evidence of change.',
'Kyvykkyyden muutos osaksi organisaation arkea.':'Embedding capability in how the organisation works.',
'OMAA TEKNOLOGIAA, OIKEAA TYÖTÄ':'OUR TECHNOLOGY, REAL WORK',
'Yksi työ. Kaksi näkökulmaa.':'One task. Two perspectives.',
'Yhteinen kuva muutoksesta.':'A shared understanding of change.',
'Oppija kehittää kyvykkyyttään omassa työssään. Organisaation tilaajalle voidaan julkaista erillinen, rajattu raportti. Näitä kahta kokemusta ei sekoiteta.':'Learners build capability in their own work. A separate, restricted report may be released to the organisation. These two experiences are kept distinct.',
'TEKNISEEN TOTEUTUKSEEN PERUSTUVA RAKENNEKUVA':'CONCEPTUAL MODEL BASED ON PRODUCT IMPLEMENTATION',
'EI OHJELMISTON RUUTUKAAPPAUS · EI ASIAKASDATAA':'NOT A SOFTWARE SCREENSHOT · NO CLIENT DATA',
'01 / OPPIMISKOKEMUS':'01 / LEARNER EXPERIENCE',
'OMAT TYÖTEHTÄVÄT':'REAL WORK TASKS',
'Työstä oman osaamisen näytöksi.':'Turning work into evidence of capability.',
'TYÖTEHTÄVÄ':'WORK TASK',
'COACH-TUKI':'COACHING SUPPORT',
'OMA NÄYTTÖ':'PERSONAL EVIDENCE',
'Valmennus auttaa tekemään seuraavan kokeilun. Näyttö vahvistuu vasta, kun uusi tapa toimia kestää toiston ja siirtyy uuteen tilanteeseen.':'Coaching supports the next experiment. Evidence grows when a new practice can be repeated and applied in a different situation.',
'Ensimmäinen näyttö':'First signal',
'Toisto':'Repeat',
'Siirto':'Transfer',
'Itsenäisyys':'Independence',
'TYÖN TULOS, EI KLIKKAUSTEN MÄÄRÄ':'WORK OUTCOMES, NOT CLICK COUNTS',
'02 / TILAAJAN DATA':'02 / BUYER DATA',
'RAJATTU NÄKYVYYS':'RESTRICTED VIEW',
'Raportointi ilman yksityisten työtekstien avaamista.':'Reporting without exposing private work texts.',
'Erillinen julkaisu':'Separate publication',
'Yhteenveto ei muodostu suoraan keskusteluista.':'Reports are not generated directly from conversations.',
'Ryhmäkohtainen näyttö':'Group-level evidence',
'Näytön vaiheita tarkastellaan hyväksytysti.':'Evidence stages are presented after review.',
'Käyttöoikeuksilla rajattu':'Access controlled',
'Tilaajalla on vain sallittu raportointinäkymä.':'Buyers see only their authorised reporting view.',
'TIETOSUOJAA EI KORVATA MARKKINOINTIVÄITTEILLÄ':'PRIVACY CANNOT BE REPLACED BY MARKETING CLAIMS',
'Tutustu Capability-toimitukseen':'Explore Capability delivery',
'Prompted yhdistää ihmislähtöisen valmennuksen ja oman digitaalisen palvelun. Rakennamme muutosta, joka kantaa yksittäistä kokeilua pidemmälle.':'Prompted combines human coaching with a proprietary digital service. We help turn individual experiments into lasting changes in work.',
'KUVALUONNOS H01 / EI HYVÄKSYTTY JULKAISUKUVA':'H01 ART STUDY / NOT APPROVED FOR PUBLICATION',
'Aloitetaan yhdestä oikeasta työtehtävästä.':'Start with one real work challenge.',
'Ota yhteyttä':'Get in touch',
'Osaaminen muuttuu arvoksi, kun':'Capability becomes valuable when',
 'työ muuttuu.':'work changes.',
'Rajattu organisaatiopilotti, jossa uudet tekoälyavusteiset työtavat rakennetaan oikeaan työhön.':'A focused organisational pilot that builds new AI-assisted ways of working in real tasks.',
'LÄHTÖTASO → VALMENNUS → TODETTU MUUTOS':'BASELINE → COACHING → EVIDENCE OF CHANGE',
'ALUSTAVA ORGANISAATIOJAKSO NOIN 90 PV':'INITIAL ORGANISATIONAL PILOT AROUND 90 DAYS',
'Keskustellaan pilotista':'Discuss the pilot',
'Yksi kehityspolku.':'One development path.',
'Kolme todennettavaa vaihetta.':'Three observable stages.',
'Prompted yhdistää työtehtävään sidotun harjoittelun, digitaalisen valmennuspalvelun ja rajatun näytön syntyneestä muutoksesta.':'Prompted connects practice in real tasks, digital coaching and carefully bounded evidence of change.',
'VISUAALINEN MENETELMÄKUVAUS. EI AITO TUOTENÄYTTÖ EIKÄ VALMIS ASIAKASRAPORTTI.':'METHOD ILLUSTRATION. NOT A LIVE PRODUCT SCREEN OR A CUSTOMER REPORT.',
'Työ ja lähtötilanne':'Real work and baseline',
'Tunnistetaan osallistujan oikea tehtävä ja tarvittava muutos, ennen kuin ryhdytään harjoittelemaan.':'Identify the participant’s actual task and the change needed before practising.',
'Digitaalinen valmennus arjessa':'Digital coaching at work',
'Osallistuja tekee, kokeilee, toistaa ja oppii omassa työkontekstissaan. Ihminen tukee kokonaisuutta.':'People experiment, repeat and learn in their own work context, with human support.',
'Näyttö muutoksesta':'Evidence of change',
'Arvioidaan havaintoja, toistoa, siirrettävyyttä ja itsenäistymistä. Tilaaja saa rajatun yhteenvedon.':'Assess signals, repeatability, transfer and independence. The buyer receives a restricted summary.',
'Keskustellaan toimituksesta':'Discuss delivery',
'RAJATTU JA KÄYTÄNNÖLLINEN':'FOCUSED AND PRACTICAL',
'Ei irrallista koulutusta. Ei epämääräistä muutoshanketta.':'Not a one-off course. Not an open-ended transformation programme.',
'Roolien ja työn konteksti':'People, roles and work context',
'Tuki omaan työhön':'Support in real tasks',
'Todennettava, rajattu näyttö':'Bounded, reviewable evidence',
'Yhteinen jatkopäätös':'A joint decision on next steps',
'Onko teillä yksi työ, jonka pitäisi muuttua?':'Is there one way of working you want to change?',
'Keskustellaan':'Let’s talk',
}

routes={'home':'','literacy':'literacy','cap':'capability','transform':'transformation','company':None,'contact':None,'privacy':None,'terms':None,'experience':None}
def url(lang,key):
 p=routes[key] if routes[key] is not None else {'company':{'fi':'yritys','en':'company'},'contact':{'fi':'yhteys','en':'contact'},'privacy':{'fi':'tietosuoja','en':'privacy'},'terms':{'fi':'ehdot','en':'terms'},'experience':{'fi':'tutustu','en':'explore'}}[key][lang]
 return f'/{lang}/'+(p+'/' if p else '')

def esc(s):return html.escape(str(s),quote=True)

def translate_fragment(markup):
 s=BeautifulSoup(str(markup),'html.parser')
 for node in list(s.find_all(string=True)):
  if node.parent and node.parent.name in ['script','style']: continue
  v=str(node); key=v.strip()
  if key in trans:
   node.replace_with(NavigableString(v.replace(key,trans[key])))
 return s

def header(lang,page):
 fi=lang=='fi'; home=url(lang,'home')
 names=[('literacy','Literacy'),('cap','Capability'),('transform','Transformation'),('experience','Demo'),('company','Yritys' if fi else 'Company')]
 nav=''.join(f'<a href="{url(lang,k)+( "#menetelma" if k=="home" else "")}"'+(' class="active" aria-current="page"' if k==page else '')+f'>{name}</a>' for k,name in names)
 other='en' if fi else 'fi'
 return f'''<header class="topbar"><div class="shell"><a href="{home}" class="logo" aria-label="Prompted — {'etusivu' if fi else 'home'}"><img src="/assets/wordmark-dark.svg" alt="Prompted" width="148" height="25"></a><nav class="nav" aria-label="{'Päänavigaatio' if fi else 'Main navigation'}">{nav}</nav><div class="bar-right"><div class="language"><a href="{url(other,page)}" hreflang="{other}" aria-label="{'EN ↗ — Read in English' if fi else 'FI ↗ — Lue suomeksi'}">{other.upper()} ↗</a></div><a href="{url(lang,'contact')}" class="navcta">{'Keskustellaan' if fi else 'Let’s talk'} ↗</a><button class="nav-toggle" type="button" aria-label="{'Avaa valikko' if fi else 'Open menu'}" aria-expanded="false" aria-controls="mobile-nav"><span></span><span></span><span></span></button></div></div><nav class="mobile-nav" id="mobile-nav" aria-hidden="true" aria-label="{'Mobiilivalikko' if fi else 'Mobile menu'}">{nav}<a href="{url(other,page)}">{'In English' if fi else 'Suomeksi'} ↗</a><a href="{url(lang,'contact')}">{'Keskustellaan' if fi else 'Let’s talk'} ↗</a></nav></header>'''

def footer(lang):
 fi=lang=='fi'
 return f'''<footer class="footer"><div class="shell"><div><strong>Prompted Oy</strong> · Turku, Finland · 3550114-7</div><div><a href="{url(lang,'company')}">{'Yritys' if fi else 'Company'}</a> · <a href="{url(lang,'privacy')}">{'Tietosuoja' if fi else 'Privacy'}</a> · <a href="{url(lang,'terms')}">{'Palveluehdot' if fi else 'Service terms'}</a> · <a href="https://app.prompted.fi" rel="noopener noreferrer">{'Kirjaudu' if fi else 'Sign in'} ↗</a></div><div>PREVIEW · NOT PUBLISHED · © 2026</div></div></footer>'''


def page_html(lang,page,main,desc=None):
 c=C[lang]; other='en' if lang=='fi' else 'fi'; title=(('Capability-demo | Tilaajalle ja osallistujalle | Prompted' if lang=='fi' else 'Capability demo | Buyer and participant | Prompted') if page=='experience' else SEO[lang][page]); description=desc or (SERVICES[lang][page]['meta'] if page in ['literacy','transform'] else c['site_desc']); current=url(lang,page)
 # open graph logo and URL; withheld from indexing during design gate.
 if page=='experience': description=('Kokeile Prompted Capabilitya tilaajana tai osallistujana. Yksi palvelu, kaksi näkökulmaa, ilman kirjautumista.' if lang=='fi' else 'Explore Prompted Capability as a buyer or participant. One service, two perspectives, no sign-in.')
 web_desc=esc(description)
 cards={ 'literacy': 'Literacy', 'cap': 'Capability', 'transform': 'Transformation' }
 ld={'@context':'https://schema.org','@graph':[
  {'@type':'Organization','@id':'https://prompted.fi/#organization','name':'Prompted Oy','legalName':'Prompted Oy','url':'https://prompted.fi/','taxID':'3550114-7','founder':{'@type':'Person','name':'Jarkko Sjöman','url':'https://jarkkosjoman.com'},'address':{'@type':'PostalAddress','addressLocality':'Turku','addressCountry':'FI'}},
  {'@type':'WebSite','@id':'https://prompted.fi/#website','url':'https://prompted.fi/','name':'Prompted','inLanguage':['fi','en']},
  {'@type':'WebPage','@id':'https://prompted.fi'+current+'#webpage','name':title,'description':description,'url':'https://prompted.fi'+current,'inLanguage':lang,'isPartOf':{'@id':'https://prompted.fi/#website'}}
 ]}
 if page in cards:ld['@graph'].append({'@type':'Service','name':'Prompted '+cards[page],'provider':{'@id':'https://prompted.fi/#organization'},'url':'https://prompted.fi'+current,'description':description,'areaServed':'Europe'})
 ld_safe_json=json.dumps(ld,ensure_ascii=False).replace('<',chr(92)+'u003c')
 content=f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="#090b09"><title>{esc(title)}</title><meta name="description" content="{web_desc}"><link rel="canonical" href="https://prompted.fi{current}"><link rel="alternate" hreflang="fi" href="https://prompted.fi{url('fi',page)}"><link rel="alternate" hreflang="en" href="https://prompted.fi{url('en',page)}"><link rel="alternate" hreflang="x-default" href="https://prompted.fi{url('fi',page)}"><meta property="og:type" content="website"><meta property="og:site_name" content="Prompted"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{web_desc}"><meta property="og:url" content="https://prompted.fi{current}"><meta property="og:image" content="https://prompted.fi/assets/share-prompted.jpg"><meta property="og:locale" content="{'fi_FI' if lang=='fi' else 'en_US'}"><link rel="icon" href="/assets/favicon.ico"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png"><link rel="stylesheet" href="/assets/concept.css"><link rel="stylesheet" href="/assets/pages.css"><link rel="stylesheet" href="/assets/product-first.css"><link rel="stylesheet" href="/assets/product-system.css">{('<link rel="stylesheet" href="/assets/buyer-experience.css">' if page=='experience' else '')}<script type="application/ld+json">{ld_safe_json}</script><script defer src="/assets/concept.js"></script>{('<script defer src="/assets/buyer-experience.js"></script>' if page=='experience' else '')}</head><body><a class="skip-link" href="#main">{'Siirry sisältöön' if lang=='fi' else 'Skip to content'}</a>{header(lang,page)}<main id="main">{main}</main>{footer(lang)}</body></html>'''
 return content




def product_first_hero(lang, page):
 fi = lang == 'fi'
 cap = page == 'cap'
 home_href = url(lang,'home')
 contact = url(lang,'contact')
 capability = url(lang,'cap')
 headline = ('Osaaminen näkyy,<br><em>kun työ muuttuu.</em>' if fi else 'Capability is visible<br><em>when work changes.</em>') if cap else ('Tekoäly osaksi<br><em>oikeaa työtä.</em>' if fi else 'Make AI part<br><em>of real work.</em>')
 lead = ('Prompted Capability yhdistää todelliset työtehtävät, digitaalisen valmennuksen ja muutoksesta syntyvän näytön. Rajattu pilotti antaa organisaatiolle perustan seuraavaan päätökseen.' if fi else 'Prompted Capability connects real work, digital coaching and reviewable evidence of change. A focused pilot gives organisations a basis for their next decision.') if cap else ('Kehitämme yritysten tekoälylukutaitoa ja uusia toimintatapoja oikeissa työtehtävissä. Digitaalinen valmennus tukee oppimista, ja näyttö auttaa arvioimaan muutosta.' if fi else 'We develop AI literacy and new ways of working through real tasks. Digital coaching supports learning, while evidence helps organisations assess change.')
 maincta = ('Avaa Capability-demo' if fi else 'Open the Capability demo') if cap else ('Katso Capability-demo' if fi else 'See the Capability demo')
 secondcta = ('Keskustellaan pilotista' if fi else 'Discuss the pilot') if cap else ('Tutustu pilottiin' if fi else 'Explore the pilot')
 first_href = url(lang,'experience')
 second_href = contact if cap else capability
 helper = (lambda fi_s,en_s: fi_s if fi else en_s)
 return f'''<section class="pf-hero {'pf-capability' if cap else 'pf-home'}" id="alku" aria-labelledby="pf-heading">
  <div class="shell pf-hero-shell">
    <div class="pf-copy">
      <div class="pf-eyebrow"><span class="pf-eyebrow-square" aria-hidden="true"></span>{'02 / PROMPTED CAPABILITY' if cap else 'PROMPTED / PEOPLE × TECHNOLOGY × WORK'}</div>
      <div class="pf-copy-main">
        <p class="pf-clarifier">{helper('Tekoälykyvykkyyden kehittämistä yrityksille', 'AI capability development for organisations')}</p>
        <h1 id="pf-heading">{headline}</h1>
        <p class="pf-intro">{lead}</p>
        <div class="pf-actions"><a class="pf-button-primary" href="{first_href}">{maincta} <span aria-hidden="true">↗</span></a><a class="pf-button-quiet" href="{second_href}">{secondcta} <span aria-hidden="true">↗</span></a></div>
      </div>
      <div class="pf-microproof" aria-label="{helper('Kolme Prompted-palvelua','Three Prompted services')}"><span>01 <b>Literacy</b></span><span>02 <b>Capability</b></span><span>03 <b>Transformation</b></span></div>
    </div>
    <div class="pf-artwork">
      <div class="pf-art-topline"><span>{helper('PROMPTED / TUOTTEEN TOIMINTAPERIAATE','PROMPTED / PRODUCT EXPERIENCE')}</span><span>2026 / CONCEPT STUDY</span></div>
      <figure class="pf-composition" aria-label="{helper('Havainnekuva Promptedin digitaalisesta valmennuspalvelusta ja rajatusta Data-raportoinnista','Illustration of Prompted digital coaching and restricted Data reporting')}">
        <div class="pf-halo" aria-hidden="true"></div>
        <div class="pf-browser" aria-hidden="true">
          <div class="pf-browser-top"><div class="pf-bdots"><i></i><i></i><i></i></div><span class="pf-browser-address">app.prompted.fi</span><div class="pf-browser-signet">P<span>.</span></div></div>
          <div class="pf-app-layout">
            <div class="pf-app-side"><div class="pf-app-mark">PROMPTED<span>.</span></div><div class="pf-side-divider"></div><div class="pf-side-link active"><i>01</i>{helper('Tänään','Today')}</div><div class="pf-side-link"><i>02</i>{helper('Oma työ','My work')}</div><div class="pf-side-link"><i>03</i>{helper('Oma kehitys','Development')}</div><div class="pf-side-link"><i>04</i>{helper('Omat tiedot','My evidence')}</div><div class="pf-side-bottom">{helper('TYÖSSÄ OPPIMINEN','LEARNING AT WORK')}</div></div>
            <div class="pf-app-content">
              <div class="pf-app-breadcrumb">CAPABILITY <span>/</span> {helper('OMA TYÖTILA','MY WORKSPACE')}</div>
              <div class="pf-app-heading"><div><small>{helper('TÄMÄN PÄIVÄN TYÖ','TODAY’S WORK')}</small><h3>{helper('Työ muuttuu tekemällä.','Change happens through doing.')}</h3></div><div class="pf-app-avatar" aria-hidden="true">P</div></div>
              <div class="pf-task-box"><div class="pf-task-head"><span>{helper('TYÖTEHTÄVÄ','WORK TASK')}</span><i>01 / 03</i></div><h4>{helper('Valitse yksi tehtävä, jonka haluat tehdä paremmin.','Choose one task you want to improve.')}</h4><div class="pf-task-rule"></div><p>{helper('Tunnista onnistumisen kriteeri. Kokeile uutta toimintatapaa aidossa työssä.','Define success. Try a new approach in real work.')}</p></div>
              <div class="pf-coach-row"><span class="pf-coach-avatar" aria-hidden="true">✳</span><div><strong>{helper('Digitaalinen valmennus','Digital coaching')}</strong><span>{helper('Seuraava pieni kokeilu, oikeassa työssä.','The next small experiment, in real work.')}</span></div><span class="pf-coach-arrow" aria-hidden="true">↗</span></div>
              <div class="pf-app-bottom"><span>{helper('TYÖ → KOKEILU → NÄYTTÖ','WORK → EXPERIMENT → EVIDENCE')}</span><span>{helper('OMA EDISTYMINEN','PERSONAL PROGRESS')}</span></div>
            </div>
          </div>
        </div>
        <div class="pf-data-overlay" aria-hidden="true"><div class="pf-data-eyebrow"><span class="pf-data-dot"></span>PROMPTED DATA <small>{helper('TILAAJAN NÄKYMÄ','BUYER VIEW')}</small></div><div class="pf-data-title">{helper('Julkaistu ryhmätason näyttö','Published group-level evidence')}</div><div class="pf-data-table"><div><span>{helper('Ryhmäraportti','Group report')}</span><b>{helper('Erillinen julkaisu','Separate release')}</b></div><div><span>{helper('Tiedon rajaus','Data boundary')}</span><b>{helper('Käyttöoikeuksin','Access controlled')}</b></div><div><span>{helper('Arvioinnin perusta','Evidence basis')}</span><b>{helper('Toisto · Siirto · Itsenäisyys','Repeat · Transfer · Independence')}</b></div></div><div class="pf-data-foot">{helper('EI YKSITYISIÄ TYÖTEKSTEJÄ','NO PRIVATE WORK TEXTS')}</div></div>
        <div class="pf-phone" aria-hidden="true"><div class="pf-phone-top"><span class="pf-phone-notch"></span></div><div class="pf-phone-content"><small>PROMPTED<span>.</span></small><div class="pf-phone-label">{helper('OMA NÄYTTÖ','MY EVIDENCE')}</div><h4>{helper('Osaaminen näkyy työssä.','Evidence from real work.')}</h4><div class="pf-phone-track"><span><i></i>{helper('Ensimmäinen näyttö','First signal')}</span><span><i></i>{helper('Toisto','Repeat')}</span><span><i></i>{helper('Siirrettävyys','Transfer')}</span><span><i></i>{helper('Itsenäisyys','Independence')}</span></div><div class="pf-phone-note">{helper('Digitaalinen palvelu / mobiilinäkymän periaate','Digital service / responsive view concept')}</div></div></div>
      </figure>
      <div class="pf-art-disclaimer"><span class="pf-disclaimer-square" aria-hidden="true"></span><span>{helper('Tuotteen todelliseen rakenteeseen perustuva havainnekuva. Ei ruutukaappaus tai asiakasdataa.','Product illustration based on the real service architecture. Not a screenshot or client data.')}</span></div>
    </div>
  </div>
</section>'''

def site_main(lang,page):
 fi=lang=='fi'; src='index' if page=='home' else 'capability'
 soup=BeautifulSoup((OUT/'templates'/f'{src}.html').read_text(),'html.parser')
 main=soup.select_one('main')
 if not fi:
  main=translate_fragment(main).select_one('main')
  for tag in main.find_all(attrs={'alt':True}):
   if tag['alt'] in trans: tag['alt']=trans[tag['alt']]
 def normalize(a):
  href=a.get('href','')
  if href.startswith('mailto:'):a['href']=url(lang,'contact'); return
  if href=='capability.html':a['href']=url(lang,'cap');return
  if href.startswith('index.html'):a['href']=url(lang,'home')+href[len('index.html'):];return
  if href=='#ratkaisut' or href=='#menetelma' or href=='#yritys':a['href']=url(lang,'home')+href;return
  if href.startswith('assets/'): a['href']='/'+href;return
  # headings link placeholder href=#ratkaisut in cards; update separately
 for a in main.find_all('a'):normalize(a)
 for img in main.find_all('img'):
  if img.get('src','').startswith('assets/'):img['src']='/'+img['src']
 # Three real destination links. Legacy concept offer tile URLs were only placeholders.
 for tile,k in zip(main.select('.offer-tile'),['literacy','cap','transform']):
  if tile.name=='a':tile['href']=url(lang,k)
  else:
   a=tile.find('a')
   if a:a['href']=url(lang,k)
 # Remove art figcaption misleading if not needed? Keep approval label explicit.
 for a in main.select('.proof-end a'):a['href']=url(lang,'cap') if page=='home' else url(lang,'contact')
 # Product-first preview hero is created per language; it replaces only the prior hero, not the product and legal material below.
 old_hero=main.select_one('.hero' if page=='home' else '.cap-hero')
 if old_hero:
  replacement=BeautifulSoup(product_first_hero(lang,page),'html.parser').select_one('section')
  old_hero.replace_with(replacement)
 if page=='cap':
  # Don't omit material terms: scope is tentative, not signed contract.
  s=BeautifulSoup(f'''<section class="additional-truth"><div class="shell"><div class="kicker"><span class="dash"></span>{'TOIMITUKSEN RAJAT' if fi else 'SCOPE AND LIMITS'}</div><div class="terms-grid"><h2>{'Pilotin ehdot sovitaan ennen aloitusta.' if fi else 'Pilot terms are agreed before delivery.'}</h2><p>{esc(C[lang]['cap_scope_body'])} {esc(C[lang]['cap_disclaimer'])}</p></div></div></section>''','html.parser')
  section=main.select_one('.closing')
  if section:section.insert_before(s)
 # page_html owns the sole <main> landmark; keep only the template contents.
 return main.decode_contents()


def service_visual(lang,key):
 fi=lang=='fi'
 t=lambda f,e: f if fi else e
 if key=='literacy':
  rows=[
   (t('Työn konteksti','Work context'),t('Roolit · Työkalut · Tilanteet','Roles · Tools · Situations')),
   (t('Harkinta','Human judgement'),t('Tarkistaminen · Riskit · Vastuu','Review · Risk · Responsibility')),
   (t('Yhteinen perusta','Shared foundation'),t('Harjoittelu oikeassa työssä','Practice in real work')),
   (t('Dokumentointi','Documentation'),t('Sovitut toimet · Jatkotarpeet','Agreed measures · Next priorities')),
  ]
  entries=''.join(f'<div class="ps-literacy-row"><span aria-hidden="true">0{i+1}</span><div><strong>{esc(title)}</strong><small>{esc(detail)}</small></div><i aria-hidden="true">↗</i></div>' for i,(title,detail) in enumerate(rows))
  return f'''<div class="ps-product-panel ps-literacy-panel" aria-label="{t('Havainnekuva lukutaidon kehittämisen osa-alueista','Illustration of the AI literacy delivery areas')}">
   <div class="ps-panel-top"><span>PROMPTED <b>LITERACY</b></span><span>{t('TOIMITUSMALLI','DELIVERY MODEL')}</span></div>
   <div class="ps-literacy-top"><span class="ps-kicker">{t('TYÖLÄHTÖINEN TEKOÄLYLUKUTAITO','WORK-RELEVANT AI LITERACY')}</span><strong>{t('Yhteinen perusta.','A shared foundation.')}<br>{t('Oikea konteksti.','Real-world context.')}</strong><p>{t('Eri rooleihin sopiva oppiminen ja dokumentoitavat toimet.','Context-sensitive learning and documented actions.')}</p></div>
   <div class="ps-literacy-rows">{entries}</div>
   <div class="ps-panel-bottom"><span>{t('EI SERTIFIKAATTI- TAI LAINMUKAISUUSTAKUUTA','NO CERTIFICATE OR COMPLIANCE GUARANTEE')}</span><span aria-hidden="true">✳</span></div>
  </div>'''
 rows=[
  (t('Johto','Leadership'),t('Yhteinen tavoite','Shared objective')),
  (t('Työ','Real work'),t('Muuttuvat toimintatavat','New ways of working')),
  (t('Kyvykkyys','Capability'),t('Valmennus ja käytännön tuki','Coaching and practical support')),
  (t('Näyttö','Evidence'),t('Toisto · Siirto · Itsenäisyys','Repeat · Transfer · Independence')),
 ]
 stages=''.join(f'<div class="ps-transform-stage"><span class="ps-transform-count">0{i+1}</span><div><small>{esc(title)}</small><strong>{esc(detail)}</strong></div></div>' for i,(title,detail) in enumerate(rows))
 return f'''<div class="ps-product-panel ps-transform-panel" aria-label="{t('Havainnekuva organisaation muutostyön toimintamallista','Illustration of the organisational transformation approach')}">
  <div class="ps-panel-top"><span>PROMPTED <b>TRANSFORMATION</b></span><span>{t('MUUTOSMALLI','CHANGE MODEL')}</span></div>
  <div class="ps-transform-head"><div class="ps-kicker">{t('STRATEGIASTA ARJEN TYÖHÖN','FROM STRATEGY TO WORK')}</div><strong>{t('Muutos ei ole','Change is not')}<br>{t('käyttöönottoprosentti.','an adoption percentage.')}</strong></div>
  <div class="ps-transform-stages">{stages}</div>
  <div class="ps-panel-bottom"><span>{t('RÄÄTÄLÖITY YHTEISTYÖ · EI VAKIOITU PAKETTI','TAILORED ENGAGEMENT · NOT A FIXED PACKAGE')}</span><span aria-hidden="true">↗</span></div>
 </div>'''


def service_main(lang,key):
 d=SERVICES[lang][key]; fi=lang=='fi'
 stages=''.join(f'<div class="detail-stage"><small>{esc(s[0])}</small><h3>{esc(s[1])}</h3></div>' for s in d['steps'])
 faq=''.join(f'<details class="faq-item"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q,a in d['faq'])
 subtitle= ('YHTEINEN PERUSTA' if fi else 'A SHARED FOUNDATION') if key=='literacy' else ('MUUTOS JOHTAA TYÖHÖN' if fi else 'CHANGE STARTS WITH WORK')
 side = service_visual(lang,key)
 note = 'Havainnekuva toimituksen toimintaperiaatteesta. Ei todellinen ohjelmistonäkymä tai asiakastulos.' if fi else 'Conceptual delivery illustration. Not a real software screen or customer result.'
 next_head = ('Kun yhteinen perusta on rakennettu, miten työtavat kehittyvät?' if fi else 'Once the foundation is in place, how do ways of working improve?') if key=='literacy' else ('Tarvitsetteko ensin rajatun, mitattavan kokeilun?' if fi else 'Would a focused, reviewable pilot be the right starting point?')
 next_body = ('Capability vie kehittämisen yksittäisistä oppimistoimista työhön, toistoon ja itsenäiseen soveltamiseen.' if fi else 'Capability takes development beyond learning activities and into real work, repeatability and independent application.') if key=='literacy' else ('Capability tarjoaa rajatumman lähtökohdan ennen laajemman organisaatiomuutoksen suunnittelua.' if fi else 'Capability provides a focused starting point before planning a wider organisational change.')
 next_cta = 'Tutustu Capabilityyn' if fi else 'Explore Capability'
 bridge=f'''<section class="ps-bridge"><div class="shell ps-bridge-grid"><span class="ps-kicker">{('SEURAAVA ASKEL' if fi else 'NEXT STEP')}</span><div><h2>{next_head}</h2><p>{next_body}</p><a href="{url(lang,'cap')}">{next_cta} <span aria-hidden="true">↗</span></a></div></div></section>'''
 return f'''<section class="ps-service-hero ps-service-{key}" aria-labelledby="ps-service-heading"><div class="shell ps-service-grid">
  <div class="ps-service-copy"><div class="ps-eyebrow"><span aria-hidden="true"></span>{esc(d['eyebrow'])}</div>
    <div><p class="ps-hero-label">{subtitle}</p><h1 id="ps-service-heading">{esc(('Tekoälylukutaito alkaa oikeasta työstä.' if fi else 'AI literacy starts with real work.') if key=='literacy' else d['h1'])}</h1><p class="ps-service-intro">{esc(d['intro'])}</p>
    <div class="ps-service-actions"><a class="pf-button-primary" href="{url(lang,'contact')}">{esc(d['cta'])} <span aria-hidden="true">↗</span></a><a class="pf-button-quiet" href="#toimitus">{'Näin etenemme' if fi else 'How it works'} <span aria-hidden="true">↓</span></a></div></div>
    <div class="ps-service-keyline"><span>{'01 / LITERACY' if key=='literacy' else '03 / TRANSFORMATION'}</span><span>{'PROMPTED / PEOPLE × TECHNOLOGY × WORK'}</span></div></div>
  <div class="ps-service-visual"><div class="ps-art-meta"><span>{'TOIMITUKSEN PERIAATE' if fi else 'DELIVERY PRINCIPLE'}</span><span>CONCEPT STUDY</span></div>{side}
   <p class="ps-concept-disclaimer"><span aria-hidden="true"></span>{note}</p></div>
 </div></section>
 <section class="detail-why"><div class="shell detail-why-grid"><span class="kicker">{'MIKSI TÄMÄ' if fi else 'WHY IT MATTERS'}</span><div><h2>{esc(d['why_title'])}</h2><p>{esc(d['why'])}</p></div></div></section>
 <section class="detail-process" id="toimitus"><div class="shell"><div class="kicker"><span class="dash"></span>{'MITEN ETENEMME' if fi else 'HOW WE WORK'}</div><h2>{'Selkeä lähtö. Todellinen työ. Tunnistettava seuraava askel.' if fi else 'A clear starting point. Real work. A meaningful next step.'}</h2><div class="detail-stages">{stages}</div></div></section>
 <section class="detail-context"><div class="shell context-grid"><div><div class="kicker"><span class="dash"></span>{'KENELLE' if fi else 'FOR WHOM'}</div><h2>{esc(d['who_title'])}</h2><p>{esc(d['who'])}</p></div><div class="context-limit"><div class="kicker">{'RAJAUKSET' if fi else 'BOUNDARIES'}</div><h3>{esc(d['bound_title'])}</h3><p>{esc(d['bound'])}</p></div></div></section>
 {bridge}<section class="detail-faq"><div class="shell"><h2>{'Usein kysyttyä' if fi else 'Frequently asked questions'}</h2>{faq}</div></section>{close_section(lang,d['cta'])}'''

def close_section(lang,cta=None):
 fi=lang=='fi'; return f'<section class="closing"><div class="shell"><h2>{"Aloitetaan yhdestä oikeasta haasteesta." if fi else "Let’s start with one real challenge."}</h2><a href="{url(lang,"contact")}">{esc(cta or ("Ota yhteyttä" if fi else "Get in touch"))} <span>↗</span></a></div></section>'

def utility_main(lang,page):
 fi=lang=='fi';c=C[lang]
 if page=='company':
  return f'''<section class="detail-hero company-hero"><div class="shell"><div class="cap-eyebrow">{esc(c['company_eyebrow'])}</div><div class="detail-hero-grid"><h1>{esc(c['company_title'])}</h1><div class="detail-aside"><p>{esc(c['company_lead'])}</p><p>{esc(c['company_body'])}</p></div></div></div></section><section class="detail-context"><div class="shell context-grid"><div><div class="kicker"><span class="dash"></span>{'PERUSTAJA' if fi else 'FOUNDER'}</div><h2>Jarkko Sjöman</h2><p>{'Promptedin perustaja. Taustalla yritysviestinnän, strategisen kehittämisen ja ihmisten valmentamisen työtä. Teknologia täydentää ihmisen tekemistä, ei korvaa sitä.' if fi else 'Founder of Prompted. Background in business communications, strategic development and working with people. Technology supports human capability rather than replacing it.'}</p><a class="profile-link" href="https://jarkkosjoman.com" rel="noopener noreferrer">jarkkosjoman.com ↗</a></div><div class="context-limit"><div class="kicker">{'YRITYS' if fi else 'COMPANY'}</div><h3>Prompted Oy</h3><p>Turku, Finland · Business ID 3550114-7</p><p>{'Yritys kehittää digitaalisen valmennuksen ja todennettavan työssä oppimisen palveluja.' if fi else 'The company develops services for digital coaching and evidence-based learning in real work.'}</p></div></div></section>{close_section(lang)}'''
 if page=='contact':
  return f'''<section class="detail-hero contact-hero"><div class="shell"><div class="cap-eyebrow">{esc(c['contact_eyebrow'])}</div><div class="detail-hero-grid"><h1>{esc(c['contact_page_title'])}</h1><div class="detail-aside"><p>{esc(c['contact_page_body'])}</p><a class="action-primary" href="mailto:jarkko@prompted.fi">{'Kirjoita suoraan' if fi else 'Email us directly'} <b aria-hidden="true">↗</b></a><p class="address-link">jarkko@prompted.fi</p></div></div></div></section><section class="closing"><div class="shell"><h2>{'Aloitetaan keskustelusta.' if fi else 'Start with a conversation.'}</h2><a href="mailto:jarkko@prompted.fi">jarkko@prompted.fi <span>↗</span></a></div></section>'''
 if page=='privacy':
  def legal_para(s):
   value=esc(s)
   value=value.replace('jarkko@prompted.fi','<a href="mailto:jarkko@prompted.fi">jarkko@prompted.fi</a>')
   return value.replace('tietosuoja.fi','<a href="https://tietosuoja.fi/" rel="noopener noreferrer">tietosuoja.fi</a>')
  title_markup=esc(c['privacy_title']).replace('Tietosuojaseloste','Tietosuoja<wbr>seloste')
  sections=''.join(f'<section class="legal-section" id="privacy-{i:02d}" aria-labelledby="privacy-title-{i:02d}"><h2 id="privacy-title-{i:02d}">{esc(h)}</h2><p>{legal_para(b)}</p></section>' for i,(h,b) in enumerate(c['privacy_sections'],1))
  links=''.join(f'<li><a href="#privacy-{i:02d}"><span aria-hidden="true">{i:02d}</span>{esc(h)}</a></li>' for i,(h,_) in enumerate(c['privacy_sections'],1))
  toc=f'<section class="legal-toc-wrap"><div class="shell"><details class="legal-toc"><summary>{"Sisällys" if fi else "Contents"} <span class="legal-toc-count">{len(c["privacy_sections"])} {"osiota" if fi else "sections"}</span></summary><ol>{links}</ol></details></div></section>'
  return f'''<section class="legal-hero"><div class="shell"><div class="cap-eyebrow">PROMPTED / {'TIETOSUOJA' if fi else 'PRIVACY'}</div><h1>{title_markup}</h1><p>{esc(c['privacy_intro'])}</p><div class="legal-draft">{'LUONNOS / EI JURIDISESTI HYVÄKSYTTY JULKAISUSISÄLTÖ' if fi else 'DRAFT / NOT YET LEGALLY APPROVED FOR PUBLICATION'}</div></div></section>{toc}<section class="legal-body"><div class="shell">{sections}</div></section>'''
 if page=='terms':
  def terms_para(s):
   value=esc(s).replace('jarkko@prompted.fi','<a href="mailto:jarkko@prompted.fi">jarkko@prompted.fi</a>')
   token='tietosuojaselosteessamme' if fi else 'privacy notice'
   href='/fi/tietosuoja/' if fi else '/en/privacy/'
   return value.replace(token,f'<a href="{href}">{token}</a>')
  sections=''.join(f'<section class="legal-section" id="terms-{i:02d}" aria-labelledby="terms-title-{i:02d}"><h2 id="terms-title-{i:02d}">{esc(h)}</h2><p>{terms_para(b)}</p></section>' for i,(h,b) in enumerate(c['terms_sections'],1))
  links=''.join(f'<li><a href="#terms-{i:02d}"><span aria-hidden="true">{i:02d}</span>{esc(h)}</a></li>' for i,(h,_) in enumerate(c['terms_sections'],1))
  toc=f'<section class="legal-toc-wrap"><div class="shell"><details class="legal-toc"><summary>{"Sisällys" if fi else "Contents"} <span class="legal-toc-count">{len(c["terms_sections"])} {"osiota" if fi else "sections"}</span></summary><ol>{links}</ol></details></div></section>'
  return f'''<section class="legal-hero"><div class="shell"><div class="cap-eyebrow">PROMPTED / {'EHDOT' if fi else 'TERMS'}</div><h1>{esc(c['terms_title'])}</h1><p>{esc(c['terms_body'])}</p><div class="legal-draft">{'LUONNOS / TARKISTETTAVA ENNEN JULKAISUA' if fi else 'DRAFT / TO BE REVIEWED BEFORE PUBLICATION'}</div></div></section>{toc}<section class="legal-body"><div class="shell">{sections}</div></section>'''
 raise ValueError(page)

for lang in ('fi','en'):
 for page in ['home','literacy','cap','transform','company','contact','privacy','terms','experience']:
  main=(experience_main(lang) if page=='experience' else (site_main(lang,page) if page in ['home','cap'] else (service_main(lang,page) if page in ['literacy','transform'] else utility_main(lang,page))))
  p=OUT/url(lang,page).lstrip('/')/'index.html'
  p.parent.mkdir(parents=True,exist_ok=True)
  desc=SERVICES[lang][page]['meta'] if page in ['literacy','transform'] else (C[lang]['cap_lead'] if page=='cap' else None)
  p.write_text(page_html(lang,page,main,desc),encoding='utf-8')
(OUT/'index.html').write_text('<!doctype html><html lang="fi"><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow"><meta http-equiv="refresh" content="0;url=/fi/"><title>Prompted</title></head><body><a href="/fi/">Prompted</a></body></html>',encoding='utf-8')
(OUT/'robots.txt').write_text('User-agent: *\nDisallow: /\n',encoding='utf-8')
# Only limited prelaunch headers; stronger production controls must be reviewed on the real Vercel deployment.
vercel={'version':2,'cleanUrls':False,'trailingSlash':True,'redirects':[{'source':'/','destination':'/fi/','permanent':False},{'source':'/capability','destination':'/fi/capability/','permanent':True},{'source':'/literacy','destination':'/fi/literacy/','permanent':True},{'source':'/transformation','destination':'/fi/transformation/','permanent':True},{'source':'/transformerism','destination':'/fi/transformation/','permanent':True},{'source':'/fi/transformerism','destination':'/fi/transformation/','permanent':True},{'source':'/en/transformerism','destination':'/en/transformation/','permanent':True},{'source':'/capability/','destination':'/fi/capability/','permanent':True},{'source':'/literacy/','destination':'/fi/literacy/','permanent':True},{'source':'/transformation/','destination':'/fi/transformation/','permanent':True},{'source':'/transformerism/','destination':'/fi/transformation/','permanent':True},{'source':'/fi/transformerism/','destination':'/fi/transformation/','permanent':True},{'source':'/en/transformerism/','destination':'/en/transformation/','permanent':True}],'headers':[{'source':'/(.*)','headers':[{'key':'X-Content-Type-Options','value':'nosniff'},{'key':'Referrer-Policy','value':'strict-origin-when-cross-origin'},{'key':'X-Frame-Options','value':'DENY'},{'key':'Permissions-Policy','value':'camera=(), microphone=(), geolocation=(), payment=()'},{'key':'X-Robots-Tag','value':'noindex, nofollow'}, {'key':'Content-Security-Policy','value':"default-src 'self'; object-src 'none'; base-uri 'self'; frame-ancestors 'none'; form-action 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; upgrade-insecure-requests"}]}]}
(OUT/'vercel.json').write_text(json.dumps(vercel,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('BUILT',len(list(OUT.glob('*/**/index.html'))),'pages',OUT)
