# Bagora

Tuteur IA Socratique bienveillant pour préparer le **Diplôme National du Brevet (DNB) série générale**, niveau 3ème. Quatre enseignants virtuels — un par matière — s'appuyant sur les annales 2021-2025 et les programmes officiels du cycle 4.

- **M. Fourier** — Mathématiques
- **Mme Colette** — Français
- **M. Hérodote** — Histoire-Géographie-EMC
- **Mme Curie** — Sciences (Physique-Chimie, SVT, Technologie)

Le projet fournit un site statique qui génère un **prompt système personnalisé** (prénom de l'élève, style du professeur) prêt à être collé dans un projet Mistral, Claude ou ChatGPT, accompagné d'un **pack de fichiers markdown** (compétences, grilles critériées, questions d'annales) à uploader dans le même projet.

## Arborescence

```
.
├── README.md
├── LICENSE              ← MIT (code)
├── LICENSE-DATA         ← CC BY-SA 4.0 (contenu pédagogique)
├── docs/                ← site statique (GitHub Pages)
│   ├── index.html
│   ├── style.css
│   ├── app.js
│   └── downloads/       ← packs .zip par matière (générés)
├── data/                ← contenu pédagogique source
│   ├── mathematiques/
│   │   ├── consignes.md     ← prompt système
│   │   └── data/*.md        ← grilles de compétences + questions d'annales
│   ├── francais/
│   ├── histoire-geographie/
│   └── sciences/
└── src/                 ← scripts de build
    └── build_packs.py   ← génère docs/downloads/*.zip depuis data/
```

## Utilisation

### Consulter le site

Le site est un fichier `docs/index.html` qui peut être servi tel quel (GitHub Pages, serveur statique, ou simplement ouvert en local).

```bash
# Serveur local pour test
python3 -m http.server 8000
# Puis ouvre http://localhost:8000/docs/
```

### Régénérer les packs de données

Si tu modifies un fichier markdown dans `data/{matière}/data/` (ajout de notion, correction, enrichissement), il faut reconstruire les archives téléchargeables avec :

```bash
python3 src/build_packs.py
```

Le script lit `data/{matière}/data/*.md`, empaquette chaque matière à plat dans un `.zip` et écrit le résultat dans `docs/downloads/`. Pas de dépendance externe — stdlib Python uniquement.

Exemple de sortie :

```
  ✓ mathematiques           21 files    36 KB  →  docs/downloads/mathematiques.zip
  ✓ francais                28 files    49 KB  →  docs/downloads/francais.zip
  ✓ histoire-geographie     27 files    42 KB  →  docs/downloads/histoire-geographie.zip
  ✓ sciences                28 files    51 KB  →  docs/downloads/sciences.zip
```

### Modifier un prompt système

Les prompts sont dans `data/{matière}/consignes.md`. Le site `docs/index.html` les charge dynamiquement et applique les personnalisations (prénom, style pédagogique). Si tu changes un `consignes.md`, il faut mettre à jour la copie inline dans `docs/app.js` (bloc `RAW_PROMPTS`) — le site n'utilise pas `fetch()` pour éviter les problèmes de CORS et fonctionner hors-ligne.

## Déploiement

Repo hébergé sur GitHub avec le dossier `docs/` servi par GitHub Pages : *Settings → Pages → Source : main, folder : /docs*.

## Licences

Ce dépôt est distribué sous **deux licences distinctes** :

- **Code** (`docs/`, `src/`, HTML/CSS/JS, scripts Python) → [MIT](LICENSE)
- **Contenu pédagogique** (`data/` et `docs/downloads/`) → [CC BY-SA 4.0](LICENSE-DATA)

Si tu réutilises le code, crédite le projet Bagora. Si tu réutilises ou adaptes le contenu pédagogique, tu dois redistribuer tes modifications sous la même licence CC BY-SA 4.0.

## Sources

Les données sont dérivées des annales DNB et du programme officiel cycle 4 publiés par le Ministère de l'Éducation nationale sur [eduscol.education.gouv.fr](https://eduscol.education.gouv.fr). Les PDF originaux ne sont pas redistribués — seules des synthèses, résumés et grilles critériées dérivées sont présents ici.
