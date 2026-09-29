#!/usr/bin/env python3
"""Builds the PDF On site: one landing page per language (own URL, hreflang, Open Graph, JSON-LD, screenshots),
support, sitemap.xml and llms.txt. privacy.html is kept as a hand-written file.
Run `python3 build.py` after editing the texts below; the generated HTML files are never edited by hand."""
import html
import json
import os
import pathlib

SITE = "https://abbas-hoseiny.github.io/pdfgo/"   # switch to an own domain: change SITE and BASE, add a CNAME file
BASE = "/pdfgo/"
DATE = "2026-09-29"
APP_ID = "6812877977"
STORE = f"https://apps.apple.com/app/pdf-on/id{APP_ID}"
GITHUB = "https://github.com/Abbas-Hoseiny/pdfgo"
GOOGLE_VERIFICATION = os.environ.get("GOOGLE_SITE_VERIFICATION", "")   # Search Console HTML tag, once Abbas has it
ROOT = pathlib.Path(__file__).resolve().parent

# code, name, direction, Open Graph locale, path below the site root, App Store storefront
LANGS = [("en", "English", "ltr", "en_US", "", ""), ("de", "Deutsch", "ltr", "de_DE", "de/", "de"), ("es", "Español", "ltr", "es_ES", "es/", "es"),
         ("tr", "Türkçe", "ltr", "tr_TR", "tr/", "tr"), ("ar", "العربية", "rtl", "ar_AR", "ar/", ""), ("fa", "فارسی", "rtl", "fa_IR", "fa/", ""),
         ("ur", "اردو", "rtl", "ur_PK", "ur/", "")]
# every language the app itself speaks (project.yml knownRegions)
APP_LANGS = ["en", "de", "es", "tr", "ar", "fa", "ur", "en-GB", "fr", "it", "pt-BR", "pt-PT", "nl", "pl", "ru", "uk", "cs", "sk", "hu", "ro",
             "el", "sv", "da", "nb", "fi", "ca", "hr", "sl", "id", "ms", "vi", "th", "ja", "ko", "zh-Hans", "zh-Hant", "hi", "bn", "gu",
             "kn", "ml", "mr", "or", "pa", "ta", "te"]
# screenshots per language: img/<lang>/<key>.webp (ar/ur show the library instead of the highlight list)
SHOTS = {"en": ["form", "reading", "id", "home", "highlights", "pages"], "de": ["form", "reading", "id", "home", "highlights", "pages"],
         "es": ["form", "reading", "id", "home", "highlights", "pages"], "tr": ["form", "reading", "id", "home", "highlights", "pages"],
         "ar": ["form", "reading", "id", "home", "library", "pages"], "fa": ["form", "reading", "id", "home", "highlights", "pages"],
         "ur": ["form", "reading", "id", "home", "library", "pages"]}

# ---------------------------------------------------------------- landing pages ------------------------------------------------------
L = {}

L["en"] = dict(
    title="PDF On – Scan, fill in and sign PDFs on iPhone. Free, offline.",
    desc="Free iPhone PDF app: scan paper to PDF, fill in any form (even a photographed one), sign, copy your ID card or passport in original size, convert Word to PDF, OCR. No account, no upload.",
    nav=("Home", "Privacy", "Support"),
    tag="Scan, fill in, sign. Everything stays on your iPhone.",
    store="Download on the App Store",
    store_note="Free · iOS 17 or later · No account",
    lead="PDF On is a free PDF scanner and editor for iPhone. It turns paper into clean PDFs, fills in forms (real PDF forms and photographed or scanned ones), places your signature and passport photo, copies an ID card or passport front and back onto one sheet in true size, converts Word, Excel and PowerPoint files to PDF, recognizes text offline and lets you highlight while reading. No account, no upload, no ads, no subscription.",
    problems_h2="When PDF On helps",
    problems=["You received a form as a PDF or on paper and have to fill it in, sign it and send it back today, from your phone.",
              "A landlord, bank or employer wants a copy of your ID card or passport, both sides, and it should look like a proper photocopy.",
              "You need to send a signed contract, a job application with your photo, or a scanned receipt, as one clean PDF with a sensible file name.",
              "You want to read a long PDF, mark the important lines and get all your highlights as a list.",
              "You do not want a scanner app that needs an account, a subscription or uploads your documents to somebody's cloud."],
    features_h2="What PDF On can do",
    features=[("📄", "Scan and create PDFs", "Scan documents with automatic edge detection, or take a photo and let the edges be found and straightened. Build PDFs from photos, files and other PDFs; choose page size, layout (1, 2 or 4 per page) and quality; add date and time stamps; protect with a password."),
              ("✏️", "Fill in any form", "Tap a field and type: the text lands inside the box, on the line. Return jumps to the next field, checkmarks snap into checkboxes, dates follow the form's format. Works with real PDF forms and with photographed or scanned ones. Your name, address and phone appear as suggestions above the keyboard (Settings › My details)."),
              ("✍️", "Sign and add your photo", "Sign with your finger, or photograph your signature on paper; it lands over the signature line. A passport photo goes into the photo frame of an application form, found automatically."),
              ("🪪", "ID card & passport copy", "Front and back on one sheet in true original size, optionally enlarged, in color or grayscale, with cut lines and a watermark such as “Copy for landlord”."),
              ("🔍", "Text recognition, offline", "On-device OCR makes scans searchable. Copy the text, search inside the document, or export it as a Word document (.docx)."),
              ("🖍️", "Read and highlight", "Full-screen reading mode with trimmed margins. Highlight with one swipe in four colors, name your colors, add notes, jump to any highlight from the list and share them as text. The app remembers where you stopped."),
              ("📑", "Manage pages", "Reorder, rotate, crop, straighten and delete pages. Merge PDFs, insert scans, photos or other PDFs. Convert Word, Excel, PowerPoint, Pages, Numbers, Keynote, text and HTML files to PDF."),
              ("🔒", "Private by design", "Works fully offline. No account, no ads, no tracking, no data collection. Optional app lock with Face ID. Share extension: send photos and PDFs from other apps to PDF On.")],
    shots_h2="Screenshots",
    shots={"form": "Filling in a photographed form: the text lands inside the boxes", "reading": "Reading mode with highlights",
           "id": "ID card and passport copy in original size", "home": "Start: scan, photos, camera, file",
           "highlights": "The list of all highlights", "library": "The library with all PDFs", "pages": "Manage pages: reorder, crop, merge"},
    how_h2="How it works",
    steps=[("Capture", "Scan a document, pick photos, or open a PDF or Word file."),
           ("Fill in and sign", "Tap, type, set checkmarks, sign. Your details are one tap away above the keyboard."),
           ("Share", "AirDrop, Mail, WhatsApp or any app, with a proper file name. Your PDFs stay in the library on your iPhone.")],
    privacy_h3="Privacy in one sentence",
    privacy_text="No account, no server of ours, no ads. Everything, including text recognition, is computed and stored on your iPhone; a document leaves the phone only when you share it yourself.",
    privacy_link="Read the privacy policy",
    faq_h2="Frequently asked questions",
    faqs=[("Is PDF On free?", "Yes. PDF On is free, without ads, without an account and without a subscription."),
          ("Can I fill in a PDF form that has no real form fields, for example a scanned or photographed form?", "Yes. Tap the box on the page and type; the text is placed inside the box, on the line. Return jumps to the next box, checkmarks snap into checkboxes. Real PDF forms with fields work too."),
          ("How do I copy my ID card or passport, front and back, on one page with my iPhone?", "Open PDF On › ID card & passport, photograph the front and the back. PDF On places both on one A4 or Letter sheet in original size, optionally enlarged, in color or grayscale, with cut lines and an optional watermark such as “Copy for landlord”."),
          ("How do I sign a PDF on my iPhone?", "Open the PDF in PDF On, tap Edit and choose Signature. Draw it with your finger, or photograph your signature on paper; the background is removed and the signature lands over the signature line. Saved signatures can be reused."),
          ("Are my documents uploaded anywhere?", "No. PDF On has no server. Scanning, text recognition and face and frame detection run on the iPhone. A document leaves the phone only when you share it yourself, for example by AirDrop, Mail or WhatsApp."),
          ("Does PDF On have OCR and does it work offline?", "Yes. Text recognition runs on the device with Apple's Vision framework, without internet. Recognized text can be copied, searched and exported as a Word document (.docx)."),
          ("Can PDF On convert Word, Excel or PowerPoint files to PDF?", "Yes. Open a Word, Excel, PowerPoint, Pages, Numbers, Keynote, text or HTML file in PDF On and it becomes a PDF, on the device."),
          ("Which iPhones and languages?", "Every iPhone with iOS 17 or later. The app speaks 46 languages, among them English, German, Spanish, Turkish, Arabic, Persian, Urdu, French, Italian, Portuguese, Hindi, Japanese, Korean and Chinese, with full right-to-left layout for Arabic, Persian and Urdu.")],
)

