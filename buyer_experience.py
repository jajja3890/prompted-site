"""Login-free, static Buyer-Led Product Experience: illustrative, no tenant data or live LLM."""
from html import escape


def experience_main(lang):
    fi = lang == 'fi'
    t=lambda fi_text,en_text: fi_text if fi else en_text
    cards=[
      ("people",t("HR / People","HR / People"),t("Miten näemme, että oppiminen muuttaa työtä?","How do we know learning changes work?")),
      ("leader",t("Liiketoimintajohto","Business leader"),t("Mikä muuttuu käytännössä ja mitä se voisi tarkoittaa?","What changes in practice, and what could that mean?")),
      ("learner",t("Osallistuja","Participant"),t("Miten saan valmennuksesta apua omaan tehtävääni?","How will coaching help me in a real task?")),
    ]
    roles=''.join(f'<button type="button" class="be-option" data-role="{id}" aria-pressed="false"><span class="be-option-title">{escape(title)}</span><small>{escape(desc)}</small><span class="be-option-arrow" aria-hidden="true">↗</span></button>' for id,title,desc in cards)
    scenarios=[
      ("quality",t("Laajan aineiston laadunvarmistus","Quality-check complex material"),t("Tunnista väitteet, varmista lähteet, tarkista lopputulos.","Find claims, validate sources and review the result.")),
      ("report",t("Toistuva asiakasraportti","Recurring client report"),t("Muuta toistuva työ selkeäksi, uudelleen käytettäväksi tavaksi.","Turn repeated work into a method you can reuse.")),
      ("decision",t("Päätösvaihtoehtojen vertailu","Compare decision options"),t("Aseta kriteerit ja haasta omaa ajattelua.","Set criteria and challenge your assumptions.")),
    ]
    scenarios_markup=''.join(f'<button type="button" class="be-option" data-scenario="{id}" aria-pressed="false"><span class="be-option-title">{escape(title)}</span><small>{escape(desc)}</small><span class="be-option-arrow" aria-hidden="true">↗</span></button>' for id,title,desc in scenarios)
    steps=[t("Työtilanne","Work scenario"),t("Valmennus","Coaching"),t("Näyttö","Evidence"),t("Tilaajan Data","Buyer Data"),t("Vaikutus","Impact")]
    nav=''.join(f'<button type="button" class="be-stage" data-step="{idx}" aria-current="{ "step" if idx==0 else "false" }"><span>0{idx+1}</span><b>{escape(name)}</b></button>' for idx,name in enumerate(steps))
    disclaimer=t("Tämä on vuorovaikutteinen, fiktiiviseen esimerkkitilanteeseen perustuva tuotekokeilu. Se ei ole kirjautunut asiakastili, oikea tekoälykeskustelu eikä osoitus kävijän osaamisesta.",
                 "This interactive product walkthrough uses fictional examples. It is not a logged-in customer account, a live AI conversation or an assessment of your skills.")
    return f'''<section class="be-intro" aria-labelledby="be-page-title"><div class="shell be-intro-grid">
      <div><p class="be-eyebrow"><span class="be-live-dot" aria-hidden="true"></span>PROMPTED / PRODUCT EXPERIENCE <span class="be-tag">{t('EI KIRJAUTUMISTA','NO SIGN-IN')}</span></p>
        <h1 id="be-page-title">{t('Älä vain katso tuotetta.','Don’t just look at the product.')}<br><em>{t('Kokeile sen ideaa.','Experience how it works.')}</em></h1>
        <p class="be-intro-lead">{t('Valitse oma näkökulmasi, tee yksi työssä tapahtuva valinta ja näe, miten valmennus, näyttö ja tilaajan raportointi liittyvät toisiinsa. Viidessä minuutissa tiedät enemmän kuin esittelykalvoista.','Choose your perspective, make a decision about real work, and explore how coaching, evidence and buyer reporting connect. Experience the concept in minutes, without a sales call.')}</p>
        <a class="be-jump" href="#kokeilu">{t('Aloita tuotekokeilu','Start the product experience')} <span aria-hidden="true">↘</span></a>
        <div class="be-intro-proof"><span>01 {t('Oikea työ','Real work')}</span><span>02 {t('Mukautuva tuki','Adaptive support')}</span><span>03 {t('Rajattu näyttö','Bounded evidence')}</span></div>
      </div>
      <div class="be-intro-visual" aria-hidden="true"><div class="be-device"><div class="be-device-toolbar"><span class="be-three-dots">● ● ●</span><span>prompted / experience</span><span>✳</span></div><div class="be-device-body"><small>CAPABILITY / WORKSPACE</small><strong>{t('Mikä työ voisi muuttua?','What could change in your work?')}</strong><div class="be-device-block">{t('01 / Tunnista tehtävä','01 / Define the task')}<span>↗</span></div><div class="be-device-block be-device-block-active">{t('02 / Kokeile uutta tapaa','02 / Try a new approach')}<span>↗</span></div><div class="be-device-block">{t('03 / Arvioi näyttöä','03 / Review evidence')}<span>↗</span></div></div></div><div class="be-float-note">{t('TYÖ → VALMENNUS → NÄYTTÖ','WORK → COACHING → EVIDENCE')}</div></div>
    </div></section>
    <section class="be-experience" id="kokeilu" aria-labelledby="be-experience-title"><div class="shell">
      <div class="be-experience-head"><div><p class="be-eyebrow">INTERACTIVE WALKTHROUGH / 01—05</p><h2 id="be-experience-title">{t('Kokeile Promptedia.','Explore Prompted.')}</h2><p>{t('Ei lomaketta. Ei asiakasdataa. Ei esityspakkoa.','No form. No customer data. No sales presentation.')}</p></div><div class="be-experience-time"><span>~ 05 MIN</span><small>{t('Voit vaihtaa polkua milloin tahansa.','Explore the steps in any order.')}</small></div></div>
      <div class="be-shell" data-buyer-experience data-locale="{lang}">
        <nav class="be-progress" aria-label="{t('Tuotekokeilun vaiheet','Product experience steps')}">{nav}</nav>
        <div class="be-workspace">
          <aside class="be-aside"><div class="be-aside-mark">PROMPTED<span>.</span></div><div class="be-aside-context"><small>WORK / SUPPORT / EVIDENCE</small><strong>{t('Yksi työkokemus. Useampi näkökulma.','One work experience. More than one perspective.')}</strong></div><div class="be-aside-status"><span class="be-status-dot" aria-hidden="true"></span>{t('Julkinen esimerkkitila','Public example environment')}</div><p class="be-aside-privacy">{t('Valintasi pysyvät tämän sivun muistissa. Emme lähetä niitä palvelimelle tai tallenna selaimeesi.','Your choices stay in this page’s temporary memory. They are not sent to a server or saved in your browser.')}</p></aside>
          <div class="be-surface">
            <div class="be-current"><span id="be-current-number">01 / 05</span><span id="be-current-name">{steps[0]}</span><button class="be-reset" type="button" data-reset>{t('Aloita alusta ↺','Start again ↺')}</button></div>
            <div class="be-alert" role="note">{escape(disclaimer)}</div><noscript><p class="be-nojs">{t('Tuotekokeilu tarvitsee JavaScriptin. Voit silti tutustua palveluihin ja lähettää yhteydenoton ilman sitä.','This walkthrough needs JavaScript. You can still explore the services and contact us without it.')}</p></noscript>
            <div id="be-screen" aria-live="polite" aria-atomic="false">
               <p class="be-kicker">{t('ALOITETAAN SINUSTA','START WITH YOUR VIEW')}</p><h3>{t('Mistä näkökulmasta tutustut?','Which perspective is yours?')}</h3><p class="be-screen-lead">{t('Sama teknologia näyttää erilaiselta oppijan ja ostajan näkökulmasta.','The same service looks different to a learner and a buyer.')}</p><div class="be-options be-options-roles">{roles}</div>
            </div>
            <div class="be-actions"><button class="be-back" type="button" data-back disabled>← {t('Edellinen','Previous')}</button><span id="be-step-label" class="be-step-label">01 / 05</span><button class="be-next" type="button" data-next>{t('Jatka','Continue')} <span aria-hidden="true">↗</span></button></div>
          </div>
        </div>
      </div>
      <p class="be-below">{t('Esittely on oma, turvallinen verkkosivun toiminnallisuus. Se ei avaa oikeaa Prompted-työtilaa eikä käsittele yksityisiä keskusteluja.','This is a safe on-site interactive walkthrough. It does not open a real Prompted workspace or process private conversations.')}</p>
    </div></section>
    <section class="be-buyers" aria-labelledby="be-buyers-title"><div class="shell"><div class="be-buyers-head"><p class="be-eyebrow">{t('OSTAJAN TIETOPAKETTI','BUYER DECISION GUIDE')} / 01—03</p><h2 id="be-buyers-title">{t('Mitä oikeastaan ostetaan?','What are you buying?')}</h2><p>{t('Kolme erilaista aloitusta. Sama periaate: kehittäminen sidotaan oikeaan työhön.','Three different ways to start. The same principle: development must connect to real work.')}</p></div><div class="be-buyers-grid">
       <article><span>01 / FOUNDATION</span><h3>Literacy</h3><p>{t('Roolikohtaisen tekoälylukutaidon yhteinen perusta, käytännön harjoittelu ja sovittujen toimien dokumentointi. Ei viranomaissertifikaatti tai lainmukaisuustakuu.','Role-specific AI literacy, practical exercises and documentation of agreed steps. Not an official certificate or compliance guarantee.')}</p><a href="/{lang}/literacy/">{t('Tutustu tarjontaan','Explore the offering')} ↗</a></article>
       <article class="be-buyer-featured"><span>02 / REAL WORK</span><h3>Capability</h3><p>{t('Alustava rajattu organisaatiopilotti: noin 20 osallistujaa, noin 90 päivän arviointijakso. Henkilökohtainen eteneminen ei ole sidottu määräpäivään. Laajuus ja ehdot sovitaan erikseen.','An indicative focused pilot: around 20 participants and an approximately 90-day organisational review period. Individual progress is not tied to a fixed deadline. Scope and terms are agreed separately.')}</p><a href="/{lang}/capability/">{t('Tutustu pilottiin','Explore the pilot')} ↗</a></article>
       <article><span>03 / AT SCALE</span><h3>Transformation</h3><p>{t('Organisaation tilanteeseen sovitettu muutoskokonaisuus, jossa yhdistyvät johdon tavoitteet, työtapojen kehitys ja todennettava näyttö.','A tailored organisational change engagement connecting leadership goals, new ways of working and reviewable evidence.')}</p><a href="/{lang}/transformation/">{t('Tutustu muutostyöhön','Explore transformation')} ↗</a></article>
     </div><p class="be-buyers-note">{t('Tietosuojan raja: julkinen esittely ei sisällä asiakastietoja. Oikea tilaajan raportointi tapahtuu erikseen hyväksytyllä ja käyttöoikeuksilla rajatulla raportilla.','Privacy boundary: this public experience contains no customer data. Real sponsor reporting requires a separately reviewed and access-controlled report.')}</p></div></section>
    <section class="be-after"><div class="shell be-after-grid"><div><p class="be-eyebrow">NEXT / A REAL CONVERSATION</p><h2>{t('Nyt voit kysyä parempia kysymyksiä.','Now you can ask better questions.')}</h2><p>{t('Jos tämä vastaa todelliseen tarpeeseen, voimme suunnitella rajatun aloituksen. Keskustelu alkaa työstä, ei ohjelmistoesittelystä.','If this addresses a real need, we can design a focused starting point. The discussion starts with work, not a slide deck.')}</p></div><div class="be-after-links"><a class="be-after-main" href="/{lang}/{'yhteys' if fi else 'contact'}/">{t('Keskustellaan toteutuksesta','Discuss an implementation')} ↗</a><a href="/{lang}/capability/">{t('Tutustu Capability-pilottiin','Explore the Capability pilot')} ↗</a><a href="/{lang}/literacy/">{t('Tutustu Literacyyn','Explore Literacy')} ↗</a><a href="/{lang}/transformation/">{t('Tutustu Transformationiin','Explore Transformation')} ↗</a></div></div></section>'''
