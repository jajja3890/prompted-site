from pathlib import Path
import html, json, shutil, os
PRODUCTION = os.environ.get("PROMPTED_RELEASE") == "approved-production"
if PRODUCTION and os.environ.get("PROMPTED_APPROVAL") != "reviewed-privacy-content-and-domain":
    raise SystemExit("Production build blocked. Set explicit approval variable after review.")
if PRODUCTION and os.environ.get("PROMPTED_RC7_IMAGES_APPROVED") != "both-image-studies-explicitly-approved":
    raise SystemExit("RC7 production blocked: H01/H05 art studies require explicit visual approval or replacement.")

ROOT=Path(__file__).resolve().parent
ASSET='/assets/'

C={
'fi':{
 'navigation':[('Ratkaisut','#ratkaisut'),('Miten toimimme','#menetelma'),('Yritys','yritys/')],
 'contact':'Keskustellaan','language':'FI','langother':'EN','site_desc':'Prompted auttaa organisaatioita kehittämään tekoälyavusteisia työtapoja oikeassa työssä ja arvioimaan muutosta.',
 'eyebrow':'HUMAN CAPABILITY / REAL WORK','lead_top':'Teknologia on täällä.','lead_bottom':'Muutos syntyy ihmisissä.','tagline':'Autamme yrityksiä tekemään tekoälystä osan omaa tapaa tehdä työtä. Ei vain oppimaan työkaluja, vaan muuttamaan työtä ja tekemään muutoksen näkyväksi.',
 'cta_primary':'Tutustu Capability-pilottiin','cta_secondary':'Keskustellaan tilanteestanne','scroll':'Tutustu ajatteluumme','fig':'Ihminen. Työ. Muutos.',
 'problem_kicker':'01 / LÄHTÖKOHTA','problem_title':'Pääsy tekoälyyn ei ole sama asia kuin kyky käyttää sitä hyvin.','problem_body':'Ohjelmistot, koulutukset ja kokeilut ovat vasta alku. Todellinen arvo syntyy, kun uusi työtapa toistuu, siirtyy uusiin tilanteisiin ja säilyy myös ilman jatkuvaa ohjausta.','problem_note':'Yritykset kasvavat, kun ihmiset kasvavat.',
 'solutions_kicker':'02 / TARJOOMA','solutions_title':'Yksi päämäärä. Kolme tapaa aloittaa.','solutions_intro':'Rakennamme kyvykkyyttä askel kerrallaan. Ratkaisu valitaan organisaation tilanteen mukaan, ei koulutuspäivien määrän perusteella.',
 'products':[
  ('01','LITERACY','Yhteinen perusta','Tekoälylukutaito oman työn ja organisaation vastuiden näkökulmasta. EU AI Act -valmiutta tukevat, dokumentoitavat toimet.','Kysy toteutuksesta'),
  ('02','CAPABILITY','Uusi tapa tehdä työtä','Rajattu organisaatiopilotti, jossa ihmiset kehittävät työtapojaan omissa tehtävissään digitaalisen valmennuspalvelun ja ihmisen tuella.','Tutustu pilottiin'),
  ('03','TRANSFORMATION','Muutos osaksi organisaatiota','Johdon, ihmisten ja kehittämisen yhdistäminen niin, ettei edistyminen jää yksittäisten innostuneiden varaan. Toteutus suunnitellaan tarpeen mukaan.','Keskustellaan tarpeesta')],
 'method_kicker':'03 / MENETELMÄ','method_title':'Muutos rakennetaan oikeassa työssä.','method_intro':'Sama logiikka ohjaa kaikkea tekemistämme: lähtötilanne, toistuva tekeminen, havaittava muutos.',
 'steps': [('Tunnista','Mistä työstä lähdemme ja mikä siinä pitäisi muuttua?'),('Harjoittele työssä','Ihminen kokeilee, toistaa ja soveltaa uutta tapaa omissa tehtävissään.'),('Todenna','Tarkastelemme näyttöä muutoksesta, sen rajoista ja seuraavista askeleista.')],
 'quote':'Tavoitteena ei ole, että ihminen tarvitsee tekoälyvalmentajaa ikuisesti. Tavoitteena on, että hän pärjää lopulta paremmin itse.',
 'evidence_kicker':'04 / EVIDENCE','evidence_title':'Muutosta ei pidä vain luvata. Sitä pitää pystyä arvioimaan.','evidence_body':'Prompted Data tuo tilaajalle hallinnoidun yhteenvetotason näkymän kehittymisestä. Yksittäisen osallistujan työ ja yksityiset valmennuskeskustelut eivät kuulu työnantajan raporttiin.','evidence_note':'Ei keksittyjä ROI-lukuja. Ei yksilötason seurantaa. Näyttö ennen väitettä.',
 'close_kicker':'SEURAAVA ASKEL','close_title':'Aloitetaan yhdestä oikeasta ongelmasta.','close_body':'Kerro, missä tekoälyn hyödyntäminen ei vielä näy työn arjessa. Katsomme yhdessä, mistä kannattaa aloittaa.',
 'footer_links':'Sivut','legal':'Tietosuoja','company':'Yritys','capability':'Capability','contact_title':'Yhteys','footnote':'Companies grow when people grow.',
 'cap_eyebrow':'PROMPTED / CAPABILITY','cap_title':'Osaaminen muuttuu arvoksi vasta, kun työ muuttuu.','cap_lead':'Prompted Capability on organisaatiolle rajattu, maksullinen pilotti, jossa rakennetaan uusia tekoälyavusteisia työtapoja oikeassa työssä ja arvioidaan muutosta.',
 'cap_scope_title':'Pilotti, joka on tarpeeksi rajattu aloitettavaksi.','cap_scope_body':'Alustava organisaation arviointijakso on noin 90 päivää ja tyypillinen osallistujamäärä noin 20. Tarkka sisältö, aikataulu ja hinta sovitaan tarjouksessa. 90 päivää ei ole osallistujan pakollinen valmistumisaika.',
 'cap_stages':[('01 / LÄHTÖTASO','Tunnistamme, miten työ nyt sujuu ja mihin muutosta tarvitaan.'),('02 / TYÖSSÄ OPPIMINEN','Osallistujat harjoittelevat omissa tehtävissään digitaalisen valmennuspalvelun tukemina.'),('03 / ARVIOINTI','Kokoamme perustellun kuvan toistosta, siirrettävyydestä ja itsenäistymisestä.')],
 'cap_difference_title':'Teknologia ja ihminen tekevät eri työtä.','cap_difference_body':'Digitaalinen valmennuspalvelu tukee osallistujaa arjen tehtävissä. Promptedin vastuuhenkilö tukee organisaatiota ja pitää huolen siitä, että kokeilu liittyy liiketoiminnan tavoitteisiin.',
 'cap_privacy_title':'Havainto ei ole työntekijän valvontaa.','cap_privacy_body':'Tilaaja saa hallinnoitua yhteenvetotietoa, ei yksittäisen osallistujan raakatekstiä tai yksityisiä keskusteluja. Raportoinnin suojarajat ja julkaisuvaatimukset sovitaan ennen pilottia.',
 'cap_disclaimer':'Pilotti ei takaa tiettyä taloudellista tuottoa, yksilösertifikaattia tai välitöntä muutosta koko organisaatiossa.',
 'cap_cta':'Keskustellaan sopivuudesta','company_eyebrow':'PROMPTED / YRITYS','company_title':'Companies grow when people grow.','company_lead':'Prompted Oy on turkulainen yritys, joka auttaa organisaatioita muuttamaan tekoälyn mahdollisuudet ihmisten todelliseksi työkyvykkyydeksi.',
 'company_body':'Meidän lähtökohtamme on inhimillinen: ihmiset tarvitsevat aikaa, kontekstia, kannustusta ja käytännön näyttöä. Teknologia tuo mahdollisuudet. Ihmiset muuttavat työn.',
 'contact_eyebrow':'PROMPTED / YHTEYS','contact_page_title':'Mistä teillä pitäisi aloittaa?','contact_page_body':'Ensimmäiseen keskusteluun ei tarvita valmista projektisuunnitelmaa. Riittää, että tiedätte, mikä nykyisessä työssä ei vielä muutu.','email_label':'Kirjoita suoraan','email_subject':'Keskustelu Promptedin kanssa','contact_steps':[('01','Kuvaile tilanne'),('02','Valitaan sopiva lähtöpiste'),('03','Sovitaan seuraava askel')],
 'terms_title':'Palveluehdot','terms_body':'Verkkosivustolla esitellään Promptedin B2B-palveluja. Tästä sivustosta ei synny tilausta tai sopimusta. Mahdollisen asiakastoimituksen palvelukuvaus, hinta, vastuut ja muut ehdot vahvistetaan kirjallisessa tarjouksessa ja sopimuksessa. Lisätietoja: jarkko@prompted.fi.','privacy_title':'Tietosuoja verkkosivulla','privacy_intro':'Prompted Oy käsittelee yhteydenottoja ja verkkosivun tekniseen toimintaan liittyviä tietoja vain asianmukaisiin tarkoituksiin.',
 'privacy_sections':[('Rekisterinpitäjä','Prompted Oy, Y-tunnus 3550114-7, Turku, Suomi. Yhteydenotot: jarkko@prompted.fi.'),('Yhteydenotot','Kun otat yhteyttä sähköpostitse, käsittelemme viestisi tietoja vastataksemme ja hoitaaksemme mahdollista asiakassuhdetta. Säilytysaika määräytyy asian käsittelyn ja lakisääteisten tarpeiden mukaan.'),('Tekniset tiedot','Sivusto toimitetaan Vercelin infrastruktuurista. Palveluntarjoaja voi käsitellä palvelun saatavuuden ja tietoturvan kannalta tarpeellisia teknisiä tietoja, kuten IP-osoitteita ja pyyntölokeja.'),('Evästeet ja mittaus','Tässä sivustoversiossa ei ole erillistä markkinointiseurantaa, analytiikkaskriptejä eikä yhteydenottolomaketta.'),('Oikeutesi','Voit pyytää pääsyä henkilötietoihisi, niiden oikaisua tai poistamista soveltuvan lain mukaisesti. Ota yhteyttä rekisterinpitäjään. Voit myös tehdä valituksen tietosuojavaltuutetulle.')]
},
'en':{
 'navigation':[('Solutions','#solutions'),('How it works','#method'),('Company','company/')],
 'contact':'Let’s talk','language':'EN','langother':'FI','site_desc':'Prompted helps organisations build AI-assisted ways of working in real work and understand what changes.',
 'eyebrow':'HUMAN CAPABILITY / REAL WORK','lead_top':'Technology is here.','lead_bottom':'Change is human.','tagline':'We help organisations make AI part of how people actually work. Not just learn a tool, but change work and make progress visible.',
 'cta_primary':'Explore Capability','cta_secondary':'Discuss your challenge','scroll':'Explore the approach','fig':'People. Work. Change.',
 'problem_kicker':'01 / THE CHALLENGE','problem_title':'Access to AI is not the same as the ability to use it well.','problem_body':'Software, training and experiments are only the beginning. Real value emerges when a new practice is repeated, transferred to other tasks and sustained with less support.','problem_note':'Companies grow when people grow.',
 'solutions_kicker':'02 / WHAT WE OFFER','solutions_title':'One ambition. Three ways to begin.','solutions_intro':'We build capability one step at a time. The right starting point depends on the organisation, not the number of training days.',
 'products':[
  ('01','LITERACY','A shared foundation','AI literacy in the context of real work and organisational responsibility. Documentable measures that support EU AI Act readiness.','Ask about delivery'),
  ('02','CAPABILITY','A new way of working','A defined organisational pilot in which people develop practices in their real work, supported by a digital coaching service and a human partner.','Explore the pilot'),
  ('03','TRANSFORMATION','Change that takes hold','Connecting leadership, people and development so progress does not rely on a handful of enthusiasts. Delivery is tailored to the context.','Discuss your needs')],
 'method_kicker':'03 / OUR APPROACH','method_title':'Change is built in real work.','method_intro':'A clear sequence underpins everything we do: baseline, repeated practice, observable change.',
 'steps': [('Understand','Which part of work needs to change, and why?'),('Practise at work','People try, repeat and apply new practices in their actual tasks.'),('Evaluate','We examine evidence of change, its limits and the next steps.')],
 'quote':'The goal is not for someone to need a digital coach forever. The goal is for them to become more capable on their own.',
 'evidence_kicker':'04 / EVIDENCE','evidence_title':'Change should not just be promised. It should be assessed.','evidence_body':'Prompted Data offers organisations a governed, aggregate view of progress. Individual work content and private coaching conversations do not appear in the employer’s report.','evidence_note':'No invented ROI. No individual surveillance. Evidence before claims.',
 'close_kicker':'THE NEXT STEP','close_title':'Start with one real problem.','close_body':'Tell us where AI adoption is not yet changing day-to-day work. Together we can identify a useful first step.',
 'footer_links':'Explore','legal':'Privacy','company':'Company','capability':'Capability','contact_title':'Contact','footnote':'Companies grow when people grow.',
 'cap_eyebrow':'PROMPTED / CAPABILITY','cap_title':'Capability creates value when work changes.','cap_lead':'Prompted Capability is a defined, paid organisational pilot to establish AI-assisted practices in real work and evaluate what changes.',
 'cap_scope_title':'A pilot that is focused enough to start.','cap_scope_body':'The tentative organisational evaluation window is around 90 days, with a typical cohort of around 20 participants. Precise scope, timing and price are agreed in the proposal. Ninety days is not a mandatory completion deadline for each learner.',
 'cap_stages':[('01 / BASELINE','Identify current practices and where change is needed.'),('02 / PRACTICE','Participants build new ways of working in their own tasks, with digital coaching support.'),('03 / EVALUATION','Build an evidence-based understanding of repetition, transfer and independence.')],
 'cap_difference_title':'Technology and people have different roles.','cap_difference_body':'The digital coaching service supports participants in everyday tasks. A named Prompted contact supports the organisation and ensures the pilot remains tied to its priorities.',
 'cap_privacy_title':'Evidence is not employee surveillance.','cap_privacy_body':'Sponsors receive governed, aggregate reporting, not raw individual work or private conversations. Reporting boundaries and release conditions are agreed before the pilot.',
 'cap_disclaimer':'The pilot does not guarantee financial returns, individual credentials or immediate organisation-wide change.',
 'cap_cta':'Discuss pilot fit','company_eyebrow':'PROMPTED / COMPANY','company_title':'Companies grow when people grow.','company_lead':'Prompted Oy is based in Turku, Finland. We help organisations turn the possibilities of AI into real capability in the way people work.',
 'company_body':'Our starting point is human: people need context, encouragement, practice and evidence. Technology creates opportunities. People change the work.',
 'contact_eyebrow':'PROMPTED / CONTACT','contact_page_title':'Where should your organisation begin?','contact_page_body':'You do not need a finished project brief to have a first conversation. Just tell us what is not changing in the way work gets done.','email_label':'Email us directly','email_subject':'A conversation with Prompted','contact_steps':[('01','Describe the challenge'),('02','Choose a useful starting point'),('03','Agree on next steps')],
 'terms_title':'Service terms','terms_body':'This website introduces Prompted’s B2B services. No order or contract is made through the website. Any customer delivery scope, price, responsibilities and other terms are agreed in a written proposal and contract. Questions: jarkko@prompted.fi.','privacy_title':'Website privacy','privacy_intro':'Prompted Oy processes contact enquiries and technical website information for appropriate, limited purposes.',
 'privacy_sections':[('Controller','Prompted Oy, business ID 3550114-7, Turku, Finland. Contact: jarkko@prompted.fi.'),('Email enquiries','When you email us, we process your message to respond and manage any resulting business relationship. Retention depends on the handling of the enquiry and applicable legal duties.'),('Technical data','The site is hosted on Vercel infrastructure. The service provider may process technical data needed for security and availability, such as IP addresses and request logs.'),('Cookies and analytics','This website version contains no separate marketing trackers, analytics scripts or contact form.'),('Your rights','You may request access, correction or erasure of your personal data where the law applies. Contact the controller. You may also lodge a complaint with the Finnish Data Protection Ombudsman.')]
}}