L["de"] = dict(
    title="PDF On – PDF scannen, ausfüllen und unterschreiben auf dem iPhone. Kostenlos, offline.",
    desc="Kostenlose iPhone-PDF-App: Papier scannen, jedes Formular ausfüllen (auch fotografierte), unterschreiben, Ausweis oder Reisepass in Originalgröße kopieren, Word zu PDF, Texterkennung. Ohne Konto, ohne Upload.",
    nav=("Start", "Datenschutz", "Support"),
    tag="Scannen, ausfüllen, unterschreiben. Alles bleibt auf deinem iPhone.",
    store="Laden im App Store",
    store_note="Kostenlos · iOS 17 oder neuer · Ohne Konto",
    lead="PDF On ist ein kostenloser PDF-Scanner und -Editor für das iPhone. Er macht aus Papier saubere PDFs, füllt Formulare aus (echte PDF-Formulare und fotografierte oder gescannte), setzt Unterschrift und Bewerbungsfoto, kopiert Ausweis oder Reisepass mit Vorder- und Rückseite auf ein Blatt in Originalgröße, wandelt Word-, Excel- und PowerPoint-Dateien in PDF um, erkennt Text offline und markiert beim Lesen. Ohne Konto, ohne Upload, ohne Werbung, ohne Abo.",
    problems_h2="Wann PDF On hilft",
    problems=["Du hast ein Formular als PDF oder auf Papier bekommen und musst es heute noch ausfüllen, unterschreiben und zurückschicken, vom Handy aus.",
              "Vermieter, Bank oder Arbeitgeber wollen eine Kopie von Ausweis oder Reisepass, beide Seiten, und sie soll wie eine richtige Fotokopie aussehen.",
              "Du musst einen unterschriebenen Vertrag, eine Bewerbung mit Foto oder einen gescannten Beleg als ein sauberes PDF mit vernünftigem Dateinamen schicken.",
              "Du willst ein langes PDF lesen, die wichtigen Zeilen markieren und alle Markierungen als Liste bekommen.",
              "Du willst keine Scanner-App, die ein Konto oder ein Abo braucht oder deine Dokumente in irgendeine Cloud lädt."],
    features_h2="Was PDF On kann",
    features=[("📄", "Scannen und PDFs erstellen", "Dokumente scannen mit automatischer Randerkennung, oder ein Foto machen und die Ränder finden und geraderichten lassen. PDFs aus Fotos, Dateien und anderen PDFs bauen; Seitengröße, Layout (1, 2 oder 4 pro Seite) und Qualität wählen; Datum und Uhrzeit stempeln; mit Passwort schützen."),
              ("✏️", "Jedes Formular ausfüllen", "Feld antippen und schreiben: Der Text landet im Kästchen, auf der Linie. Die Eingabetaste springt ins nächste Feld, Häkchen rasten in Kontrollkästchen ein, Daten folgen dem Format des Formulars. Geht mit echten PDF-Formularen und mit fotografierten oder gescannten. Name, Adresse und Telefon erscheinen als Vorschläge über der Tastatur (Einstellungen › Meine Angaben)."),
              ("✍️", "Unterschrift und Foto", "Mit dem Finger unterschreiben oder die Unterschrift vom Papier abfotografieren; sie landet über der Unterschriftszeile. Ein Bewerbungsfoto kommt in den Fotorahmen des Formulars, der automatisch erkannt wird."),
              ("🪪", "Ausweis & Reisepass kopieren", "Vorder- und Rückseite auf einem Blatt in Originalgröße, wahlweise vergrößert, farbig oder in Graustufen, mit Schnittlinien und einem Wasserzeichen wie „Kopie für Vermieter“."),
              ("🔍", "Texterkennung, offline", "Die Texterkennung auf dem Gerät macht Scans durchsuchbar. Text kopieren, im Dokument suchen oder als Word-Dokument (.docx) exportieren."),
              ("🖍️", "Lesen und markieren", "Lesemodus im Vollbild mit beschnittenen Rändern. Mit einem Wisch in vier Farben markieren, Farben benennen, Notizen anfügen, aus der Liste zu jeder Markierung springen und sie als Text teilen. Die App merkt sich, wo du aufgehört hast."),
              ("📑", "Seiten verwalten", "Seiten ordnen, drehen, zuschneiden, geraderichten und löschen. PDFs zusammenführen, Scans, Fotos oder andere PDFs einfügen. Word-, Excel-, PowerPoint-, Pages-, Numbers-, Keynote-, Text- und HTML-Dateien in PDF umwandeln."),
              ("🔒", "Privat von Grund auf", "Funktioniert komplett offline. Kein Konto, keine Werbung, kein Tracking, keine Datensammlung. Optionale App-Sperre mit Face ID. Teilen-Erweiterung: Fotos und PDFs aus anderen Apps an PDF On schicken.")],
    shots_h2="Screenshots",
    shots={"form": "Fotografiertes Formular ausfüllen: Der Text landet in den Kästchen", "reading": "Lesemodus mit Markierungen",
           "id": "Ausweis- und Reisepasskopie in Originalgröße", "home": "Start: Scannen, Fotos, Kamera, Datei",
           "highlights": "Die Liste aller Markierungen", "library": "Die Bibliothek mit allen PDFs", "pages": "Seiten verwalten: ordnen, zuschneiden, zusammenführen"},
    how_h2="So geht es",
    steps=[("Aufnehmen", "Dokument scannen, Fotos auswählen oder ein PDF oder eine Word-Datei öffnen."),
           ("Ausfüllen und unterschreiben", "Antippen, schreiben, Häkchen setzen, unterschreiben. Deine Angaben stehen über der Tastatur bereit."),
           ("Teilen", "AirDrop, Mail, WhatsApp oder jede App, mit richtigem Dateinamen. Deine PDFs bleiben in der Bibliothek auf deinem iPhone.")],
    privacy_h3="Datenschutz in einem Satz",
    privacy_text="Kein Konto, kein eigener Server, keine Werbung. Alles, auch die Texterkennung, wird auf deinem iPhone gerechnet und gespeichert; ein Dokument verlässt das Telefon nur, wenn du es selbst teilst.",
    privacy_link="Datenschutzerklärung lesen",
    faq_h2="Häufige Fragen",
    faqs=[("Ist PDF On kostenlos?", "Ja. PDF On ist kostenlos, ohne Werbung, ohne Konto und ohne Abo."),
          ("Kann ich ein PDF-Formular ohne echte Formularfelder ausfüllen, zum Beispiel ein gescanntes oder fotografiertes?", "Ja. Kästchen auf der Seite antippen und schreiben; der Text wird im Kästchen auf der Linie platziert. Die Eingabetaste springt ins nächste Kästchen, Häkchen rasten in Kontrollkästchen ein. Echte PDF-Formulare mit Feldern gehen auch."),
          ("Wie kopiere ich Ausweis oder Reisepass mit Vorder- und Rückseite auf eine Seite mit dem iPhone?", "PDF On › Ausweis & Reisepass öffnen, Vorder- und Rückseite fotografieren. PDF On setzt beide auf ein A4- oder Letter-Blatt in Originalgröße, wahlweise vergrößert, farbig oder in Graustufen, mit Schnittlinien und optionalem Wasserzeichen wie „Kopie für Vermieter“."),
          ("Wie unterschreibe ich ein PDF auf dem iPhone?", "PDF in PDF On öffnen, Bearbeiten antippen und Unterschrift wählen. Mit dem Finger zeichnen oder die Unterschrift vom Papier abfotografieren; der Hintergrund wird entfernt und die Unterschrift landet über der Unterschriftszeile. Gespeicherte Unterschriften lassen sich wiederverwenden."),
          ("Werden meine Dokumente irgendwohin hochgeladen?", "Nein. PDF On hat keinen Server. Scannen, Texterkennung sowie Gesichts- und Rahmenerkennung laufen auf dem iPhone. Ein Dokument verlässt das Telefon nur, wenn du es selbst teilst, etwa per AirDrop, Mail oder WhatsApp."),
          ("Hat PDF On Texterkennung (OCR) und geht sie offline?", "Ja. Die Texterkennung läuft auf dem Gerät mit Apples Vision-Framework, ohne Internet. Erkannter Text lässt sich kopieren, durchsuchen und als Word-Dokument (.docx) exportieren."),
          ("Kann PDF On Word-, Excel- oder PowerPoint-Dateien in PDF umwandeln?", "Ja. Eine Word-, Excel-, PowerPoint-, Pages-, Numbers-, Keynote-, Text- oder HTML-Datei in PDF On öffnen, und sie wird auf dem Gerät zum PDF."),
          ("Welche iPhones und Sprachen?", "Jedes iPhone mit iOS 17 oder neuer. Die App spricht 46 Sprachen, darunter Deutsch, Englisch, Spanisch, Türkisch, Arabisch, Persisch, Urdu, Französisch, Italienisch, Portugiesisch, Hindi, Japanisch, Koreanisch und Chinesisch, mit vollständigem Rechts-nach-links-Layout für Arabisch, Persisch und Urdu.")],
)

