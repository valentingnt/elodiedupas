# elodiedupas

Site one-page statique d'Élodie Dupas, en ligne sur https://elodiedupas.fr (Vercel, pas de build).

- `index.html` — la page en français (HTML + CSS + JS inline)
- `en/index.html` — la version anglaise, **générée** : après toute modification de `index.html`, lancer `python3 tools/build-en.py`
- `assets/` — image (AVIF/WebP/JPEG) et polices Computer Modern réduites aux glyphes latins (licence OFL)
- SEO : `robots.txt`, `sitemap.xml`, `llms.txt`, `site.webmanifest`, images de partage `og-fr.png` / `og-en.png`, icônes

Aperçu local : `npx serve .` · Un push sur `main` déploie en production.
