#!/usr/bin/env python3
"""Génère en/index.html (version anglaise) à partir de index.html.

À relancer après chaque modification de index.html :
    python3 tools/build-en.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "index.html"
DST = ROOT / "en" / "index.html"

TITLE_FR = "Élodie Dupas · Doctorante en économie du développement"
TITLE_EN = "Élodie Dupas · PhD Candidate in Development Economics"

# (français, anglais) — chaque chaîne doit exister dans index.html
PAIRS = [
    ('<html lang="fr">', '<html lang="en">'),
    (TITLE_FR, TITLE_EN),
    ('content="Élodie Dupas, doctorante en économie du développement à la Bordeaux School of Economics. Recherches sur les politiques de protection sociale en Afrique."',
     'content="Élodie Dupas, PhD candidate in development economics at the Bordeaux School of Economics. Research on social protection policies in Africa."'),
    ('<link rel="canonical" href="https://elodiedupas.fr/">', '<link rel="canonical" href="https://elodiedupas.fr/en">'),
    ('content="Doctorante à la Bordeaux School of Economics. Recherches sur les politiques de protection sociale en Afrique."',
     'content="PhD candidate at the Bordeaux School of Economics. Research on social protection policies in Africa."'),
    ('<meta property="og:url" content="https://elodiedupas.fr/">', '<meta property="og:url" content="https://elodiedupas.fr/en">'),
    ('<meta property="og:locale" content="fr_FR">\n  <meta property="og:locale:alternate" content="en_GB">',
     '<meta property="og:locale" content="en_GB">\n  <meta property="og:locale:alternate" content="fr_FR">'),
    ('https://elodiedupas.fr/og-fr.png', 'https://elodiedupas.fr/og-en.png'),
    ('content="Élodie Dupas, doctorante en économie du développement, Bordeaux School of Economics"',
     'content="Élodie Dupas, PhD candidate in development economics, Bordeaux School of Economics"'),
    # JSON-LD
    ('"@id": "https://elodiedupas.fr/#profilepage",\n        "url": "https://elodiedupas.fr/",',
     '"@id": "https://elodiedupas.fr/en#profilepage",\n        "url": "https://elodiedupas.fr/en",'),
    ('"inLanguage": "fr",', '"inLanguage": "en",'),
    ('"jobTitle": "Doctorante en économie du développement"', '"jobTitle": "PhD Candidate in Development Economics"'),
    ('"knowsAbout": ["Économie du développement", "Protection sociale", "Évaluation des politiques publiques", "Afrique"]',
     '"knowsAbout": ["Development economics", "Social protection", "Public policy evaluation", "Africa"]'),
    # Contenu visible
    ('Doctorante en économie du développement · <abbr', 'PhD candidate in development economics · <abbr'),
    ('aria-label="Copier l\'adresse e-mail"', 'aria-label="Copy email address"'),
    ('aria-label="Me contacter : dupas.elodie@outlook.com"', 'aria-label="Contact me: dupas.elodie@outlook.com"'),
    ('<span class="t1">Me contacter</span>', '<span class="t1">Contact me</span>'),
    ('<p class="caption">Approvisionnement, étude de terrain.</p>', '<p class="caption">Supply chain, a field study.</p>'),
    ('alt="Un teckel en lunettes de soleil, debout sur un jerrican, qui fait le plein à la pompe."',
     'alt="A dachshund in sunglasses, standing on a jerrycan, filling up at a petrol pump."'),
    ('<p class="label muted">§ 0 Thèse</p>', '<p class="label muted">§ 0 Thesis</p>'),
    ('<p class="caption">Politiques de protection sociale en Afrique.</p>', '<p class="caption">Social protection policies in Africa.</p>'),
    ('<span>Page en cours de remplissage</span>', '<span>Page filling up</span>'),
    ('<a class="lang" href="/en" hreflang="en" lang="en">English</a>', '<a class="lang" href="/" hreflang="fr" lang="fr">Français</a>'),
    ('<span class="label muted mid">Composé en Computer Modern</span>', '<span class="label muted mid">Typeset in Computer Modern</span>'),
    ('<span>Écrire un e-mail</span>', '<span>Write an email</span>'),
    ('<span class="txt"><span>Copier l\'adresse</span><span>Adresse copiée</span></span>', '<span class="txt"><span>Copy address</span><span>Address copied</span></span>'),
    ('data-close>Fermer</button>', 'data-close>Close</button>'),
    ('announce("Adresse e-mail copiée");', 'announce("Email address copied");'),
]


def main():
    html = SRC.read_text(encoding="utf-8")
    for fr, en in PAIRS:
        if fr not in html:
            raise SystemExit(f"Chaîne introuvable dans index.html :\n  {fr[:90]}")
        html = html.replace(fr, en)
    DST.parent.mkdir(exist_ok=True)
    DST.write_text(html, encoding="utf-8")
    print(f"OK → {DST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