# Public products are strictly Literacy, Capability and Transformation.
# Marketing content is deliberately specific, but does not promise compliance certificates,
# ROI, unverified client outcomes or a standard Transformation package.
SERVICES = {
 'fi': {
  'literacy': {
   'eyebrow':'PROMPTED / LITERACY · TEKOÄLYLUKUTAITO',
   'h1':'Tekoälylukutaito organisaatioille, jotka haluavat edetä vastuullisesti.',
   'intro':'Prompted Literacy auttaa yrityksiä luomaan yhteisen, työhön liittyvän perustan tekoälyn käyttöön ja dokumentoimaan osaamisen kehittämiseksi tehtyjä toimia.',
   'meta':'Tekoälylukutaidon kehittäminen yrityksille: työhön liittyvät käyttötavat, vastuut ja dokumentoitava eteneminen. EU AI Act -lukutaitovalmiuden tueksi.',
   'why_title':'Pelkkä yleiskurssi ei kerro, mitä ihmiset osaavat tehdä omassa työssään.',
   'why':'Lähtötilanteet vaihtelevat. Eri roolit, työkalut, riskit ja työn todelliset tehtävät vaikuttavat siihen, mitä organisaatiossa on syytä oppia ja dokumentoida.',
   'steps':[('01 / TILANNE','Tunnistamme käytössä olevat tekoälytyökalut, roolit ja tärkeimmät oppimistarpeet.'),('02 / YHTEINEN PERUSTA','Harjoittelemme vastuullista käyttöä oman työn esimerkeissä, huomioiden arvioinnin ja harkinnan.'),('03 / DOKUMENTOINTI','Kokoamme sovitut toimet ja jatkokehittämisen tarpeet organisaation omaa käyttöä varten.')],
   'bound_title':'Lukutaito ei ole sertifikaattilupaus.',
   'bound':'EU:n tekoälysääntelyn lukutaitovelvoitteeseen ei liity yhtä yleistä virallista kurssia tai Promptedin myöntämää viranomaissertifikaattia. Organisaation pitää arvioida tarpeelliset toimet oman toimintansa ja riskien näkökulmasta. Toteutuksen laajuus sovitaan ennen aloitusta.',
   'who_title':'Kenelle tämä sopii?',
   'who':'HR- ja henkilöstöjohdolle, esihenkilöille sekä liiketoimintavastuullisille, jotka tarvitsevat selkeän aloituksen henkilöstön tekoälylukutaidon kehittämiseen.',
   'faq':[('Korvaako Prompted Literacy lainmukaisuuden arvioinnin?','Ei. Tuemme henkilöstön tekoälylukutaidon kehittämistä ja toimien dokumentointia, mutta emme anna oikeudellista vaatimustenmukaisuustakuuta.'),('Onko tämä sama kuin Capability?','Ei. Literacy luo yhteistä lähtötasoa ja vastuullisen käytön perustaa. Capability vie kehittämisen pidemmälle oikeisiin työtehtäviin ja muutoksen arviointiin.')],
   'cta':'Keskustellaan tekoälylukutaidon tarpeesta'
  },
  'transform': {
   'eyebrow':'PROMPTED / TRANSFORMATION · ORGANISAATIOMUUTOS',
   'h1':'Tekoälymuutos, joka näkyy organisaation tavassa tehdä työtä.',
   'intro':'Prompted Transformation yhdistää johdon tavoitteet, työntekijöiden uudenlaisen tekemisen ja muutoksen arvioinnin. Kokonaisuus suunnitellaan organisaation tilanteen mukaan.',
   'meta':'Organisaation tekoälymuutos: yhdistämme liiketoiminnan tavoitteet, henkilöstön kyvykkyyden kehittämisen ja todellisten työtapojen muutoksen arvioinnin.',
   'why_title':'Työkaluista hyötyihin tarvitaan muutos työn arjessa.',
   'why':'Käyttöönotto ei riitä, jos toimivat käytännöt eivät toistu, siirry tiimien välillä ja säily ilman jatkuvaa ulkoista tukea. Muutosta pitää johtaa työstä käsin.',
   'steps':[('01 / TAVOITE','Määritämme yhdessä, mitä liiketoiminnassa ja arjen työssä halutaan muuttaa.'),('02 / KYVYKKYYS','Yhdistämme sopivat oppimis- ja valmennustoimet todellisiin tehtäviin.'),('03 / NÄYTTÖ','Tarkastelemme toistoa, siirrettävyyttä ja itsenäistymistä sekä päätämme seuraavista toimista.')],
   'bound_title':'Ei valmista muutospakettia jokaiselle yritykselle.',
   'bound':'Transformation on tarvelähtöinen yhteistyömalli, ei etukäteen vakioitu ohjelma tai luvattu liiketoimintahyöty. Lopullinen laajuus, vastuut, mittarit ja ehdot määritellään asiakaskohtaisesti.',
   'who_title':'Kenelle tämä sopii?',
   'who':'Liiketoimintajohdolle, muutosvastuullisille sekä People- ja L&D-johdolle, kun tavoitteena on yksittäistä koulutusta laajempi toimintatapojen uudistuminen.',
   'faq':[('Miten tämä eroaa yksittäisestä koulutuksesta?','Työ alkaa liiketoiminnan muutostarpeesta. Harjoittelu, tuki ja arviointi liittyvät työn todellisiin tehtäviin, eivät vain koulutukseen osallistumiseen.'),('Onko Transformationilla kiinteä kesto tai hinta?','Ei tässä vaiheessa. Tarve, rajaus ja toteutusmalli määritellään yhdessä ja vahvistetaan tarjouksessa.')],
   'cta':'Keskustellaan organisaation muutoksesta'
  }
 },
 'en': {
  'literacy': {
   'eyebrow':'PROMPTED / LITERACY · AI LITERACY',
   'h1':'AI literacy for organisations that want to move forward responsibly.',
   'intro':'Prompted Literacy helps companies establish a shared, work-relevant foundation for using AI and document their capability-building measures.',
   'meta':'AI literacy for organisations: practical workplace use, responsible judgement and documented learning measures supporting EU AI Act readiness.',
   'why_title':'A generic course does not show how people use AI in their own work.',
   'why':'Different roles, tools, risks and everyday tasks call for different learning priorities. A credible programme starts from that context, not a one-size-fits-all certificate.',
   'steps':[('01 / CONTEXT','Identify the AI tools, roles and learning needs relevant to the organisation.'),('02 / FOUNDATION','Practise responsible use through real workplace examples, including human judgement and evaluation.'),('03 / DOCUMENTATION','Document agreed measures and the areas that need further development.')],
   'bound_title':'AI literacy is not a compliance certificate.',
   'bound':'The EU AI Act literacy obligation does not prescribe one universal official training programme or an authority-issued Prompted certificate. Organisations must assess suitable measures for their own context and risks. Scope is agreed before delivery.',
   'who_title':'Who is this for?',
   'who':'HR, People and L&D leaders, managers and business owners who need a practical starting point for strengthening workforce AI literacy.',
   'faq':[('Does Prompted Literacy guarantee legal compliance?','No. We support AI literacy measures and documentation, but do not provide a legal-compliance guarantee.'),('How does Literacy differ from Capability?','Literacy provides a common foundation for responsible AI use. Capability goes further by developing real work practices and evaluating the changes.')],
   'cta':'Discuss your AI literacy needs'
  },
  'transform': {
   'eyebrow':'PROMPTED / TRANSFORMATION · ORGANISATIONAL CHANGE',
   'h1':'AI transformation that changes how your organisation works.',
   'intro':'Prompted Transformation connects leadership goals, practical capability development and evaluation of changing work. The engagement is designed around the organisation’s context.',
   'meta':'Organisational AI transformation: connect business priorities, people development and evidence of lasting changes in real work.',
   'why_title':'New tools only create value when work changes.',
   'why':'Adoption alone is insufficient if good practices are not repeated, transferred between teams and sustained without constant external support. Change needs to be led from real work.',
   'steps':[('01 / PURPOSE','Agree what needs to change in business outcomes and day-to-day work.'),('02 / CAPABILITY','Connect learning and coaching to meaningful real-world tasks.'),('03 / EVIDENCE','Examine repeatability, transfer and independence, then decide on the next steps.')],
   'bound_title':'Not a one-size-fits-all transformation package.',
   'bound':'Transformation is a tailored collaboration model, not a standardised programme or guaranteed business result. Scope, ownership, measures and terms are agreed with each customer.',
   'who_title':'Who is this for?',
   'who':'Business, transformation, People and L&D leaders seeking broader changes in ways of working than a stand-alone training programme can deliver.',
   'faq':[('How is this different from training?','The starting point is a business need. Development, support and evaluation take place in the context of actual workplace tasks.'),('Does Transformation have a fixed timeline or price?','Not at present. Scope and delivery are planned together and confirmed in a written proposal.')],
   'cta':'Discuss organisational transformation'
  }
 }
}