L["es"] = dict(
    title="PDF On – Escanear, rellenar y firmar PDF en el iPhone. Gratis, sin conexión.",
    desc="App de PDF gratuita para iPhone: escanea papel a PDF, rellena cualquier formulario (incluso fotografiado), firma, copia tu DNI o pasaporte a tamaño real, convierte Word a PDF, OCR. Sin cuenta, sin subidas.",
    nav=("Inicio", "Privacidad", "Soporte"),
    tag="Escanea, rellena, firma. Todo se queda en tu iPhone.",
    store="Descargar en el App Store",
    store_note="Gratis · iOS 17 o posterior · Sin cuenta",
    lead="PDF On es un escáner y editor de PDF gratuito para iPhone. Convierte el papel en PDF limpios, rellena formularios (formularios PDF reales y también fotografiados o escaneados), coloca tu firma y tu foto de carnet, copia el DNI o el pasaporte por ambas caras en una hoja a tamaño real, convierte archivos de Word, Excel y PowerPoint a PDF, reconoce texto sin conexión y te deja subrayar mientras lees. Sin cuenta, sin subidas, sin anuncios, sin suscripción.",
    problems_h2="Cuándo ayuda PDF On",
    problems=["Has recibido un formulario en PDF o en papel y tienes que rellenarlo, firmarlo y devolverlo hoy, desde el móvil.",
              "El casero, el banco o la empresa quieren una copia de tu DNI o pasaporte, por las dos caras, y debe parecer una fotocopia de verdad.",
              "Tienes que enviar un contrato firmado, una solicitud de empleo con tu foto o un recibo escaneado, como un solo PDF limpio con un nombre de archivo sensato.",
              "Quieres leer un PDF largo, marcar las líneas importantes y tener todas tus marcas en una lista.",
              "No quieres una app de escaneo que exija cuenta o suscripción o que suba tus documentos a la nube de alguien."],
    features_h2="Qué puede hacer PDF On",
    features=[("📄", "Escanear y crear PDF", "Escanea documentos con detección automática de bordes, o haz una foto y deja que los bordes se detecten y se enderecen. Crea PDF a partir de fotos, archivos y otros PDF; elige tamaño de página, disposición (1, 2 o 4 por página) y calidad; añade sellos de fecha y hora; protege con contraseña."),
              ("✏️", "Rellenar cualquier formulario", "Toca un campo y escribe: el texto queda dentro de la casilla, sobre la línea. Intro salta al campo siguiente, las marcas encajan en las casillas, las fechas siguen el formato del formulario. Funciona con formularios PDF reales y con fotografiados o escaneados. Tu nombre, dirección y teléfono aparecen como sugerencias sobre el teclado (Ajustes › Mis datos)."),
              ("✍️", "Firmar y añadir tu foto", "Firma con el dedo o fotografía tu firma en papel; queda sobre la línea de firma. La foto de carnet va al recuadro de la solicitud, que se detecta solo."),
              ("🪪", "Copia de DNI y pasaporte", "Anverso y reverso en una hoja a tamaño real, con ampliación opcional, en color o en escala de grises, con líneas de corte y una marca de agua como «Copia para el casero»."),
              ("🔍", "Reconocer texto, sin conexión", "El OCR en el dispositivo hace que los escaneos se puedan buscar. Copia el texto, busca dentro del documento o expórtalo como documento de Word (.docx)."),
              ("🖍️", "Leer y subrayar", "Modo de lectura a pantalla completa con márgenes recortados. Subraya con un gesto en cuatro colores, pon nombre a tus colores, añade notas, salta a cualquier marca desde la lista y compártelas como texto. La app recuerda dónde te quedaste."),
              ("📑", "Gestionar páginas", "Reordena, gira, recorta, endereza y elimina páginas. Combina PDF, inserta escaneos, fotos u otros PDF. Convierte archivos de Word, Excel, PowerPoint, Pages, Numbers, Keynote, texto y HTML a PDF."),
              ("🔒", "Privado por diseño", "Funciona totalmente sin conexión. Sin cuenta, sin anuncios, sin rastreo, sin recopilación de datos. Bloqueo opcional de la app con Face ID. Extensión de compartir: envía fotos y PDF desde otras apps a PDF On.")],
    shots_h2="Capturas de pantalla",
    shots={"form": "Rellenar un formulario fotografiado: el texto queda en las casillas", "reading": "Modo de lectura con marcas",
           "id": "Copia de DNI y pasaporte a tamaño real", "home": "Inicio: escanear, fotos, cámara, archivo",
           "highlights": "La lista de todas las marcas", "library": "La biblioteca con todos los PDF", "pages": "Gestionar páginas: ordenar, recortar, combinar"},
    how_h2="Cómo funciona",
    steps=[("Capturar", "Escanea un documento, elige fotos o abre un PDF o un archivo de Word."),
           ("Rellenar y firmar", "Toca, escribe, marca casillas, firma. Tus datos están a un toque sobre el teclado."),
           ("Compartir", "AirDrop, Mail, WhatsApp o cualquier app, con un nombre de archivo correcto. Tus PDF se quedan en la biblioteca de tu iPhone.")],
    privacy_h3="Privacidad en una frase",
    privacy_text="Sin cuenta, sin servidor nuestro, sin anuncios. Todo, incluido el reconocimiento de texto, se calcula y se guarda en tu iPhone; un documento solo sale del teléfono cuando tú lo compartes.",
    privacy_link="Leer la política de privacidad",
    faq_h2="Preguntas frecuentes",
    faqs=[("¿PDF On es gratis?", "Sí. PDF On es gratis, sin anuncios, sin cuenta y sin suscripción."),
          ("¿Puedo rellenar un formulario PDF sin campos reales, por ejemplo uno escaneado o fotografiado?", "Sí. Toca la casilla en la página y escribe; el texto se coloca dentro de la casilla, sobre la línea. Intro salta a la casilla siguiente y las marcas encajan en las casillas de verificación. Los formularios PDF reales con campos también funcionan."),
          ("¿Cómo copio mi DNI o pasaporte por las dos caras en una página con el iPhone?", "Abre PDF On › DNI y pasaporte y fotografía el anverso y el reverso. PDF On coloca ambos en una hoja A4 o Carta a tamaño real, con ampliación opcional, en color o en escala de grises, con líneas de corte y una marca de agua opcional como «Copia para el casero»."),
          ("¿Cómo firmo un PDF en el iPhone?", "Abre el PDF en PDF On, toca Editar y elige Firma. Dibújala con el dedo o fotografía tu firma en papel; el fondo se elimina y la firma queda sobre la línea de firma. Las firmas guardadas se pueden reutilizar."),
          ("¿Mis documentos se suben a algún sitio?", "No. PDF On no tiene servidor. El escaneo, el reconocimiento de texto y la detección de caras y recuadros se ejecutan en el iPhone. Un documento solo sale del teléfono cuando tú lo compartes, por ejemplo por AirDrop, Mail o WhatsApp."),
          ("¿PDF On tiene OCR y funciona sin conexión?", "Sí. El reconocimiento de texto se ejecuta en el dispositivo con el framework Vision de Apple, sin internet. El texto reconocido se puede copiar, buscar y exportar como documento de Word (.docx)."),
          ("¿PDF On convierte archivos de Word, Excel o PowerPoint a PDF?", "Sí. Abre un archivo de Word, Excel, PowerPoint, Pages, Numbers, Keynote, texto o HTML en PDF On y se convierte en PDF, en el dispositivo."),
          ("¿Qué iPhones e idiomas?", "Cualquier iPhone con iOS 17 o posterior. La app habla 46 idiomas, entre ellos español, inglés, alemán, turco, árabe, persa, urdu, francés, italiano, portugués, hindi, japonés, coreano y chino, con diseño completo de derecha a izquierda para árabe, persa y urdu.")],
)

