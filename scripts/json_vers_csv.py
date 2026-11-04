"""
Convertit resultats.json (produit par carte_dndi.py) en matrice_operalta.csv,
prêt à être déposé dans le chat Operalta ou ouvert dans Excel.

Utilisation (PowerShell, dans le même dossier que resultats.json) :
  python json_vers_csv.py
"""

import csv
import json

with open("resultats.json", encoding="utf-8") as f:
    resultats = json.load(f)

colonnes = [
    "Étape", "Requête OpenAlex", "Nb études", "Études depuis 2020",
    "Part récente (%)", "Couverture vs meilleure étape (%)", "Couleur",
    "En essor", "Article clé 1", "Article clé 2", "Article clé 3",
]

# utf-8-sig : pour qu'Excel affiche correctement les accents
with open("matrice_operalta.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f, delimiter=";")
    w.writerow(colonnes)
    for r in resultats:
        articles = [
            f'{a["titre"]} ({a["annee"]}, {a["citations"]} citations) {a["lien"]}'
            for a in r["articles"]
        ]
        articles += [""] * (3 - len(articles))
        w.writerow([
            r["nom"], r["requete"], r["total"], r["recent"],
            round(r["part_recente"] * 100), round(r.get("couverture", 0) * 100),
            r["couleur"], "oui" if r["en_essor"] else "non",
            *articles[:3],
        ])

print("Fichier créé : matrice_operalta.csv")