SEO_TITLES = {
 'fi': {'home':'Tekoälykyvykkyyden kehittäminen yrityksille | Prompted', 'literacy':'Tekoälylukutaito yrityksille | Prompted Literacy', 'cap':'Tekoälykyvykkyyden kehittäminen | Prompted Capability', 'transform':'Tekoälymuutos organisaatioille | Prompted Transformation', 'company':'Prompted Oy | Tekoälykyvykkyys ja työssä oppiminen', 'contact':'Ota yhteyttä | Prompted Oy', 'privacy':'Tietosuoja | Prompted Oy', 'terms':'Palveluehdot | Prompted Oy'},
 'en': {'home':'AI capability development for organisations | Prompted', 'literacy':'AI literacy for organisations | Prompted Literacy', 'cap':'Develop AI capability at work | Prompted Capability', 'transform':'Prompted Transformation | Organisational AI transformation', 'company':'About Prompted Oy | AI capability at work', 'contact':'Contact Prompted Oy', 'privacy':'Privacy | Prompted Oy', 'terms':'Service terms | Prompted Oy'}
}
LAST_MEANINGFUL_UPDATE = '2026-10-21'  # Update when material copy, links or structured data change.

def structured_data(lang, page, title, description, current):
    origin='https://prompted.fi'
    org_id=origin+'/#organization'
    org={'@type':'Organization','@id':org_id, 'name':'Prompted Oy', 'legalName':'Prompted Oy',
         'url':origin+'/', 'logo':{'@type':'ImageObject', 'url':origin+'/assets/apple-touch-icon.png', 'width':180, 'height':180},
         'taxID':'3550114-7', 'email':'jarkko@prompted.fi', 'founder':{'@type':'Person','name':'Jarkko Sjöman','url':'https://jarkkosjoman.com/'},
         'address':{'@type':'PostalAddress', 'addressLocality':'Turku', 'addressCountry':'FI'},
         'description':C[lang]['site_desc']}
    site={'@type':'WebSite','@id':origin+'/#website','name':'Prompted','url':origin+'/','publisher':{'@id':org_id},'inLanguage':['fi','en']}
    webpage={'@type':'WebPage','@id':origin+current+'#webpage','url':origin+current,
             'name':title,'description':description,'inLanguage':lang,'isPartOf':{'@id':site['@id']},
             'about':{'@id':org_id}}
    graph=[org,site,webpage]
    if page in ('literacy','cap','transform'):
        service_name={'literacy':'Prompted Literacy','cap':'Prompted Capability','transform':'Prompted Transformation'}[page]
        service_description=SERVICES[lang][page]['intro'] if page!='cap' else C[lang]['cap_lead']
        graph.append({'@type':'Service','@id':origin+current+'#service','name':service_name,
                      'serviceType':service_name,'description':service_description,
                      'provider':{'@id':org_id},'url':origin+current,
                      'audience':{'@type':'BusinessAudience','audienceType':'Organisations'}})
    if page!='home':
        graph.append({'@type':'BreadcrumbList','@id':origin+current+'#breadcrumb','itemListElement':[
            {'@type':'ListItem','position':1,'name':'Prompted','item':origin+urls(lang)['home']},
            {'@type':'ListItem','position':2,'name':title,'item':origin+current}]})
    return json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False,separators=(',',':')).replace('<','\u003c')