L["tr"] = dict(
    title="PDF On – iPhone'da PDF tara, doldur ve imzala. Ücretsiz, çevrimdışı.",
    desc="Ücretsiz iPhone PDF uygulaması: kâğıdı PDF'e tara, her formu doldur (fotoğrafı çekilmiş olsa bile), imzala, kimlik veya pasaportunu gerçek boyutta kopyala, Word'ü PDF'e dönüştür, OCR. Hesap yok, yükleme yok.",
    nav=("Başlangıç", "Gizlilik", "Destek"),
    tag="Tara, doldur, imzala. Her şey iPhone'unda kalır.",
    store="App Store'dan indir",
    store_note="Ücretsiz · iOS 17 veya üzeri · Hesap gerekmez",
    lead="PDF On, iPhone için ücretsiz bir PDF tarayıcı ve düzenleyicidir. Kâğıdı temiz PDF'lere dönüştürür, formları doldurur (gerçek PDF formları ile fotoğrafı çekilmiş veya taranmış olanları), imzanı ve vesikalık fotoğrafını yerleştirir, kimlik veya pasaportun ön ve arka yüzünü tek sayfaya gerçek boyutta kopyalar, Word, Excel ve PowerPoint dosyalarını PDF'e dönüştürür, metni çevrimdışı tanır ve okurken işaretlemeni sağlar. Hesap yok, yükleme yok, reklam yok, abonelik yok.",
    problems_h2="PDF On ne zaman işe yarar",
    problems=["PDF olarak ya da kâğıt üzerinde bir form aldın; bugün telefondan doldurup imzalayıp geri göndermen gerekiyor.",
              "Ev sahibi, banka veya işveren kimlik ya da pasaportunun iki yüzünün kopyasını istiyor ve düzgün bir fotokopi gibi görünmeli.",
              "İmzalı bir sözleşmeyi, fotoğraflı bir iş başvurusunu veya taranmış bir fişi, mantıklı bir dosya adıyla tek bir temiz PDF olarak göndermen gerekiyor.",
              "Uzun bir PDF'i okuyup önemli satırları işaretlemek ve tüm işaretlerini liste olarak almak istiyorsun.",
              "Hesap ya da abonelik isteyen veya belgelerini birilerinin bulutuna yükleyen bir tarayıcı uygulaması istemiyorsun."],
    features_h2="PDF On neler yapabilir",
    features=[("📄", "Tara ve PDF oluştur", "Belgeleri otomatik kenar algılama ile tara ya da fotoğraf çek, kenarlar bulunup düzeltilsin. Fotoğraflardan, dosyalardan ve başka PDF'lerden PDF oluştur; sayfa boyutunu, düzeni (sayfa başına 1, 2 veya 4) ve kaliteyi seç; tarih ve saat damgası ekle; parola ile koru."),
              ("✏️", "Her formu doldur", "Alana dokun ve yaz: metin kutunun içine, çizginin üzerine oturur. Return tuşu sonraki alana geçer, onay işaretleri kutucuklara oturur, tarihler formun biçimine uyar. Gerçek PDF formlarıyla ve fotoğrafı çekilmiş ya da taranmış formlarla çalışır. Adın, adresin ve telefonun klavyenin üstünde öneri olarak görünür (Ayarlar › Bilgilerim)."),
              ("✍️", "İmzala ve fotoğrafını ekle", "Parmağınla imzala ya da kâğıttaki imzanın fotoğrafını çek; imza çizgisinin üzerine oturur. Vesikalık fotoğraf, otomatik bulunan fotoğraf çerçevesine yerleşir."),
              ("🪪", "Kimlik ve pasaport kopyası", "Ön ve arka yüz tek sayfada gerçek boyutta, isteğe bağlı büyütme, renkli veya gri tonlu, kesim çizgileri ve „Ev sahibi için kopya“ gibi bir filigranla."),
              ("🔍", "Metin tanıma, çevrimdışı", "Cihaz üzerindeki OCR taramaları aranabilir yapar. Metni kopyala, belge içinde ara ya da Word belgesi (.docx) olarak dışa aktar."),
              ("🖍️", "Oku ve işaretle", "Kenar boşlukları kırpılmış tam ekran okuma modu. Tek kaydırmayla dört renkte işaretle, renklerine ad ver, not ekle, listeden herhangi bir işarete atla ve metin olarak paylaş. Uygulama kaldığın yeri hatırlar."),
              ("📑", "Sayfaları yönet", "Sayfaları yeniden sırala, döndür, kırp, düzelt ve sil. PDF'leri birleştir, tarama, fotoğraf ya da başka PDF'ler ekle. Word, Excel, PowerPoint, Pages, Numbers, Keynote, metin ve HTML dosyalarını PDF'e dönüştür."),
              ("🔒", "Tasarımı gereği özel", "Tamamen çevrimdışı çalışır. Hesap yok, reklam yok, izleme yok, veri toplama yok. Face ID ile isteğe bağlı uygulama kilidi. Paylaşım uzantısı: başka uygulamalardan fotoğraf ve PDF'leri PDF On'a gönder.")],
    shots_h2="Ekran görüntüleri",
    shots={"form": "Fotoğrafı çekilmiş bir formu doldurma: metin kutuların içine oturur", "reading": "İşaretli okuma modu",
           "id": "Gerçek boyutta kimlik ve pasaport kopyası", "home": "Başlangıç: tara, fotoğraflar, kamera, dosya",
           "highlights": "Tüm işaretlerin listesi", "library": "Tüm PDF'lerin bulunduğu arşiv", "pages": "Sayfaları yönet: sırala, kırp, birleştir"},
    how_h2="Nasıl çalışır",
    steps=[("Yakala", "Bir belge tara, fotoğraf seç ya da bir PDF veya Word dosyası aç."),
           ("Doldur ve imzala", "Dokun, yaz, onay işareti koy, imzala. Bilgilerin klavyenin üstünde tek dokunuşla hazır."),
           ("Paylaş", "AirDrop, Mail, WhatsApp ya da herhangi bir uygulama, doğru dosya adıyla. PDF'lerin iPhone'undaki arşivde kalır.")],
    privacy_h3="Tek cümleyle gizlilik",
    privacy_text="Hesap yok, bize ait sunucu yok, reklam yok. Metin tanıma dahil her şey iPhone'unda hesaplanır ve saklanır; bir belge telefondan yalnızca sen paylaştığında çıkar.",
    privacy_link="Gizlilik politikasını oku",
    faq_h2="Sık sorulan sorular",
    faqs=[("PDF On ücretsiz mi?", "Evet. PDF On ücretsizdir; reklam yok, hesap yok, abonelik yok."),
          ("Gerçek form alanları olmayan, örneğin taranmış ya da fotoğrafı çekilmiş bir PDF formunu doldurabilir miyim?", "Evet. Sayfadaki kutuya dokun ve yaz; metin kutunun içine, çizginin üzerine yerleşir. Return sonraki kutuya geçer, onay işaretleri kutucuklara oturur. Alanları olan gerçek PDF formları da çalışır."),
          ("iPhone ile kimlik ya da pasaportumun ön ve arka yüzünü tek sayfaya nasıl kopyalarım?", "PDF On › Kimlik ve pasaport'u aç, ön ve arka yüzün fotoğrafını çek. PDF On ikisini de bir A4 ya da Letter sayfaya gerçek boyutta yerleştirir; isteğe bağlı büyütme, renkli ya da gri tonlu, kesim çizgileri ve „Ev sahibi için kopya“ gibi isteğe bağlı filigranla."),
          ("iPhone'da bir PDF'i nasıl imzalarım?", "PDF'i PDF On'da aç, Düzenle'ye dokun ve İmza'yı seç. Parmağınla çiz ya da kâğıttaki imzanın fotoğrafını çek; arka plan kaldırılır ve imza, imza çizgisinin üzerine oturur. Kaydedilen imzalar yeniden kullanılabilir."),
          ("Belgelerim bir yere yükleniyor mu?", "Hayır. PDF On'un sunucusu yoktur. Tarama, metin tanıma, yüz ve çerçeve algılama iPhone'da çalışır. Bir belge telefondan yalnızca sen paylaştığında çıkar; örneğin AirDrop, Mail ya da WhatsApp ile."),
          ("PDF On'da OCR var mı ve çevrimdışı çalışıyor mu?", "Evet. Metin tanıma, Apple'ın Vision çerçevesiyle cihazda, internetsiz çalışır. Tanınan metin kopyalanabilir, aranabilir ve Word belgesi (.docx) olarak dışa aktarılabilir."),
          ("PDF On Word, Excel ya da PowerPoint dosyalarını PDF'e dönüştürebilir mi?", "Evet. Bir Word, Excel, PowerPoint, Pages, Numbers, Keynote, metin ya da HTML dosyasını PDF On'da aç; cihazda PDF'e dönüşür."),
          ("Hangi iPhone'lar ve diller?", "iOS 17 veya üzeri her iPhone. Uygulama 46 dil konuşur; aralarında Türkçe, İngilizce, Almanca, İspanyolca, Arapça, Farsça, Urduca, Fransızca, İtalyanca, Portekizce, Hintçe, Japonca, Korece ve Çince var; Arapça, Farsça ve Urduca için tam sağdan sola düzen.")],
)

L["ar"] = dict(
    title="PDF On – امسح واملأ ووقّع ملفات PDF على iPhone. مجانًا ودون إنترنت.",
    desc="تطبيق PDF مجاني لـ iPhone: امسح الورق إلى PDF، واملأ أي نموذج (حتى المصوَّر)، ووقّع، وانسخ بطاقة الهوية أو جواز السفر بالحجم الأصلي، وحوّل Word إلى PDF، مع التعرّف على النصوص. بلا حساب وبلا رفع ملفات.",
    nav=("الرئيسية", "الخصوصية", "الدعم"),
    tag="امسح واملأ ووقّع. كل شيء يبقى على iPhone.",
    store="تنزيل من App Store",
    store_note="مجاني · iOS 17 أو أحدث · بلا حساب",
    lead="PDF On ماسح ضوئي ومحرّر PDF مجاني لـ iPhone. يحوّل الورق إلى ملفات PDF نظيفة، ويملأ النماذج (نماذج PDF الحقيقية والمصوَّرة أو الممسوحة)، ويضع توقيعك وصورتك الشخصية، وينسخ بطاقة الهوية أو جواز السفر بوجهيه على ورقة واحدة بالحجم الأصلي، ويحوّل ملفات Word وExcel وPowerPoint إلى PDF، ويتعرّف على النصوص دون إنترنت، ويتيح لك التظليل أثناء القراءة. بلا حساب، وبلا رفع ملفات، وبلا إعلانات، وبلا اشتراك.",
    problems_h2="متى يفيدك PDF On",
    problems=["وصلك نموذج بصيغة PDF أو على ورق، وعليك ملؤه وتوقيعه وإعادته اليوم من هاتفك.",
              "يطلب المؤجّر أو البنك أو صاحب العمل نسخة من بطاقة الهوية أو جواز السفر بوجهيه، وينبغي أن تبدو كنسخة مصوّرة حقيقية.",
              "تحتاج إلى إرسال عقد موقّع أو طلب توظيف بصورتك أو إيصال ممسوح، كملف PDF واحد نظيف باسم ملف مناسب.",
              "تريد قراءة ملف PDF طويل وتظليل السطور المهمة والحصول على كل تظليلاتك في قائمة.",
              "لا تريد تطبيق مسح يتطلب حسابًا أو اشتراكًا أو يرفع مستنداتك إلى سحابة أحدهم."],
    features_h2="ما الذي يستطيعه PDF On",
    features=[("📄", "المسح وإنشاء PDF", "امسح المستندات مع اكتشاف تلقائي للحواف، أو التقط صورة ودع الحواف تُكتشف وتُعدَّل استقامتها. أنشئ ملفات PDF من الصور والملفات وملفات PDF أخرى؛ اختر حجم الصفحة والترتيب (1 أو 2 أو 4 في الصفحة) والجودة؛ أضف أختام التاريخ والوقت؛ واحمِ الملف بكلمة مرور."),
              ("✏️", "تعبئة أي نموذج", "انقر على الحقل واكتب: يستقر النص داخل الخانة على السطر. زر الإدخال ينتقل إلى الحقل التالي، وعلامات الاختيار تستقر في المربعات، والتواريخ تتبع تنسيق النموذج. يعمل مع نماذج PDF الحقيقية ومع النماذج المصوَّرة أو الممسوحة. يظهر اسمك وعنوانك وهاتفك كاقتراحات فوق لوحة المفاتيح (الإعدادات › بياناتي)."),
              ("✍️", "التوقيع وإضافة صورتك", "وقّع بإصبعك أو صوّر توقيعك على الورق؛ يستقر فوق سطر التوقيع. وتوضع الصورة الشخصية في إطار الصورة في نموذج الطلب، الذي يُكتشف تلقائيًا."),
              ("🪪", "نسخة بطاقة الهوية وجواز السفر", "الوجه والظهر على ورقة واحدة بالحجم الأصلي، مع تكبير اختياري، بالألوان أو بتدرّج الرمادي، مع خطوط قص وعلامة مائية مثل «نسخة للمؤجّر»."),
              ("🔍", "التعرّف على النصوص دون إنترنت", "التعرّف على النصوص على الجهاز يجعل الملفات الممسوحة قابلة للبحث. انسخ النص، أو ابحث داخل المستند، أو صدّره كمستند Word ‏(.docx)."),
              ("🖍️", "القراءة والتظليل", "وضع قراءة بملء الشاشة مع اقتصاص الهوامش. ظلّل بسحبة واحدة بأربعة ألوان، وسمِّ ألوانك، وأضف ملاحظات، وانتقل إلى أي تظليل من القائمة، وشاركها كنص. يتذكر التطبيق أين توقفت."),
              ("📑", "إدارة الصفحات", "أعد ترتيب الصفحات ودوّرها وقصّها وعدّل استقامتها واحذفها. ادمج ملفات PDF، وأدرج مسحًا أو صورًا أو ملفات PDF أخرى. حوّل ملفات Word وExcel وPowerPoint وPages وNumbers وKeynote والنصوص وHTML إلى PDF."),
              ("🔒", "خصوصية من الأساس", "يعمل بالكامل دون إنترنت. بلا حساب، وبلا إعلانات، وبلا تتبّع، وبلا جمع بيانات. قفل اختياري للتطبيق بـ Face ID. ملحق المشاركة: أرسل الصور وملفات PDF من التطبيقات الأخرى إلى PDF On.")],
    shots_h2="لقطات الشاشة",
    shots={"form": "تعبئة نموذج مصوَّر: يستقر النص داخل الخانات", "reading": "وضع القراءة مع التظليلات",
           "id": "نسخة بطاقة الهوية وجواز السفر بالحجم الأصلي", "home": "البداية: مسح ضوئي، الصور، الكاميرا، ملف",
           "highlights": "قائمة كل التظليلات", "library": "المكتبة بكل ملفات PDF", "pages": "إدارة الصفحات: ترتيب وقص ودمج"},
    how_h2="كيف يعمل",
    steps=[("التقط", "امسح مستندًا، أو اختر صورًا، أو افتح ملف PDF أو Word."),
           ("املأ ووقّع", "انقر واكتب وضع علامات الاختيار ووقّع. بياناتك على بُعد نقرة فوق لوحة المفاتيح."),
           ("شارك", "AirDrop أو البريد أو WhatsApp أو أي تطبيق، باسم ملف مناسب. تبقى ملفات PDF في المكتبة على iPhone.")],
    privacy_h3="الخصوصية في جملة واحدة",
    privacy_text="بلا حساب، وبلا خادم خاص بنا، وبلا إعلانات. كل شيء، بما فيه التعرّف على النصوص، يُحسب ويُخزَّن على iPhone؛ ولا يغادر المستند الهاتف إلا عندما تشاركه بنفسك.",
    privacy_link="اقرأ سياسة الخصوصية",
    faq_h2="أسئلة شائعة",
    faqs=[("هل PDF On مجاني؟", "نعم. PDF On مجاني، بلا إعلانات، وبلا حساب، وبلا اشتراك."),
          ("هل يمكنني تعبئة نموذج PDF بلا حقول حقيقية، مثل نموذج ممسوح أو مصوَّر؟", "نعم. انقر على الخانة في الصفحة واكتب؛ يوضع النص داخل الخانة على السطر. زر الإدخال ينتقل إلى الخانة التالية، وعلامات الاختيار تستقر في المربعات. نماذج PDF الحقيقية ذات الحقول تعمل أيضًا."),
          ("كيف أنسخ بطاقة الهوية أو جواز السفر بوجهيه على صفحة واحدة بـ iPhone؟", "افتح PDF On › بطاقة الهوية وجواز السفر، وصوّر الوجه والظهر. يضع PDF On كليهما على ورقة A4 أو Letter بالحجم الأصلي، مع تكبير اختياري، بالألوان أو بتدرّج الرمادي، مع خطوط قص وعلامة مائية اختيارية مثل «نسخة للمؤجّر»."),
          ("كيف أوقّع ملف PDF على iPhone؟", "افتح ملف PDF في PDF On، وانقر على تعديل واختر توقيع. ارسمه بإصبعك أو صوّر توقيعك على الورق؛ تُزال الخلفية ويستقر التوقيع فوق سطر التوقيع. يمكن إعادة استخدام التوقيعات المحفوظة."),
          ("هل تُرفع مستنداتي إلى أي مكان؟", "لا. ليس لدى PDF On خادم. المسح والتعرّف على النصوص واكتشاف الوجوه والإطارات تعمل على iPhone. لا يغادر المستند الهاتف إلا عندما تشاركه بنفسك، مثلًا عبر AirDrop أو البريد أو WhatsApp."),
          ("هل يوفّر PDF On التعرّف على النصوص (OCR) وهل يعمل دون إنترنت؟", "نعم. يعمل التعرّف على النصوص على الجهاز بإطار Vision من Apple، دون إنترنت. يمكن نسخ النص المتعرَّف عليه والبحث فيه وتصديره كمستند Word ‏(.docx)."),
          ("هل يحوّل PDF On ملفات Word أو Excel أو PowerPoint إلى PDF؟", "نعم. افتح ملف Word أو Excel أو PowerPoint أو Pages أو Numbers أو Keynote أو نصًا أو HTML في PDF On فيتحوّل إلى PDF على الجهاز."),
          ("أي أجهزة iPhone وأي لغات؟", "كل iPhone بنظام iOS 17 أو أحدث. يتحدث التطبيق 46 لغة، منها العربية والإنجليزية والألمانية والإسبانية والتركية والفارسية والأردية والفرنسية والإيطالية والبرتغالية والهندية واليابانية والكورية والصينية، مع تخطيط كامل من اليمين إلى اليسار للعربية والفارسية والأردية.")],
)

