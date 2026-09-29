# PDF On – website

Public site of the iPhone app **PDF On** (App Store: https://apps.apple.com/app/pdf-on/id6812877977), served by GitHub Pages at https://abbas-hoseiny.github.io/pdfgo/.

The HTML is generated: edit the texts in `build.py`, run `python3 build.py`, commit the result. `privacy.html` is hand-written. `og.html` is the source of the Open Graph image `og.png` (render at 1200×900 headless and crop to 1200×630). Screenshots in `img/<lang>/` come from the App Store screenshots of the app repo (480 px wide WebP).

Pages: landing page per language (`/`, `/de/`, `/es/`, `/tr/`, `/ar/`, `/fa/`, `/ur/`), `privacy.html` (seven languages), `support.html`, `sitemap.xml`, `llms.txt`.

To move to an own domain: set `SITE`/`BASE` in `build.py`, add a `CNAME` file, rebuild, and update the marketing/support/privacy URLs in App Store Connect and in the app.