def e(s):return html.escape(str(s),quote=True)
def relroot(path):return '/'+path.strip('/')+'/' if path else '/'
def urls(lang):return {'home':f'/{lang}/','literacy':f'/{lang}/literacy/','cap':f'/{lang}/capability/','transform':f'/{lang}/transformation/','company':f'/{lang}/'+('yritys/' if lang=='fi' else 'company/'),'contact':f'/{lang}/'+('yhteys/' if lang=='fi' else 'contact/'),'privacy':f'/{lang}/'+('tietosuoja/' if lang=='fi' else 'privacy/'),'terms':f'/{lang}/'+('ehdot/' if lang=='fi' else 'terms/')}
def link_to(path):return path

def shell(lang,page,title,description,body):
 c=C[lang]; u=urls(lang); oth='en' if lang=='fi' else 'fi'; v=urls(oth); current=u[page];
 nav=[('Literacy',u['literacy']),('Capability',u['cap']),('Transformation',u['transform']),(c['navigation'][1][0],u['home']+'#'+('menetelma' if lang=='fi' else 'method')),(c['navigation'][2][0],u['company'])]
 navhtml=''.join(f'<a href="{e(href)}"{" aria-current=\"page\"" if href==current else ""}>{e(label)}</a>' for label,href in nav)
 canonical='https://prompted.fi'+current
 robots_meta = 'index,follow,max-image-preview:large' if PRODUCTION else 'noindex,nofollow'
 htmltitle=e(SEO_TITLES[lang][page]); jsonld=structured_data(lang,page,SEO_TITLES[lang][page],description,current)
 return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{htmltitle}</title><meta name="description" content="{e(description)}">