L["fa"] = dict(
    title="PDF On – اسکن، پر کردن و امضای PDF روی iPhone. رایگان و آفلاین.",
    desc="برنامهٔ رایگان PDF برای iPhone: کاغذ را به PDF اسکن کنید، هر فرمی را پر کنید (حتی عکس‌گرفته‌شده)، امضا کنید، کارت شناسایی یا گذرنامه را در اندازهٔ اصلی کپی کنید، Word را به PDF تبدیل کنید، تشخیص متن. بدون حساب، بدون آپلود.",
    nav=("شروع", "حریم خصوصی", "پشتیبانی"),
    tag="اسکن کنید، پر کنید، امضا کنید. همه‌چیز روی iPhone شما می‌ماند.",
    store="دانلود از App Store",
    store_note="رایگان · iOS 17 یا جدیدتر · بدون حساب",
    lead="PDF On یک اسکنر و ویرایشگر رایگان PDF برای iPhone است. کاغذ را به PDFهای تمیز تبدیل می‌کند، فرم‌ها را پر می‌کند (فرم‌های واقعی PDF و فرم‌های عکس‌گرفته‌شده یا اسکن‌شده)، امضا و عکس پرسنلی شما را جای می‌دهد، کارت شناسایی یا گذرنامه را با هر دو رو در یک برگ و در اندازهٔ اصلی کپی می‌کند، فایل‌های Word و Excel و PowerPoint را به PDF تبدیل می‌کند، متن را آفلاین تشخیص می‌دهد و هنگام خواندن هایلایت می‌کند. بدون حساب، بدون آپلود، بدون تبلیغ، بدون اشتراک.",
    problems_h2="PDF On چه زمانی کمک می‌کند",
    problems=["فرمی به‌صورت PDF یا روی کاغذ دریافت کرده‌اید و باید همین امروز آن را از گوشی پر کنید، امضا کنید و برگردانید.",
              "صاحب‌خانه، بانک یا کارفرما کپی کارت شناسایی یا گذرنامهٔ شما را با هر دو رو می‌خواهد و باید مثل یک فتوکپی واقعی به نظر برسد.",
              "باید قراردادی امضاشده، درخواست شغلی با عکس یا رسیدی اسکن‌شده را به‌صورت یک PDF تمیز با نام فایل مناسب بفرستید.",
              "می‌خواهید یک PDF طولانی را بخوانید، خط‌های مهم را هایلایت کنید و همهٔ هایلایت‌ها را در یک فهرست داشته باشید.",
              "برنامهٔ اسکنری نمی‌خواهید که حساب یا اشتراک بخواهد یا اسناد شما را به ابر کسی آپلود کند."],
    features_h2="PDF On چه می‌تواند بکند",
    features=[("📄", "اسکن و ساخت PDF", "اسناد را با تشخیص خودکار لبه‌ها اسکن کنید یا عکس بگیرید تا لبه‌ها پیدا و صاف شوند. از عکس‌ها، فایل‌ها و PDFهای دیگر PDF بسازید؛ اندازهٔ صفحه، چیدمان (۱، ۲ یا ۴ در هر صفحه) و کیفیت را انتخاب کنید؛ مُهر تاریخ و ساعت بزنید؛ با گذرواژه محافظت کنید."),
              ("✏️", "پر کردن هر فرمی", "روی فیلد بزنید و بنویسید: متن داخل کادر و روی خط می‌نشیند. کلید Return به فیلد بعدی می‌رود، تیک‌ها در چک‌باکس‌ها جا می‌گیرند، تاریخ‌ها از قالب فرم پیروی می‌کنند. با فرم‌های واقعی PDF و با فرم‌های عکس‌گرفته‌شده یا اسکن‌شده کار می‌کند. نام، نشانی و تلفن شما به‌صورت پیشنهاد بالای صفحه‌کلید ظاهر می‌شود (تنظیمات › اطلاعات من)."),
              ("✍️", "امضا و افزودن عکس", "با انگشت امضا کنید یا از امضای خود روی کاغذ عکس بگیرید؛ روی خط امضا قرار می‌گیرد. عکس پرسنلی در کادر عکسِ فرم درخواست می‌نشیند که خودکار پیدا می‌شود."),
              ("🪪", "کپی کارت شناسایی و گذرنامه", "رو و پشت در یک برگ در اندازهٔ اصلی، با بزرگ‌نمایی اختیاری، رنگی یا خاکستری، با خطوط برش و واترمارکی مانند «کپی برای صاحب‌خانه»."),
              ("🔍", "تشخیص متن، آفلاین", "تشخیص متن روی دستگاه، اسکن‌ها را قابل جستجو می‌کند. متن را کپی کنید، در سند جستجو کنید یا آن را به‌صورت سند Word ‏(.docx) خروجی بگیرید."),
              ("🖍️", "خواندن و هایلایت", "حالت خواندن تمام‌صفحه با حاشیه‌های بریده‌شده. با یک کشیدن در چهار رنگ هایلایت کنید، به رنگ‌ها نام بدهید، یادداشت بیفزایید، از فهرست به هر هایلایت بپرید و آن‌ها را به‌صورت متن به اشتراک بگذارید. برنامه جایی را که متوقف شدید به یاد می‌آورد."),
              ("📑", "مدیریت صفحه‌ها", "صفحه‌ها را مرتب، بچرخانید، برش دهید، صاف کنید و حذف کنید. PDFها را ادغام کنید، اسکن، عکس یا PDFهای دیگر را درج کنید. فایل‌های Word، Excel، PowerPoint، Pages، Numbers، Keynote، متن و HTML را به PDF تبدیل کنید."),
              ("🔒", "خصوصی از پایه", "کاملاً آفلاین کار می‌کند. بدون حساب، بدون تبلیغ، بدون ردیابی، بدون جمع‌آوری داده. قفل اختیاری برنامه با Face ID. افزونهٔ اشتراک‌گذاری: عکس‌ها و PDFها را از برنامه‌های دیگر به PDF On بفرستید.")],
    shots_h2="تصاویر برنامه",
    shots={"form": "پر کردن فرم عکس‌گرفته‌شده: متن داخل کادرها می‌نشیند", "reading": "حالت خواندن با هایلایت‌ها",
           "id": "کپی کارت شناسایی و گذرنامه در اندازهٔ اصلی", "home": "شروع: اسکن، عکس‌ها، دوربین، فایل",
           "highlights": "فهرست همهٔ هایلایت‌ها", "library": "کتابخانه با همهٔ PDFها", "pages": "مدیریت صفحه‌ها: مرتب‌سازی، برش، ادغام"},
    how_h2="چطور کار می‌کند",
    steps=[("بگیرید", "سندی را اسکن کنید، عکس انتخاب کنید یا یک فایل PDF یا Word باز کنید."),
           ("پر کنید و امضا کنید", "بزنید، بنویسید، تیک بزنید، امضا کنید. اطلاعات شما با یک ضربه بالای صفحه‌کلید آماده است."),
           ("به اشتراک بگذارید", "AirDrop، ایمیل، WhatsApp یا هر برنامه‌ای، با نام فایل درست. PDFهای شما در کتابخانه روی iPhone می‌مانند.")],
    privacy_h3="حریم خصوصی در یک جمله",
    privacy_text="بدون حساب، بدون سرورِ ما، بدون تبلیغ. همه‌چیز، از جمله تشخیص متن، روی iPhone شما محاسبه و ذخیره می‌شود؛ سند فقط وقتی از گوشی خارج می‌شود که خودتان آن را به اشتراک بگذارید.",
    privacy_link="خواندن سیاست حریم خصوصی",
    faq_h2="پرسش‌های متداول",
    faqs=[("آیا PDF On رایگان است؟", "بله. PDF On رایگان است، بدون تبلیغ، بدون حساب و بدون اشتراک."),
          ("آیا می‌توانم فرم PDF بدون فیلد واقعی، مثلاً فرم اسکن‌شده یا عکس‌گرفته‌شده را پر کنم؟", "بله. روی کادر در صفحه بزنید و بنویسید؛ متن داخل کادر و روی خط قرار می‌گیرد. Return به کادر بعدی می‌رود و تیک‌ها در چک‌باکس‌ها جا می‌گیرند. فرم‌های واقعی PDF با فیلد هم کار می‌کنند."),
          ("چطور کارت شناسایی یا گذرنامه را با هر دو رو در یک صفحه با iPhone کپی کنم؟", "PDF On › کارت شناسایی و گذرنامه را باز کنید و از رو و پشت عکس بگیرید. PDF On هر دو را روی یک برگ A4 یا Letter در اندازهٔ اصلی می‌گذارد، با بزرگ‌نمایی اختیاری، رنگی یا خاکستری، با خطوط برش و واترمارک اختیاری مانند «کپی برای صاحب‌خانه»."),
          ("چطور یک PDF را روی iPhone امضا کنم؟", "PDF را در PDF On باز کنید، روی ویرایش بزنید و امضا را انتخاب کنید. با انگشت بکشید یا از امضای خود روی کاغذ عکس بگیرید؛ پس‌زمینه حذف می‌شود و امضا روی خط امضا می‌نشیند. امضاهای ذخیره‌شده قابل استفادهٔ مجددند."),
          ("آیا اسناد من جایی آپلود می‌شوند؟", "نه. PDF On سرور ندارد. اسکن، تشخیص متن و تشخیص چهره و کادر روی iPhone اجرا می‌شوند. سند فقط وقتی از گوشی خارج می‌شود که خودتان آن را به اشتراک بگذارید، مثلاً با AirDrop، ایمیل یا WhatsApp."),
          ("آیا PDF On تشخیص متن (OCR) دارد و آفلاین کار می‌کند؟", "بله. تشخیص متن با چارچوب Vision اپل روی دستگاه و بدون اینترنت اجرا می‌شود. متن تشخیص‌داده‌شده را می‌توان کپی کرد، جستجو کرد و به‌صورت سند Word ‏(.docx) خروجی گرفت."),
          ("آیا PDF On فایل‌های Word، Excel یا PowerPoint را به PDF تبدیل می‌کند؟", "بله. یک فایل Word، Excel، PowerPoint، Pages، Numbers، Keynote، متن یا HTML را در PDF On باز کنید تا روی دستگاه به PDF تبدیل شود."),
          ("کدام iPhoneها و زبان‌ها؟", "هر iPhone با iOS 17 یا جدیدتر. برنامه ۴۶ زبان دارد، از جمله فارسی، انگلیسی، آلمانی، اسپانیایی، ترکی، عربی، اردو، فرانسوی، ایتالیایی، پرتغالی، هندی، ژاپنی، کره‌ای و چینی، با چیدمان کامل راست‌به‌چپ برای فارسی، عربی و اردو.")],
)

