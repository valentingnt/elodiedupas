# Charte graphique — elodiedupas.fr

Référence de la direction artistique du site. Source de vérité : les variables CSS de `index.html` (`:root`). Si ce document et le code divergent, le code fait foi et ce document est à mettre à jour.

---

## 1. Intention

- **Sujet** : site d'Élodie Dupas, doctorante en économie du développement (Bordeaux School of Economics). Thèse : pollution de l'air et inégalités de genre dans les pays à revenu faible et intermédiaire.
- **Ton** : sérieux, épuré, « agence de DA » subtil mais léché. L'humour tient en un seul élément, le meme (teckel à la pompe), traité comme une figure d'article scientifique.
- **Références** : l'article LaTeX (Computer Modern, figures numérotées, sections §, `\begin{document}`), la grille éditoriale suisse, le papier imprimé (grain léger).
- **Contraintes fortes** :
  - une seule page, **jamais de scroll** (`html, body { overflow: hidden }`), sur tous les écrans ;
  - **performance** : lisible sur des ordinateurs lents (public académique), page ≈ 100 Ko ;
  - **la photo est toujours en couleur** (pas de noir et blanc, pas d'effet au survol).

## 2. Couleurs

| Rôle | Variable | Clair | Sombre | Usage |
|---|---|---|---|---|
| Fond | `--bg` | `#f3f2ee` | `#0f0f0e` | papier, fond de page |
| Encre | `--ink` | `#111110` | `#ecebe6` | texte principal, filet de progression |
| Secondaire | `--muted` | `#8a8880` | `#7c7a73` | libellés, légendes de bas de page |
| Filet | `--hair` | `rgba(17,17,16,.14)` | `rgba(236,235,230,.14)` | lignes de 1 px (barres haut/bas, séparateurs) |
| Piste | `--track` | `rgba(17,17,16,.10)` | `rgba(236,235,230,.10)` | fond de piste, survols, image en chargement |
| Accent | `--accent` | `#b8432c` | `#e07a5f` | **usage unique et ponctuel** : point du filet, coche « Adresse copiée » |
| Grain | `--grain` | `0.05` | `0.07` | opacité du bruit de papier |

- Panneau contact : fond `#fbfaf7` (clair) / `#1b1b19` (sombre).
- Voile derrière le panneau mobile : `rgba(10,10,9,.38)` (clair) / `rgba(0,0,0,.55)` (sombre) ; transparent sur desktop.
- Le mode sombre suit `prefers-color-scheme`, sans bouton de bascule.
- `theme-color` : `#f3f2ee` / `#0f0f0e`.

**Règle** : pas d'autre couleur. L'accent n'est jamais utilisé pour du texte courant ni pour de grandes surfaces.

## 3. Typographie

Familles (auto-hébergées dans `assets/fonts/`, réduites aux glyphes latins, licence OFL) :

| Famille | Fichier | Rôle |
|---|---|---|
| CMU Serif (romain) | `cmu-serif-roman.lat.woff2` | nom, texte |
| CMU Serif (italique) | `cmu-serif-italic.lat.woff2` | grande phrase, légendes, adresse e-mail du panneau |
| CMU Typewriter | `cmu-typewriter-text-roman.lat.woff2` | libellés (`.label`), commandes LaTeX |

Pas de gras sur la page : tout est en graisse 400. Repli : `"Latin Modern Roman", Georgia, serif` / `ui-monospace, monospace`.

Échelle :

| Élément | Classe | Taille | Style |
|---|---|---|---|
| Nom (h1) | `.name` | 17 px (19 px sur grand écran) | romain, interlettrage 0.01em |
| Libellés | `.label` | 11 px (12 px grand écran, 10 px pour `\begin…` sur mobile) | Typewriter, **MAJUSCULES**, interlettrage 0.08em |
| Commandes LaTeX | `.doc .label` | 11 px | Typewriter, minuscules, interlettrage 0.02em |
| Légendes | `.caption` | 14 px (13 px tablette, 15 px grand écran) | italique, interligne 1.35, max 18ch |
| Grande phrase | `.title` | `clamp(24px, min(4.4vw, 6.6vh), 56px)` | italique, interligne 1.06, interlettrage −0.012em, `text-wrap: balance` |
| Panneau : adresse | `.sheet-email` | 22 px mobile / 18 px desktop | italique |
| Panneau : actions | `.action` | 17 px mobile / 15 px desktop | romain |

Typographie française : apostrophe typographique `’` dans les textes visibles quand c'est possible, espace avant « ! » (« Copié ! »).

## 4. Mise en page

Structure en trois bandes, hauteur exacte de la fenêtre (`100dvh`, repli `100vh`) :

```
┌───────────────────────────────────────────────────────────────┐
│ Élodie Dupas     DOCTORANTE EN ÉCONOMIE… · BxSE    ME CONTACTER│  barre haute + filet
├───────────────────────────────────────────────────────────────┤
│                         ┌────────┐  § 0 THÈSE                  │
│                         │  meme  │  Pollution de l’air et…     │  scène
│   FIG. 1                │  9:16  │                             │
│   Approvisionnement.    └────────┘                             │
│                Page en cours de remplissage                    │  titre
│        \begin{document} ───────●──────── \end{document}        │  filet
├───────────────────────────────────────────────────────────────┤
│ © 2026 · English                                    19.10.2026 │  barre basse + filet
└───────────────────────────────────────────────────────────────┘
```

- **Marges** de page : `clamp(16px, 3.2vw, 44px)` sur les côtés ; haut `clamp(12px, 3vh, 22px)` ; zones sûres iOS respectées (`env(safe-area-inset-*)`).
- **Barres** : grille `1fr auto 1fr` en haut, `1fr auto` en bas, filet `--hair` de 1 px, 14 px d'espacement (8 px sur écran très bas).
- **Scène** : grille `1fr auto 1fr`. « Fig. 1 » + légende à gauche, alignées en bas de l'image ; « § 0 Thèse » + sujet à droite, alignés en haut de l'image.
- **Image** : ratio 9:16, hauteur = espace disponible via container queries (`min(100cqh, var(--plate-max), 177.7cqw)`), plafond `--plate-max` = 620 px (760 px sur grand écran). Repli sans container queries : `clamp(160px, 100vh − 330px, …)`.
- **Composition centrée verticalement** : la rangée image grandit jusqu'au plafond, puis l'ensemble image + titre reste centré.

Points de rupture :

| Condition | Changement |
|---|---|
| `max-width: 860px` | le titre central de la barre haute disparaît |
| `max-width: 560px` (téléphone) | une colonne : légende « Fig. 1 » au-dessus de l'image, « § 0 » masqué, image pleine hauteur |
| `max-height: 560px` et ratio ≥ 5/4 (portable zoomé, téléphone à l'horizontale) | image à gauche, titre à droite, légendes masquées |
| `max-height: 460px` | marges et barres resserrées |
| `min-width: 1600px` et `min-height: 1100px` | image jusqu'à 760 px, textes un cran plus grands |

Testé sur Chrome, Firefox et WebKit, du 320×568 au 3440×1300, plus le téléphone à l'horizontale (812×375, 667×340).

## 5. Éléments signature (LaTeX / recherche)

- **Computer Modern** : la police de LaTeX, utilisée pour tout le site (pas de colophon visible).
- **Figure numérotée** : « FIG. 1 » + légende en italique, comme dans un article (« Approvisionnement. »).
- **Section** : « § 0 THÈSE » + sujet de thèse.
- **Filet de progression** : `\begin{document}` ─── ● ─── `\end{document}`, rempli à 62 %, point accent qui pulse. Métaphore de la page « en cours de remplissage ».
- **Grain de papier** : bruit SVG (`feTurbulence`) fixe, opacité 5 % (7 % en sombre).
- **Jeu de mots** : FR « Page en cours de remplissage », EN « Page filling up » (faire le plein, comme le teckel).

## 6. Mouvement

Uniquement `transform` et `opacity` (pris en charge par le GPU, fluide sur machines lentes).

| Courbe | Valeur | Usage |
|---|---|---|
| `--ease` | `cubic-bezier(0.22, 1, 0.36, 1)` | toutes les animations de page |
| `--sheet-ease` | `cubic-bezier(0.32, 0.72, 0, 1)` | panneau mobile (courbe iOS) |

Séquence d'arrivée :

| Élément | Animation | Durée | Délai |
|---|---|---|---|
| Image | rideau qui se retire vers le haut (`scaleY` 1→0) | 1.4 s | 0.15 s |
| Image | léger zoom arrière (`scale` 1.08→1) | 1.8 s | 0.15 s |
| Titre | monte depuis un masque (`translateY` 105 %→0) | 1.1 s | 0.55 s |
| Légendes | fondu | 1 s | 0.8 s |
| Filet | fondu, puis tracé (`scaleX`) + point qui glisse | 1 s, puis 2.6 s | 0.95 s / 1.2 s |
| Point accent | pulsation d'opacité (1 → 0.25) | 2.4 s, en boucle | 3.8 s |

`prefers-reduced-motion` : tout est affiché directement, sans animation.

## 7. Contact

Le même panneau sert partout, son affichage s'adapte :

- **Déclencheur** : « ME CONTACTER » (libellé Typewriter, en haut à droite), soulignement qui se trace au survol et reste visible tant que le panneau est ouvert (desktop).
- **Contenu** : libellé « CONTACT », adresse `elodie.dupas@u-bordeaux.fr` en italique, puis deux lignes séparées par des filets :
  - enveloppe + « Écrire un e-mail » + chevron → `mailto:` ;
  - icône copier + « Copier l'adresse » → l'icône devient une coche accent et le texte « Adresse copiée ».
- **Mobile** (`hover: none` et `pointer: coarse`) : bottom sheet pleine largeur, coins hauts arrondis 18 px, poignée, bouton « Fermer », voile sombre. Se ferme en glissant vers le bas (seuil 30 % ou vitesse > 0.45 px/ms), en touchant le voile, ou 1.4 s après la copie. Vibration courte à la copie sur Android.
- **Desktop** : popover de 340 px sous le bouton, aligné à droite, coins 10 px, ombre douce, voile transparent. Se ferme avec Échap, par un clic à côté, ou après la copie. Lignes surlignées au survol, chevron qui avance de 2 px.
- **Accessibilité** : `role="dialog"`, `aria-modal`, `aria-expanded` sur le bouton, page passée en `inert`, annonce « Adresse e-mail copiée » pour les lecteurs d'écran, focus rendu au bouton uniquement après une navigation au clavier.

Icônes : traits fins (1.2 px), bouts arrondis, `currentColor`, dessinées en SVG inline (enveloppe, copier, coche, chevron).

## 8. Image (le meme)

- Teckel en lunettes de soleil sur un jerrican, à la pompe. **Toujours en couleur.**
- Fichiers : `assets/meme-360.{avif,webp,jpg}`, `assets/meme-720.{avif,webp}`, `assets/meme.jpg` (720×1280, repli). Servis via `<picture>` + `srcset`, `fetchpriority="high"`.
- Cadre : aucun cadre ni ombre ; fond `--track` pendant le chargement.

## 9. Identité dérivée

- **Favicon / icônes** : « é » en CMU Serif italique, `#f3f2ee` sur `#111110`. Fichiers : `icon.svg` (coins 12/64), `favicon.ico` (16/32/48), `apple-touch-icon.png` (180), `icon-192.png`, `icon-512.png`.
- **Images de partage** (`og-fr.png`, `og-en.png`, 1200×630) : même fond, barres et filets ; à gauche libellé Typewriter, nom en CMU Serif 92 px, sujet en italique (taille ajustée pour ne pas toucher l'image), filet `\begin{document}` ; à droite le meme en 9:16. Le générateur est un script Python hors dépôt : pour les refaire, reprendre ces règles. Changer le paramètre `?v=` dans les balises `og:image` à chaque nouvelle version, pour forcer les réseaux à rafraîchir leur cache.

## 10. Textes de référence

| Emplacement | Français | Anglais |
|---|---|---|
| Barre haute | Doctorante en économie du développement · BxSE | PhD candidate in development economics · BxSE |
| Bouton | Me contacter | Contact me |
| Fig. 1 | Approvisionnement. | Supply. |
| § 0 | Thèse — Pollution de l’air et inégalités de genre. | Thesis — Air pollution and gender inequality. |
| Titre | Page en cours de remplissage | Page filling up |
| Panneau | Écrire un e-mail / Copier l'adresse / Adresse copiée / Fermer | Write an email / Copy address / Address copied / Close |

La version anglaise (`en/index.html`) est **générée** par `python3 tools/build-en.py` : toute modification de `index.html` doit être suivie de cette commande, et tout nouveau texte visible ajouté à la liste `PAIRS` du script.