<meta name="theme-color" content="#000000"><meta name="robots" content="{robots_meta}" data-release-gate="{'production' if PRODUCTION else 'prelaunch'}">
<link rel="canonical" href="{canonical}"><link rel="alternate" hreflang="fi" href="https://prompted.fi{urls('fi')[page]}"><link rel="alternate" hreflang="en" href="https://prompted.fi{urls('en')[page]}">{'<link rel="alternate" hreflang="x-default" href="https://prompted.fi/en/">' if page=='home' else ''}
<link rel="icon" href="/assets/favicon.ico" sizes="any"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preload" href="/assets/wordmark-dark.svg" as="image" type="image/svg+xml">
<link rel="stylesheet" href="/assets/style.css"><link rel="stylesheet" href="/assets/rc7.css"><script src="/assets/site.js" defer></script>
<meta property="og:type" content="website"><meta property="og:site_name" content="Prompted"><meta property="og:locale" content="{'fi_FI' if lang=='fi' else 'en_GB'}"><meta name="twitter:card" content="summary_large_image"><meta property="og:title" content="{htmltitle}"><meta property="og:description" content="{e(description)}"><meta property="og:url" content="{canonical}">
<script type="application/ld+json">{jsonld}</script>
</head><body>
<a class="skip" href="#main">{'Siirry sisältöön' if lang=='fi' else 'Skip to content'}</a>
<header class="site-header"><div class="header-inner"><a class="wordmark" href="{u['home']}" aria-label="Prompted"><img width="190" height="22" src="/assets/wordmark-dark.svg" alt="Prompted"></a>
<nav class="nav-desktop" aria-label="{'Päävalikko' if lang=='fi' else 'Main navigation'}">{navhtml}</nav>
<div class="header-right"><div class="lang" aria-label="Language"><a href="{u[page]}" lang="{lang}" aria-current="page">{lang.upper()}</a><span>/</span><a href="{v[page]}" lang="{oth}">{oth.upper()}</a></div><a class="contact-pill" href="{u['contact']}">{e(c['contact'])}<span aria-hidden="true">↗</span></a></div>
<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="mobile-menu"><span class="open-label">{'Valikko' if lang=='fi' else 'Menu'}</span><span class="menu-bars" aria-hidden="true">☰</span></button></div>
<nav id="mobile-menu" class="nav-mobile" hidden aria-label="Mobile navigation">{navhtml}<a href="{u['contact']}">{e(c['contact'])} ↗</a><div class="mobile-lang"><a href="{u[page]}" lang="{lang}" aria-current="page">{lang.upper()}</a><a href="{v[page]}" lang="{oth}">{oth.upper()}</a></div></nav></header>
<main id="main">{body}</main>
<footer class="site-footer"><div class="footer-top"><div><img loading="lazy" src="/assets/wordmark-dark.svg" class="footer-logo" width="270" height="32" alt="Prompted"><p>{e(c['footnote'])}</p></div><div class="footer-links"><span class="mini-label">{e(c['footer_links'])}</span><a href="{u['home']}">{'Etusivu' if lang=='fi' else 'Home'}</a><a href="{u['literacy']}">Literacy</a><a href="{u['cap']}">Capability</a><a href="{u['transform']}">Transformation</a><a href="{u['company']}">{e(c['company'])}</a><a href="{u['privacy']}">{e(c['legal'])}</a><a href="{u['terms']}">{'Palveluehdot' if lang=='fi' else 'Service terms'}</a></div><div class="footer-links"><span class="mini-label">{e(c['contact_title'])}</span><a href="mailto:jarkko@prompted.fi">jarkko@prompted.fi ↗</a><span>Prompted Oy</span><span>{'Turku, Suomi' if lang=='fi' else 'Turku, Finland'}</span><span>{'Y-tunnus' if lang=='fi' else 'Business ID'} 3550114-7</span></div></div><div class="footer-bottom"><span>© 2026 Prompted Oy</span><span>HUMAN CAPABILITY / REAL WORK</span><a href="#main">{'Takaisin ylös' if lang=='fi' else 'Back to top'} ↑</a></div></footer>
</body></html>'''

def card(number,name,title,copy,cta,url):
 return f'<article class="product"><div class="product-top"><span>{e(number)} / {e(name)}</span><span class="product-arrow" aria-hidden="true">↗</span></div><div><h3>{e(title)}</h3><p>{e(copy)}</p></div><a class="textlink" href="{e(url)}">{e(cta)} <span aria-hidden="true">↗</span></a></article>'

def main_home(lang):
 c=C[lang];u=urls(lang); anchor_sol='ratkaisut' if lang=='fi' else 'solutions';anchor_method='menetelma' if lang=='fi' else 'method'
 cards=''.join(card(*product,url=(u['literacy'] if i==0 else u['cap'] if i==1 else u['transform'])) for i,product in enumerate(c['products']))
 steps=''.join(f'<li><span class="step-index">0{i+1}</span><h3>{e(title)}</h3><p>{e(text)}</p></li>' for i,(title,text) in enumerate(c['steps']))
 return f'''