L["ur"] = dict(
    title="PDF On – iPhone پر PDF اسکین کریں، پُر کریں اور دستخط کریں۔ مفت، آف لائن۔",
    desc="iPhone کے لیے مفت PDF ایپ: کاغذ کو PDF میں اسکین کریں، کوئی بھی فارم پُر کریں (تصویر والا بھی)، دستخط کریں، شناختی کارڈ یا پاسپورٹ اصل سائز میں کاپی کریں، Word کو PDF بنائیں، متن کی شناخت۔ نہ اکاؤنٹ، نہ اپ لوڈ۔",
    nav=("ہوم", "پرائیویسی", "سپورٹ"),
    tag="اسکین کریں، پُر کریں، دستخط کریں۔ سب کچھ آپ کے iPhone پر رہتا ہے۔",
    store="App Store سے ڈاؤن لوڈ کریں",
    store_note="مفت · iOS 17 یا نیا · اکاؤنٹ کے بغیر",
    lead="PDF On iPhone کے لیے ایک مفت PDF اسکینر اور ایڈیٹر ہے۔ یہ کاغذ کو صاف PDF میں بدلتا ہے، فارم پُر کرتا ہے (اصل PDF فارم اور تصویر یا اسکین والے فارم بھی)، آپ کے دستخط اور پاسپورٹ سائز تصویر لگاتا ہے، شناختی کارڈ یا پاسپورٹ کے دونوں رخ ایک صفحے پر اصل سائز میں کاپی کرتا ہے، Word، Excel اور PowerPoint فائلوں کو PDF میں بدلتا ہے، آف لائن متن پہچانتا ہے اور پڑھتے وقت ہائی لائٹ کرنے دیتا ہے۔ نہ اکاؤنٹ، نہ اپ لوڈ، نہ اشتہار، نہ سبسکرپشن۔",
    problems_h2="PDF On کب کام آتا ہے",
    problems=["آپ کو PDF یا کاغذ پر فارم ملا ہے اور آج ہی فون سے پُر کر کے، دستخط کر کے واپس بھیجنا ہے۔",
              "مالک مکان، بینک یا آجر آپ کے شناختی کارڈ یا پاسپورٹ کے دونوں رخ کی کاپی مانگتے ہیں اور وہ اصل فوٹو کاپی جیسی لگنی چاہیے۔",
              "آپ کو دستخط شدہ معاہدہ، تصویر والی ملازمت کی درخواست یا اسکین شدہ رسید، مناسب فائل نام کے ساتھ ایک صاف PDF کے طور پر بھیجنی ہے۔",
              "آپ لمبی PDF پڑھ کر اہم سطریں نشان زد کرنا اور ساری نشانیاں ایک فہرست میں لینا چاہتے ہیں۔",
              "آپ ایسی اسکینر ایپ نہیں چاہتے جو اکاؤنٹ یا سبسکرپشن مانگے یا آپ کی دستاویزات کسی کے کلاؤڈ پر اپ لوڈ کرے۔"],
    features_h2="PDF On کیا کر سکتا ہے",
    features=[("📄", "اسکین اور PDF بنائیں", "کناروں کی خودکار شناخت کے ساتھ دستاویزات اسکین کریں، یا تصویر لیں اور کنارے خود بخود ملیں اور سیدھے ہوں۔ تصاویر، فائلوں اور دوسری PDF سے PDF بنائیں؛ صفحے کا سائز، ترتیب (فی صفحہ 1، 2 یا 4) اور معیار چنیں؛ تاریخ اور وقت کی مہر لگائیں؛ پاس ورڈ سے محفوظ کریں۔"),
              ("✏️", "کوئی بھی فارم پُر کریں", "خانے پر ٹیپ کریں اور لکھیں: متن خانے کے اندر، لکیر پر بیٹھتا ہے۔ Return اگلے خانے میں لے جاتا ہے، ٹک چیک باکس میں بیٹھتے ہیں، تاریخیں فارم کے فارمیٹ کے مطابق ہوتی ہیں۔ اصل PDF فارم اور تصویر یا اسکین والے فارم دونوں کے ساتھ کام کرتا ہے۔ آپ کا نام، پتہ اور فون کی بورڈ کے اوپر تجاویز کے طور پر آتے ہیں (ترتیبات › میری معلومات)۔"),
              ("✍️", "دستخط اور اپنی تصویر", "انگلی سے دستخط کریں یا کاغذ پر اپنے دستخط کی تصویر لیں؛ وہ دستخط کی لکیر پر بیٹھ جاتے ہیں۔ پاسپورٹ سائز تصویر درخواست فارم کے تصویر والے خانے میں جاتی ہے جو خود بخود مل جاتا ہے۔"),
              ("🪪", "شناختی کارڈ و پاسپورٹ کی کاپی", "سامنے اور پیچھے ایک صفحے پر اصل سائز میں، اختیاری بڑا سائز، رنگین یا گرے اسکیل، کٹنگ لائنوں اور ”مالک مکان کے لیے کاپی“ جیسے واٹر مارک کے ساتھ۔"),
              ("🔍", "متن کی شناخت، آف لائن", "ڈیوائس پر متن کی شناخت اسکین کو قابلِ تلاش بناتی ہے۔ متن کاپی کریں، دستاویز میں تلاش کریں یا Word دستاویز (.docx) کے طور پر ایکسپورٹ کریں۔"),
              ("🖍️", "پڑھیں اور ہائی لائٹ کریں", "کٹے حاشیوں کے ساتھ فل اسکرین پڑھنے کا موڈ۔ ایک سوائپ سے چار رنگوں میں ہائی لائٹ کریں، رنگوں کو نام دیں، نوٹ لکھیں، فہرست سے کسی بھی نشانی پر جائیں اور انہیں متن کے طور پر شیئر کریں۔ ایپ یاد رکھتی ہے کہ آپ کہاں رکے تھے۔"),
              ("📑", "صفحات سنبھالیں", "صفحات کی ترتیب بدلیں، گھمائیں، کاٹیں، سیدھا کریں اور حذف کریں۔ PDF ضم کریں، اسکین، تصاویر یا دوسری PDF شامل کریں۔ Word، Excel، PowerPoint، Pages، Numbers، Keynote، متن اور HTML فائلوں کو PDF میں بدلیں۔"),
              ("🔒", "بنیادی طور پر نجی", "مکمل آف لائن کام کرتا ہے۔ نہ اکاؤنٹ، نہ اشتہار، نہ ٹریکنگ، نہ ڈیٹا اکٹھا کرنا۔ Face ID سے اختیاری ایپ لاک۔ شیئر ایکسٹینشن: دوسری ایپس سے تصاویر اور PDF PDF On کو بھیجیں۔")],
    shots_h2="اسکرین شاٹس",
    shots={"form": "تصویر والا فارم پُر کرنا: متن خانوں کے اندر بیٹھتا ہے", "reading": "نشانیوں کے ساتھ پڑھنے کا موڈ",
           "id": "اصل سائز میں شناختی کارڈ و پاسپورٹ کی کاپی", "home": "ہوم: اسکین، تصاویر، کیمرہ، فائل",
           "highlights": "ساری نشانیوں کی فہرست", "library": "ساری PDF کے ساتھ لائبریری", "pages": "صفحات سنبھالیں: ترتیب، کاٹنا، ضم کرنا"},
    how_h2="یہ کیسے کام کرتا ہے",
    steps=[("لیں", "دستاویز اسکین کریں، تصاویر چنیں یا PDF یا Word فائل کھولیں۔"),
           ("پُر کریں اور دستخط کریں", "ٹیپ کریں، لکھیں، ٹک لگائیں، دستخط کریں۔ آپ کی معلومات کی بورڈ کے اوپر ایک ٹیپ پر تیار ہیں۔"),
           ("شیئر کریں", "AirDrop، میل، WhatsApp یا کوئی بھی ایپ، درست فائل نام کے ساتھ۔ آپ کی PDF آپ کے iPhone کی لائبریری میں رہتی ہیں۔")],
    privacy_h3="ایک جملے میں پرائیویسی",
    privacy_text="نہ اکاؤنٹ، نہ ہمارا کوئی سرور، نہ اشتہار۔ سب کچھ، متن کی شناخت سمیت، آپ کے iPhone پر ہوتا اور محفوظ رہتا ہے؛ دستاویز فون سے صرف تب نکلتی ہے جب آپ خود شیئر کریں۔",
    privacy_link="پرائیویسی پالیسی پڑھیں",
    faq_h2="اکثر پوچھے گئے سوالات",
    faqs=[("کیا PDF On مفت ہے؟", "جی ہاں۔ PDF On مفت ہے، بغیر اشتہار، بغیر اکاؤنٹ اور بغیر سبسکرپشن۔"),
          ("کیا میں ایسا PDF فارم پُر کر سکتا ہوں جس میں اصل خانے نہ ہوں، مثلاً اسکین یا تصویر والا فارم؟", "جی ہاں۔ صفحے پر خانے کو ٹیپ کریں اور لکھیں؛ متن خانے کے اندر لکیر پر رکھا جاتا ہے۔ Return اگلے خانے میں لے جاتا ہے اور ٹک چیک باکس میں بیٹھتے ہیں۔ خانوں والے اصل PDF فارم بھی کام کرتے ہیں۔"),
          ("iPhone سے شناختی کارڈ یا پاسپورٹ کے دونوں رخ ایک صفحے پر کیسے کاپی کروں؟", "PDF On › شناختی کارڈ و پاسپورٹ کھولیں، سامنے اور پیچھے کی تصویر لیں۔ PDF On دونوں کو A4 یا Letter صفحے پر اصل سائز میں رکھتا ہے، اختیاری بڑا سائز، رنگین یا گرے اسکیل، کٹنگ لائنوں اور ”مالک مکان کے لیے کاپی“ جیسے اختیاری واٹر مارک کے ساتھ۔"),
          ("iPhone پر PDF پر دستخط کیسے کروں؟", "PDF کو PDF On میں کھولیں، ترمیم کریں پر ٹیپ کریں اور دستخط چنیں۔ انگلی سے بنائیں یا کاغذ پر اپنے دستخط کی تصویر لیں؛ پس منظر ہٹ جاتا ہے اور دستخط لکیر پر بیٹھ جاتے ہیں۔ محفوظ دستخط دوبارہ استعمال ہو سکتے ہیں۔"),
          ("کیا میری دستاویزات کہیں اپ لوڈ ہوتی ہیں؟", "نہیں۔ PDF On کا کوئی سرور نہیں۔ اسکین، متن کی شناخت اور چہرے و خانے کی شناخت iPhone پر چلتی ہے۔ دستاویز فون سے صرف تب نکلتی ہے جب آپ خود شیئر کریں، مثلاً AirDrop، میل یا WhatsApp سے۔"),
          ("کیا PDF On میں OCR ہے اور کیا یہ آف لائن کام کرتا ہے؟", "جی ہاں۔ متن کی شناخت Apple کے Vision فریم ورک سے ڈیوائس پر، انٹرنیٹ کے بغیر چلتی ہے۔ پہچانا گیا متن کاپی، تلاش اور Word دستاویز (.docx) کے طور پر ایکسپورٹ کیا جا سکتا ہے۔"),
          ("کیا PDF On Word، Excel یا PowerPoint فائلوں کو PDF میں بدل سکتا ہے؟", "جی ہاں۔ Word، Excel، PowerPoint، Pages، Numbers، Keynote، متن یا HTML فائل PDF On میں کھولیں اور وہ ڈیوائس پر PDF بن جاتی ہے۔"),
          ("کون سے iPhone اور زبانیں؟", "iOS 17 یا نئے والا ہر iPhone۔ ایپ 46 زبانیں بولتی ہے، جن میں اردو، انگریزی، جرمن، ہسپانوی، ترکی، عربی، فارسی، فرانسیسی، اطالوی، پرتگالی، ہندی، جاپانی، کوریائی اور چینی شامل ہیں؛ اردو، عربی اور فارسی کے لیے مکمل دائیں سے بائیں لے آؤٹ۔")],
)

