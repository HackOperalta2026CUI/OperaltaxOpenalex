# Méthode

## Décision
*Quelle piste de traitement DNDi doit-elle prioriser contre la maladie de Chagas ?*

Persona : une responsable de programme chez DNDi, avec un budget limité et plusieurs pistes possibles.

## Ce que fait la carte
Deux méthodes, au choix en haut de la page :
- **« titre seul »** (par défaut, celle du pitch) : tous les mots de la requête doivent figurer dans le titre (`title.search`). La couverture est calculée sur les études depuis 2020.
- **« titre + résumé »** : mots cherchés dans le titre ou le résumé (`title_and_abstract.search`), plus un mot exigé dans le titre. La couverture est calculée sur toutes les années.

Le classement des étapes est le même avec les deux méthodes.

Puis l'outil calcule :
- le **total** d'études, et le nombre d'études **depuis 2020** ;
- la **couverture relative** : études de l'étape / études de l'étape la mieux documentée ;
- la **couleur** : vert ≥ 50 %, jaune 20–50 %, rouge < 20 % ;
- la **tendance** « en essor » si au moins 50 % des études datent de 2020 ou après ;
- les filtres complémentaires : accès libre (`open_access.is_oa:true`), auteurs en Suisse (`authorships.institutions.country_code:CH`).

Les couleurs sont relatives parce que, sur un sujet aussi étudié, des seuils absolus (« plus de 200 études ») mettaient toutes les étapes en vert.

## Ce qui a changé
Le menu « Ce qui a changé » recalcule la carte à une date passée (`to_publication_date`) ou la compare à la dernière mise à jour. Il affiche les nouvelles études par étape et signale toute étape qui change de couleur.

## Limites connues
| Constat | Réponse |
|---|---|
| Une faute de frappe (« hagas ») a créé un faux angle mort (5 études) | Requêtes visibles et modifiables ; lire les articles avant de croire la couleur |
| Des articles très cités mais hors sujet | Mot exigé dans le titre |
| Le volume ne dit rien de la qualité | Affiché sur la carte ; la décision reste humaine |
| Trop de requêtes d'un coup (erreur 429) | Clé API, requêtes une par une, nouvel essai automatique, cache de 6 h |