<section class="intro-dark rc7-intro">
<div class="rc7-hero-grid">
  <div class="rc7-hero-copy">
    <div class="rc7-overline"><span>{e(c['eyebrow'])}</span><span>EST. 2025 / TURKU, FINLAND</span></div>
    <h1>{e(c['lead_top'])}<br><em>{e(c['lead_bottom'])}</em></h1>
    <p class="rc7-lead">{e(c['tagline'])}</p>
    <div class="rc7-actions"><a class="button primary" href="{u['cap']}">{e(c['cta_primary'])} <span aria-hidden="true">↗</span></a><a class="button secondary" href="{u['contact']}">{e(c['cta_secondary'])} <span aria-hidden="true">↗</span></a></div>
    <div class="rc7-hero-footer"><span>PEOPLE</span><span>WORK</span><span>EVIDENCE</span></div>
  </div>
  <figure class="rc7-hero-art"><img src="/assets/hero-daylight.webp" alt="{'Arkkitehtoninen kuva: suuri betonitila luonnonvalossa, yksi ihminen mittakaavana' if lang=='fi' else 'Architectural study: monumental daylight concrete space with one small person'}" width="1672" height="941" fetchpriority="high"><figcaption><span>H01 / DAYLIGHT</span><span>{'KUVATUTKIELMA · EI HYVÄKSYTTY' if lang=='fi' else 'IMAGE STUDY · NOT APPROVED'}</span></figcaption></figure>
</div>
<div class="rc7-method-index" aria-label="{'Työssä tapahtuvan muutoksen kolme vaihetta' if lang=='fi' else 'Three steps of capability change in work'}">
  <span>001 / 003</span><strong>{'Tunnista työ' if lang=='fi' else 'Understand the work'}</strong><strong>{'Kehitä käytäntöä' if lang=='fi' else 'Develop the practice'}</strong><strong>{'Osoita muutos' if lang=='fi' else 'Show the change'}</strong>
</div>
</section>
<section class="section section-light reveal"><div class="section-meta"><span>{e(c['problem_kicker'])}</span><span>THE HUMAN FACTOR</span></div><div class="lead-layout"><h2>{e(c['problem_title'])}</h2><div class="lead-text"><p>{e(c['problem_body'])}</p><div class="olive-line"></div><span>{e(c['problem_note'])}</span></div></div></section>
<section id="{anchor_sol}" class="section section-white reveal"><div class="section-meta"><span>{e(c['solutions_kicker'])}</span><span>01—03</span></div><div class="section-top"><h2>{e(c['solutions_title'])}</h2><p>{e(c['solutions_intro'])}</p></div><div class="products-grid">{cards}</div></section>
<section id="{anchor_method}" class="section section-dark reveal"><div class="section-meta"><span>{e(c['method_kicker'])}</span><span>WORK → CAPABILITY → EVIDENCE</span></div><div class="method-head"><h2>{e(c['method_title'])}</h2><p>{e(c['method_intro'])}</p></div><ol class="steps">{steps}</ol><blockquote>“{e(c['quote'])}”</blockquote></section>
<section class="evidence-section reveal"><div class="evidence-visual"><div class="tech-architecture" role="group" aria-label="{'Promptedin palveluarkkitehtuurin havainnollistus, ei käyttöliittymän kuvakaappaus' if lang=='fi' else 'Conceptual representation of Prompted service architecture; not a product screenshot'}"><div class="tech-architecture-head"><span>PROMPTED / PRODUCT SYSTEM</span><span>01 — 02</span></div><div class="tech-module tech-module-coach"><span class="tech-module-no">01</span><div><strong>{'Digitaalinen valmennuspalvelu' if lang=='fi' else 'Digital coaching service'}</strong><p>{'Oppiminen ja harjoittelu osana omia työtehtäviä.' if lang=='fi' else 'Learning and practice within real work.'}</p></div><span class="tech-module-mark" aria-hidden="true">↗</span></div><div class="tech-transfer" aria-hidden="true"><span></span><span>WORK → EVIDENCE</span><span></span></div><div class="tech-module tech-module-data"><span class="tech-module-no">02</span><div><strong>Data / Evidence</strong><p>{'Organisaatiotason arviointi ilman yksityisiä valmennuskeskusteluja.' if lang=='fi' else 'Organisation-level evaluation without private coaching conversations.'}</p></div><span class="tech-module-mark" aria-hidden="true">◌</span></div><div class="tech-architecture-foot">{'PALVELULOGIIKAN HAVAINNOLLISTUS · EI TUOTEKAAPPAUS' if lang=='fi' else 'CONCEPTUAL SYSTEM MAP · NOT A PRODUCT SCREENSHOT'}</div></div></div><div class="evidence-copy"><div class="section-meta"><span>{e(c['evidence_kicker'])}</span><span>PROOF, NOT PERFORMANCE</span></div><h2>{e(c['evidence_title'])}</h2><p>{e(c['evidence_body'])}</p><div class="evidence-note"><span class="olive-dot"></span>{e(c['evidence_note'])}</div></div></section>
<section class="closing"><span class="mini-label">{e(c['close_kicker'])}</span><h2>{e(c['close_title'])}</h2><p>{e(c['close_body'])}</p><a class="button primary" href="{u['contact']}">{e(c['contact'])}<span aria-hidden="true">↗</span></a></section>'''


def product_signature(lang, slug):
    # This is an editorial product signature, NOT a screenshot of the application.
    labels={
      'fi':{
        'literacy':('01','LITERACY','Yhteinen perusta','Vastuullinen käyttö','Dokumentoitavat toimet'),
        'capability':('02','CAPABILITY','Lähtötilanne','Työssä harjoittelu','Muutoksen arviointi'),
        'transformation':('03','TRANSFORMATION','Liiketoiminnan tavoite','Työtapojen muutos','Jatkuva kehitys')
      },
      'en':{
        'literacy':('01','LITERACY','Shared foundation','Responsible use','Documented measures'),
        'capability':('02','CAPABILITY','Baseline','Practice at work','Evaluation of change'),
        'transformation':('03','TRANSFORMATION','Business direction','Change in work','Continuous progress')
      }
    }
    num,name,*steps=labels[lang][slug]
    content=''.join(f'<li><span>0{i+1}</span><strong>{e(val)}</strong></li>' for i,val in enumerate(steps))
    return f'<aside class="product-signature" aria-label="{name}"><div class="product-signature-heading"><span>THE APPROACH</span><span>{num} / 03</span></div><div class="product-signature-number" aria-hidden="true">{num}</div><div class="product-signature-name">PROMPTED / {name}</div><ol>{content}</ol></aside>'

def cap_page(lang):
 c=C[lang];u=urls(lang)
 stages=''.join(f'<li><span class="mini-label">{e(k)}</span><p>{e(txt)}</p></li>' for k,txt in c['cap_stages'])
 return f'''<section class="subpage-hero product-page-hero product-capability"><div class="product-hero-grid"><div class="product-hero-copy"><span class="mini-label olive">{e(c['cap_eyebrow'])}</span><h1>{e(c['cap_title'])}</h1><p>{e(c['cap_lead'])}</p><a class="button primary" href="{u['contact']}">{e(c['cap_cta'])}<span aria-hidden="true">↗</span></a></div>{product_signature(lang,'capability')}</div></section>