# ---------------------------------------------------------------- helpers ------------------------------------------------------------
e = html.escape


def url_of(path):
    return SITE + path


def store_url(storefront):
    return f"https://apps.apple.com/{storefront}/app/pdf-on/id{APP_ID}" if storefront else STORE


def hreflang_links():
    links = [f'<link rel="alternate" hreflang="{c}" href="{url_of(p)}">' for c, _, _, _, p, _ in LANGS]
    links.append(f'<link rel="alternate" hreflang="x-default" href="{SITE}">')
    return "".join(links)


def head(lang, direction, title, desc, url, og_locale, extra=""):
    alternates = "".join(f'<meta property="og:locale:alternate" content="{o}">' for c, _, _, o, _, _ in LANGS if o != og_locale)
    verify = f'<meta name="google-site-verification" content="{GOOGLE_VERIFICATION}">' if GOOGLE_VERIFICATION else ""
    return f'''<!doctype html><html lang="{lang}" dir="{direction}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
{hreflang_links()}
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="apple-itunes-app" content="app-id={APP_ID}">{verify}
<meta property="og:type" content="website"><meta property="og:site_name" content="PDF On"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="PDF On app icon and name"><meta property="og:locale" content="{og_locale}">{alternates}
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(desc)}"><meta name="twitter:image" content="{SITE}og.png">
<link rel="icon" href="{BASE}icon.png"><link rel="apple-touch-icon" href="{BASE}apple-touch-icon.png">
<link rel="stylesheet" href="{BASE}style.css?v=5">
{extra}</head>'''


def lang_switch(current, target):
    """target: 'landing' links to the language pages, 'privacy' to the sections of privacy.html."""
    items = []
    for c, name, _, _, p, _ in LANGS:
        href = url_of(p) if target == "landing" else f"{BASE}privacy.html#{c}"
        cls = ' class="on"' if c == current else ""
        data = "" if target == "landing" else f' data-lang="{c}"'
        items.append(f'<a href="{href}" lang="{c}" hreflang="{c}"{cls}{data}>{name}</a>')
    return '<div class="langs">' + "".join(items) + "</div>"


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "</script>"


