from pathlib import Path
p=Path(__file__).resolve().parents[1]
f=p/'build.py'
s=f.read_text(encoding='utf-8')
if 'def product_first_hero(' in s:
    raise SystemExit('Hero already implemented')
impl=r"""

def product_first_hero(lang, page):
 fi = lang == 'fi'
 cap = page == 'cap'
 home_href = url(lang,'home')
 contact = url(lang,'contact')
 capability = url(lang,'cap')
 headline = ('Kyvykkyys kasvaa,<br><em>kun työ muuttuu.</em>' if fi else 'Capability grows<br><em>when work changes.</em>') if cap else ('Tekoäly osaksi<br><em>oikeaa työtä.</em>' if fi else 'Make AI part<br><em>of real work.</em>')
 lead = ('Prompted Capability yhdistää todelliset työtehtävät, digitaalisen valmennuksen ja muutoksesta syntyvän näytön. Rajattu pilotti antaa organisaatiolle perustan seuraavaan päätökseen.' if fi else 'Prompted Capability connects real work, digital coaching and reviewable evidence of change. A focused pilot gives organisations a basis for their next decision.') if cap else ('Kehitämme yritysten tekoälylukutaitoa ja uusia toimintatapoja oikeissa työtehtävissä. Digitaalinen valmennus tukee oppimista, ja näyttö auttaa arvioimaan muutosta.' if fi else 'We develop AI literacy and new ways of working through real tasks. Digital coaching supports learning, while evidence helps organisations assess change.')
 maincta = ('Keskustellaan pilotista' if fi else 'Discuss the pilot') if cap else ('Tutustu Capabilityyn' if fi else 'Explore Capability')
 secondcta = ('Tutustu toimintamalliin' if fi else 'See the approach') if cap else ('Tutustu ratkaisuihin' if fi else 'Explore solutions')
 first_href = contact if cap else capability
 second_href = '#menetelma' if cap else '#ratkaisut'
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

"""
s=s.replace('def site_main(lang,page):',impl+'def site_main(lang,page):')
s=s.replace(" if page=='cap':\n  # Don't omit material terms", " # Product-first preview hero is created per language; it replaces only the prior hero, not the product and legal material below.\n old_hero=main.select_one('.hero' if page=='home' else '.cap-hero')\n if old_hero:\n  replacement=BeautifulSoup(product_first_hero(lang,page),'html.parser').select_one('section')\n  old_hero.replace_with(replacement)\n if page=='cap':\n  # Don't omit material terms")
s=s.replace('<link rel="stylesheet" href="/assets/pages.css">','<link rel="stylesheet" href="/assets/pages.css"><link rel="stylesheet" href="/assets/product-first.css">')
f.write_text(s,encoding='utf-8')
print('Added product-first hero to generator; all other 16 pages preserved')