<section class="section section-light"><div class="section-meta"><span>01 / PILOT</span><span>BASELINE → PRACTICE → EVIDENCE</span></div><div class="lead-layout"><h2>{e(c['cap_scope_title'])}</h2><p class="large-paragraph">{e(c['cap_scope_body'])}</p></div><ol class="cap-steps">{stages}</ol></section>
<section class="section section-white rc7-cap-system"><div class="section-meta"><span>{'PALVELU JA TEKNOLOGIA' if lang=='fi' else 'SERVICE AND TECHNOLOGY'}</span><span>HUMAN + DIGITAL / DATA + EVIDENCE</span></div><div class="rc7-cap-system-grid"><div><span class="mini-label">THE DELIVERY MODEL</span><h2>{e(c['cap_difference_title'])}</h2><p>{e(c['cap_difference_body'])}</p><div class="rc7-principle"><span>↗</span><p>{e(c['cap_privacy_body'])}</p></div></div><div class="rc7-tech-system" role="group" aria-label="{'Prompted Capabilityn palveluosat, ei kuvakaappaus' if lang=='fi' else 'Prompted Capability components, not a screenshot'}"><div class="rc7-tech-head"><span>PROMPTED / CAPABILITY</span><span>SYSTEM / 02</span></div><div class="rc7-tech-row"><span>01</span><div><strong>{'Digitaalinen valmennuspalvelu' if lang=='fi' else 'Digital coaching service'}</strong><small>{'Harjoittelu omassa työssä · henkilökohtainen tuki' if lang=='fi' else 'Practice at work · personalised support'}</small></div></div><div class="rc7-tech-join"><span>WORK → EVIDENCE</span></div><div class="rc7-tech-row"><span>02</span><div><strong>Data / Evidence</strong><small>{'Arvioitu muutos · organisaatiotason yhteenveto' if lang=='fi' else 'Evaluated change · organisation-level view'}</small></div></div><div class="rc7-tech-bottom">{'TOIMINTAMALLIN HAVAINNOLLISTUS / EI TUOTEKUVA' if lang=='fi' else 'CONCEPTUAL REPRESENTATION / NOT A SCREENSHOT'}</div></div></div><p class="disclaimer">{e(c['cap_disclaimer'])}</p></section>
<section class="closing"><span class="mini-label">LET’S BEGIN</span><h2>{e(c['close_title'])}</h2><p>{e(c['close_body'])}</p><a class="button primary" href="{u['contact']}">{e(c['cap_cta'])} ↗</a></section>'''


def service_page(lang, key):
 c=C[lang]; u=urls(lang); s=SERVICES[lang][key]
 steps=''.join(f'<li><span class="mini-label">{e(t)}</span><p>{e(b)}</p></li>' for t,b in s['steps'])
 faq=''.join(f'<div class="qa"><h3>{e(q)}</h3><p>{e(a)}</p></div>' for q,a in s['faq'])
 return f'''<section class="subpage-hero product-page-hero product-{key}"><div class="product-hero-grid"><div class="product-hero-copy"><span class="mini-label olive">{e(s['eyebrow'])}</span><h1>{e(s['h1'])}</h1><p>{e(s['intro'])}</p><a class="button primary" href="{u['contact']}">{e(s['cta'])} ↗</a></div>{product_signature(lang,'literacy' if key=='literacy' else 'transformation')}</div></section>
<section class="section section-light"><div class="section-meta"><span>01 / {'LÄHTÖKOHTA' if lang=='fi' else 'THE CONTEXT'}</span><span>REAL WORK</span></div><div class="lead-layout"><h2>{e(s['why_title'])}</h2><p class="large-paragraph">{e(s['why'])}</p></div></section>
<section class="section section-white"><div class="section-meta"><span>02 / {'TOTEUTUS' if lang=='fi' else 'THE APPROACH'}</span><span>CONTEXT → PRACTICE → NEXT STEP</span></div><ol class="cap-steps">{steps}</ol></section>
<section class="section section-dark"><div class="split-copy"><div><span class="mini-label">WHO IT HELPS</span><h2>{e(s['who_title'])}</h2><p>{e(s['who'])}</p></div><div><span class="mini-label">HONEST SCOPE</span><h2>{e(s['bound_title'])}</h2><p>{e(s['bound'])}</p></div></div></section>
<section class="section section-light">{('<div class="official-source-band"><p class="official-source">'+('Sääntelyn alkuperäislähde' if lang=='fi' else 'Official regulatory reference')+': <a href="https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-4" rel="noopener noreferrer">EU AI Act, '+('artikla' if lang=='fi' else 'Article')+' 4 ↗</a></p></div>') if key=='literacy' else ''}<div class="section-meta"><span>03 / {'USEIN KYSYTTYÄ' if lang=='fi' else 'COMMON QUESTIONS'}</span><span>FAQ</span></div><div class="qa-grid">{faq}</div><a class="textlink" href="{u['cap']}">{'Tutustu myös Capability-pilottiin' if lang=='fi' else 'Explore the Capability pilot'} ↗</a></section>
<section class="closing"><span class="mini-label">{'SEURAAVA ASKEL' if lang=='fi' else 'NEXT STEP'}</span><h2>{e(c['close_title'])}</h2><p>{e(c['close_body'])}</p><a class="button primary" href="{u['contact']}">{e(s['cta'])} ↗</a></section>'''

def company_page(lang):
 c=C[lang];u=urls(lang)
 human = ("Promptedin perustaja Jarkko Sjöman yhdistää kokemuksen yritysviestinnästä, valmennuksesta ja luovasta työstä. Hän vastaa Promptedin kaupallisesta suunnasta ja asiakasyhteistyöstä." if lang=='fi' else
          "Prompted founder Jarkko Sjöman brings together business communications, coaching and creative practice. He leads Prompted’s commercial direction and customer relationships.")
 method = ("Lähtökohta on asiakkaan oikea työ. Uusia tapoja kokeillaan, toistetaan ja sovelletaan ennen kuin arvioidaan, mitä todella muuttui." if lang=='fi' else
           "We start with the customer's real work. New practices are tried, repeated and transferred before evaluating what actually changed.")
 limit = ("Emme julkaise tunnistettavia asiakastuloksia tai mittareita ilman todennettua näyttöä ja asianmukaista lupaa." if lang=='fi' else
          "We do not publish identifiable client outcomes or impact figures without verifiable evidence and appropriate permission.")
 return f'''<section class="subpage-hero company-page-hero"><span class="mini-label olive">{e(c['company_eyebrow'])}</span><h1>{e(c['company_title'])}</h1><p>{e(c['company_lead'])}</p></section>