def landing(code):
    t = L[code]
    _, name, direction, og_locale, path, storefront = next(x for x in LANGS if x[0] == code)
    url = url_of(path)
    store = store_url(storefront)
    shot_urls = [f"{SITE}img/{code}/{k}.webp" for k in SHOTS[code]]
    app = {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "PDF On", "url": url, "image": SITE + "og.png",
           "screenshot": shot_urls, "description": t["desc"], "operatingSystem": "iOS 17 or later", "applicationCategory": "BusinessApplication",
           "applicationSubCategory": "PDF scanner, form filler and editor", "softwareVersion": "1.0", "datePublished": "2026-09-28",
           "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD", "url": store},
           "installUrl": store, "downloadUrl": store, "sameAs": [STORE, GITHUB],
           "inLanguage": APP_LANGS, "featureList": [f[1] for f in t["features"]],
           "author": {"@type": "Person", "name": "Abbas Hoseiny", "url": SITE},
           "publisher": {"@type": "Person", "name": "Abbas Hoseiny"}}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faqs"]]}
    nav_start, nav_privacy, nav_support = t["nav"]
    cards = "".join(f'<div class="card"><div class="ico" aria-hidden="true">{i}</div><h3>{e(h)}</h3><p>{e(p)}</p></div>' for i, h, p in t["features"])
    shots = "".join(f'<figure><img src="{BASE}img/{code}/{k}.webp" alt="{e(t["shots"][k])}" width="240" height="521" loading="lazy" decoding="async"><figcaption>{e(t["shots"][k])}</figcaption></figure>' for k in SHOTS[code])
    steps = "".join(f'<div><h3>{e(h)}</h3><p>{e(p)}</p></div>' for h, p in t["steps"])
    problems = "".join(f"<li>{e(p)}</li>" for p in t["problems"])
    faqs = "".join(f'<h3>{e(q)}</h3><p>{e(a)}</p>' for q, a in t["faqs"])
    badge = f'<a class="store" href="{store}" hreflang="{code}"><img src="{BASE}app-store-badge.svg" alt="{e(t["store"])}" width="150" height="50"></a><span class="note">{e(t["store_note"])}</span>'
    body = f'''
<body><main>
<nav><a href="{url}" class="on">{e(nav_start)}</a><a href="{BASE}privacy.html#{code}">{e(nav_privacy)}</a><a href="{BASE}support.html">{e(nav_support)}</a></nav>
{lang_switch(code, "landing")}
<header class="hero"><img src="{BASE}icon.png" alt="PDF On" width="96" height="96"><div><h1>PDF On</h1><p>{e(t["tag"])}</p><div class="cta">{badge}</div></div></header>
<p class="lead">{e(t["lead"])}</p>
<h2>{e(t["problems_h2"])}</h2>
<ul class="problems">{problems}</ul>
<h2>{e(t["features_h2"])}</h2>
<div class="grid">{cards}</div>
<h2>{e(t["shots_h2"])}</h2>
<div class="shots">{shots}</div>
<h2>{e(t["how_h2"])}</h2>
<div class="steps">{steps}</div>
<div class="privacy"><h3>{e(t["privacy_h3"])}</h3><p>{e(t["privacy_text"])} <a href="{BASE}privacy.html#{code}">{e(t["privacy_link"])}</a></p></div>
<h2>{e(t["faq_h2"])}</h2>
<div class="card faq">{faqs}</div>
<div class="cta bottom">{badge}</div>
<footer><span>© 2026 Abbas Hoseiny</span><a href="{BASE}privacy.html#{code}">{e(nav_privacy)}</a><a href="{BASE}support.html">{e(nav_support)}</a><a href="{GITHUB}">GitHub</a></footer>
</main></body></html>
'''
    return head(code, direction, t["title"], t["desc"], url, og_locale, ld(app) + ld(faq)) + body


def support_page():
    title = "PDF On – Support"
    desc = "Support for the iPhone app PDF On: questions, problems and frequently asked questions. Answers in German and English."
    url = SITE + "support.html"
    return head("de", "ltr", title, desc, url, "de_DE") + f'''
<body><main>
<nav><a href="{SITE}">Start</a><a href="{BASE}privacy.html">Datenschutz · Privacy</a><a href="{BASE}support.html" class="on">Support</a></nav>
<div class="hero"><img src="{BASE}icon.png" alt="PDF On" width="96" height="96"><div><h1>Support</h1><p>PDF On für iPhone · PDF On for iPhone</p></div></div>
<div class="card"><h3>Frage oder Problem? · Question or problem?</h3>
<p>Schreib uns, wir antworten so schnell wie möglich. · Write to us, we answer as quickly as we can.</p>
<p><a href="{GITHUB}/issues/new">Nachricht senden · Send a message</a></p></div>
<h2>Häufige Fragen · FAQ</h2>
<div class="card faq">
<p><b>Wo sind meine PDFs?</b><br>In der App unter „Bibliothek“. Sie liegen nur auf deinem iPhone. Mit „Teilen“ schickst du sie überallhin.</p>
<p><b>Where are my PDFs?</b><br>In the app under “Library”. They are stored only on your iPhone. Use “Share” to send them anywhere.</p>
<p><b>Wie fülle ich ein fotografiertes Formular aus?</b><br>Bearbeiten, „Text“ wählen, ins Kästchen tippen, schreiben. Die Eingabetaste springt ins nächste Feld.</p>
<p><b>How do I fill in a photographed form?</b><br>Edit, choose “Text”, tap the box, type. Return jumps to the next field.</p>
<p><b>Wie kopiere ich Ausweis oder Reisepass?</b><br>Start › „Ausweis &amp; Reisepass“, Vorder- und Rückseite fotografieren. Beide landen in Originalgröße auf einem Blatt.</p>
<p><b>How do I copy an ID card or passport?</b><br>Home › “ID card &amp; passport”, photograph front and back. Both land on one sheet in original size.</p>
<p><b>Texterkennung funktioniert nicht?</b><br>Sie läuft auf dem Gerät und braucht iOS 17 oder neuer.</p>
<p><b>Text recognition does not work?</b><br>It runs on the device and needs iOS 17 or later.</p>
<p><b>Wird etwas hochgeladen?</b><br>Nein. PDF On hat keinen Server. Ein Dokument verlässt das iPhone nur, wenn du es selbst teilst.</p>
<p><b>Is anything uploaded?</b><br>No. PDF On has no server. A document leaves the iPhone only when you share it yourself.</p>
</div>
<footer><span>© 2026 Abbas Hoseiny</span><a href="{SITE}">Start</a><a href="{BASE}privacy.html">Datenschutz</a><a href="{STORE}">App Store</a></footer>
</main></body></html>
'''


def sitemap():
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
    alts = "".join(f'<xhtml:link rel="alternate" hreflang="{c}" href="{url_of(p)}"/>' for c, _, _, _, p, _ in LANGS)
    alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE}"/>'
    for c, _, _, _, p, _ in LANGS:
        images = "".join(f"<image:image><image:loc>{SITE}img/{c}/{k}.webp</image:loc></image:image>" for k in SHOTS[c])
        out.append(f"<url><loc>{url_of(p)}</loc><lastmod>{DATE}</lastmod>{alts}{images}</url>")
    for page in ("privacy.html", "support.html"):
        out.append(f"<url><loc>{SITE}{page}</loc><lastmod>{DATE}</lastmod></url>")
    out.append("</urlset>")
    return "\n".join(out) + "\n"


def llms():
    t = L["en"]
    lines = ["# PDF On", "", f"> {t['desc']}", "", t["lead"], "", "## Facts", "",
             f"- App Store: {STORE} (free, iOS 17 or later, released 2026-09-28, available worldwide).",
             "- Developer: Abbas Hoseiny, Germany. No account, no ads, no subscription, no in-app purchases.",
             "- What it does: scans paper with automatic edge detection; builds PDFs from photos, files and other PDFs (1, 2 or 4 per page, date/time stamps, password); "
             "fills in real PDF forms and photographed or scanned forms (text lands in the box, Return jumps to the next field, checkmarks snap into checkboxes, personal details as keyboard suggestions); "
             "signature by finger or photographed from paper, passport photo placed into the form's photo frame; ID card and passport copy front and back on one sheet in true size (color/grayscale, cut lines, watermark); "
             "on-device OCR with copy, search and export to Word (.docx); reading mode with highlights in four named colors, notes and a highlight list; "
             "page management (reorder, rotate, crop, straighten, delete, merge); converts Word, Excel, PowerPoint, Pages, Numbers, Keynote, text and HTML to PDF; Face ID app lock; share extension.",
             "- Privacy: no server, no upload, no tracking, no data collection; everything including OCR runs on the iPhone; a document leaves the phone only when the user shares it.",
             f"- Languages of the app: {len(APP_LANGS)} ({', '.join(APP_LANGS)}); full right-to-left layout for Arabic, Persian and Urdu.",
             "", "## Typical questions this app answers", "",
             "- fill in a PDF form on iPhone for free, including scanned or photographed forms without form fields",
             "- sign a PDF on iPhone with finger or a photographed signature",
             "- copy ID card or passport front and back on one A4 page in original size with iPhone",
             "- scan documents to PDF on iPhone without subscription and without upload",
             "- OCR on iPhone offline, PDF to Word (.docx)",
             "- convert Word, Excel, PowerPoint to PDF on iPhone",
             "- highlight and annotate a PDF while reading, get all highlights as a list",
             "", "## Pages", ""]
    for c, name, _, _, p, _ in LANGS:
        lines.append(f"- [{name}]({url_of(p)}): landing page in {name}")
    lines += [f"- [Privacy policy]({SITE}privacy.html): seven languages on one page (de, en, es, tr, ar, fa, ur)",
              f"- [Support]({SITE}support.html): questions via GitHub Issues", "", "## FAQ", ""]
    for q, a in t["faqs"]:
        lines += [f"**{q}** {a}", ""]
    return "\n".join(lines)


def write(rel, content):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"{rel:24} {len(content.encode()):7d} bytes")


if __name__ == "__main__":
    for c, _, _, _, p, _ in LANGS:
        write(p + "index.html", landing(c))
    write("support.html", support_page())
    write("sitemap.xml", sitemap())
    write("llms.txt", llms())
