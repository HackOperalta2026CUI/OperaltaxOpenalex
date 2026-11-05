# Travailler à trois

## La règle d'or
**Toujours `git pull` avant de commencer, et pousser souvent.** On ne pousse jamais directement sur `main` : on passe par une branche et une pull request.

## Le cycle de travail

```powershell
git switch main
git pull
git switch -c marwan/export-csv        # prenom/sujet-court
# ... travailler ...
git add .
git commit -m "Ajoute la date dans le nom de l'export CSV"
git push -u origin marwan/export-csv
```

Ensuite, sur GitHub :
1. Ouvrir la **pull request**.
2. Demander une relecture à un coéquipier.
3. Faire **Squash and merge**.
4. Supprimer la branche.

## Qui touche à quoi
Pour éviter les conflits, une seule personne modifie `docs/index.html` à la fois. Annoncez-le dans le groupe avant de commencer.

| Zone | Responsable |
|---|---|
| Carte vivante (`docs/`) | Marwan |
| Matrice Operalta + MCP | Yohan |
| Pitch + documentation | Menna |

## Messages de commit
Un verbe à l'impératif et ce que ça change : `Corrige la requête Accès`, `Ajoute la vue quadrant`.

## Données
Les exports vont dans `data/`, avec la date dans le nom : `2026-11-04_matrice_operalta.csv`. On ne remplace pas un ancien export : c'est notre historique.