<figure class="rc7-about-art"><img loading="lazy" src="/assets/hero-material.webp" alt="{'Betonin ja tumman pinnan välinen saumakohta, oliivinvärinen valosignaali' if lang=='fi' else 'Material detail: concrete and dark surface divided by a subtle olive light'}" width="1672" height="941"><figcaption><span>H05 / MATTER</span><span>{'MATERIAALITUTKIELMA · EI HYVÄKSYTTY' if lang=='fi' else 'MATERIAL STUDY · NOT APPROVED'}</span></figcaption></figure>
<section class="section section-light"><div class="section-meta"><span>WHY PROMPTED</span><span>HUMAN CAPABILITY</span></div><div class="lead-layout"><h2>{e(c['problem_note'])}</h2><div class="lead-text"><p>{e(c['company_body'])}</p><a class="textlink" href="{u['contact']}">{e(c['contact'])} ↗</a></div></div></section>
<section class="section section-dark"><div class="section-meta"><span>{'TUOTE JA TEKNOLOGIA' if lang=='fi' else 'PRODUCT AND TECHNOLOGY'}</span><span>WORK → CAPABILITY → EVIDENCE</span></div><div class="lead-layout"><h2>{'Kyvykkyyden kehittämistä, ei vain koulutusta.' if lang=='fi' else 'Capability development, not just training.'}</h2><div class="lead-text"><p>{'Prompted kehittää omaa digitaalista valmennuspalvelua ja näyttöön perustuvaa arviointia, jotta oppiminen kiinnittyy todellisiin työtehtäviin. Teknologia tukee harjoittelua; ihminen johtaa muutosta. Tuotteiden toimitusmalli ja mahdolliset pilotin rajaukset sovitaan asiakaskohtaisesti.' if lang=='fi' else 'Prompted develops a digital coaching service and evidence-based evaluation to bring learning into actual workplace tasks. Technology supports practice; people lead change. Delivery and pilot scope are agreed with each customer.'}</p></div></div></section>
<section class="section section-white"><div class="section-meta"><span>{'IHMISET JA MENETELMÄ' if lang=='fi' else 'PEOPLE AND METHOD'}</span><span>REAL WORK → EVIDENCE</span></div><div class="split-copy about-principles"><div><span class="mini-label">FOUNDER</span><h2>Jarkko Sjöman</h2><p>{e(human)}</p><p class="founder-profile"><a class="textlink" href="https://jarkkosjoman.com/" target="_blank" rel="noopener noreferrer">{'Perustajan oma sivusto' if lang=='fi' else 'Founder’s website'} <span aria-hidden="true">↗</span></a></p></div><div><span class="mini-label">WORKING PRINCIPLE</span><h2>{'Näyttö ennen väitettä' if lang=='fi' else 'Evidence before claims'}</h2><p>{e(method)}</p><p class="secondary-note">{e(limit)}</p></div></div></section>'''

def contact_page(lang):
 c=C[lang];subject=c['email_subject'].replace(' ','%20')
 steps=''.join(f'<li><span>{e(k)}</span>{e(tx)}</li>' for k,tx in c['contact_steps'])
 return f'''<section class="subpage-hero contact-hero"><span class="mini-label olive">{e(c['contact_eyebrow'])}</span><h1>{e(c['contact_page_title'])}</h1><p>{e(c['contact_page_body'])}</p><div class="contact-box"><span class="mini-label">{e(c['email_label'])}</span><a href="mailto:jarkko@prompted.fi?subject={e(subject)}">jarkko@prompted.fi <span>↗</span></a></div></section><section class="section section-light"><div class="section-meta"><span>THE NEXT STEP</span><span>01—03</span></div><ol class="contact-steps">{steps}</ol></section>'''

def privacy_page(lang):
 c=C[lang];bits=''.join(f'<section class="legal-item"><h2>{e(a)}</h2><p>{e(b)}</p></section>' for a,b in c['privacy_sections'])
 return f'''<section class="subpage-hero legal-hero"><span class="mini-label olive">PROMPTED / PRIVACY</span><h1>{e(c['privacy_title'])}</h1><p>{e(c['privacy_intro'])}</p></section><section class="section section-light legal-body">{bits}<p class="legal-date">21.10.2026 · {'Julkaisua edeltävä tarkistusversio, vahvistettava ennen lopullista käyttöönottoa.' if lang=='fi' else 'Pre-publication draft; must be verified before the final launch.'}</p></section>'''

def terms_page(lang):
 c=C[lang]
 return f'''<section class="subpage-hero legal-hero"><span class="mini-label olive">PROMPTED / TERMS</span><h1>{e(c['terms_title'])}</h1><p>{e(c['terms_body'])}</p></section>'''

def write(path,txt):
 dst=ROOT/path;dst.parent.mkdir(parents=True,exist_ok=True);dst.write_text(txt,encoding='utf-8')

for lang in ('fi','en'):
 c=C[lang];u=urls(lang)
 for key,body,ttl,desc in [
 ('home',main_home(lang),'Companies grow when people grow',c['site_desc']),
 ('literacy',service_page(lang,'literacy'),'Literacy',SERVICES[lang]['literacy']['meta']),
 ('cap',cap_page(lang),'Capability',c['cap_lead']),
 ('transform',service_page(lang,'transform'),'Transformation',SERVICES[lang]['transform']['meta']),
 ('company',company_page(lang),'Company' if lang=='en' else 'Yritys',c['company_lead']),
 ('contact',contact_page(lang),'Contact' if lang=='en' else 'Yhteys',c['contact_page_body']),
 ('privacy',privacy_page(lang),'Privacy' if lang=='en' else 'Tietosuoja',c['privacy_intro']),
 ('terms',terms_page(lang),'Service terms' if lang=='en' else 'Palveluehdot',c['terms_body'])]:
  write(Path(u[key].lstrip('/'))/'index.html',shell(lang,key,ttl,desc,body))
write(Path('index.html'),'''<!doctype html><html lang="fi"><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow"><meta http-equiv="refresh" content="0; url=/fi/"><link rel="canonical" href="https://prompted.fi/fi/"></head><body><a href="/fi/">Prompted →</a></body></html>''')
write(Path('robots.txt'),'''User-agent: *\nAllow: /\n\nUser-agent: OAI-SearchBot\nAllow: /\n\nSitemap: https://prompted.fi/sitemap.xml\n''' if PRODUCTION else '''User-agent: *\nAllow: /\n# Prelaunch HTML includes noindex; crawlers must reach it. Preview access should also be protected by hosting authentication.\n''')
if PRODUCTION:
 import xml.sax.saxutils as xu
 sitemap=''.join(f'<url><loc>https://prompted.fi{urls(l)[p]}</loc><lastmod>{LAST_MEANINGFUL_UPDATE}</lastmod></url>' for l in ('fi','en') for p in ('home','literacy','cap','transform','company','contact','privacy','terms'))
 write(Path('sitemap.xml'),'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+sitemap+'</urlset>')
else:
 (ROOT/'sitemap.xml').unlink(missing_ok=True)
write(Path('vercel.json'),json.dumps({'version':2,'cleanUrls':False,'trailingSlash':True,'redirects':[{'source':'/','destination':'/fi/','permanent':False},{'source':'/capability','destination':'/fi/capability/','permanent':True},{'source':'/literacy','destination':'/fi/literacy/','permanent':True},{'source':'/transformation','destination':'/fi/transformation/','permanent':True},{'source':'/transformerism','destination':'/fi/transformation/','permanent':True},{'source':'/fi/transformerism','destination':'/fi/transformation/','permanent':True},{'source':'/en/transformerism','destination':'/en/transformation/','permanent':True},{'source':'/privacy','destination':'/fi/tietosuoja/','permanent':True},{'source':'/terms','destination':'/fi/ehdot/','permanent':True},{'source':'/contact','destination':'/fi/yhteys/','permanent':True}],'headers':[{'source':'/(.*)','headers':[{'key':'X-Content-Type-Options','value':'nosniff'},{'key':'Referrer-Policy','value':'strict-origin-when-cross-origin'},{'key':'X-Frame-Options','value': 'DENY'},{'key':'Permissions-Policy','value':'camera=(), microphone=(), geolocation=()'}]+([] if PRODUCTION else [{'key':'X-Robots-Tag','value':'noindex, nofollow'}])}]},indent=2))
print('Built',len(list(ROOT.rglob('*.html'))),'HTML pages')
