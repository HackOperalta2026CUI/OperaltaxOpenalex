# Contexte du projet pour Claude Code

Projet étudiant (Digital Innovation Week 2026, UNIGE, défi 13 Operalta). Nous relions OpenAlex aux cartes de décision d'Operalta, sur une décision réelle : quelle piste de traitement DNDi doit prioriser contre la maladie de Chagas.

## Structure
- `docs/index.html` : la carte vivante, page unique en HTML/CSS/JS sans dépendance de build. C'est l'outil de référence.
  - Les étapes sont dans la constante `ETAPES` : id, nom, requete, titre (mot exigé dans le titre), suivantes.
  - Cache : `dndi_cache` / `dndi_precedent` (6 h).
  - Clé : `openalex_cle` dans localStorage.
- `scripts/` : ancienne version Python, sans le filtre par titre.
- `data/` : exports datés, à nommer `AAAA-MM-JJ_matrice_operalta.csv`.

## Règles de calcul
- Couverture = études de l'étape / études de l'étape la mieux documentée.
- Couleurs : vert ≥ 50 %, jaune 20–50 %, rouge < 20 %.
- Tendance « en essor » : au moins 50 % des études datent de 2020 ou après.
- Le volume d'études ne mesure pas leur qualité : toujours le rappeler.

## Règles de travail
- Ne jamais écrire de clé API (OpenAlex, Operalta) dans un fichier du dépôt.
- Operalta (MCP) : proposer les changements et attendre la validation humaine avant toute écriture. Ne pas modifier les primitives d'Operalta.
- Vérifier les articles avant de croire une couleur : une faute de frappe a déjà créé un faux angle mort (« hagas »).
- Citer OpenAlex et garder le lien vers chaque requête (provenance).
- Écrire en français, en phrases courtes.
