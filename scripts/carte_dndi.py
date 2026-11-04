"""
Carte de décision DNDi x OpenAlex (Digital Innovation Week 2026, défi Operalta)

Pour chaque étape de la décision « Quelle piste de traitement DNDi doit-elle
prioriser contre la maladie de Chagas ? », le script :
  1. interroge OpenAlex,
  2. compte les études (total et depuis 2020),
  3. récupère les 3 articles les plus cités,
  4. attribue une couleur (vert / jaune / rouge),
puis écrit resultats.json et carte.html (carte cliquable à ouvrir dans le navigateur).

Utilisation (PowerShell) :
  pip install requests
  $env:OPENALEX_API_KEY = "ta_cle"
  python carte_dndi.py
"""

import html
import json
import os
import sys

import requests

API = "https://api.openalex.org/works"
KEY = os.environ.get("OPENALEX_API_KEY")

# Couleur RELATIVE : chaque étape est comparée à l'étape la mieux documentée de la carte.
# (Des seuils absolus comme « > 200 études » mettent tout en vert sur un sujet aussi étudié.)
SEUIL_VERT = 0.50   # ≥ 50 % de l'étape la mieux couverte → vert
SEUIL_JAUNE = 0.20  # entre 20 % et 50 % → jaune ; < 20 % → rouge (angle mort relatif)
ANNEE_RECENTE = 2020
SEUIL_TENDANCE = 0.50  # part d'études récentes au-delà de laquelle le sujet est « en essor »

# Les étapes de la carte : id, nom affiché, requête OpenAlex, étapes qui en dépendent.
# Requêtes courtes (2-3 mots-clés) : OpenAlex exige que TOUS les mots soient présents
# dans le titre ou le résumé, donc chaque mot en plus réduit fortement les résultats.
ETAPES = [
    {"id": "besoin", "nom": "Besoin médical",
     "requete": "Chagas prevalence", "suivantes": ["traitements"]},
    {"id": "traitements", "nom": "Traitements actuels",
     "requete": "Chagas benznidazole", "suivantes": ["molecules"]},
    {"id": "molecules", "nom": "Nouvelles molécules",
     "requete": "Trypanosoma cruzi drug discovery", "suivantes": ["toxicite"]},
    {"id": "toxicite", "nom": "Toxicité",
     "requete": "benznidazole adverse effects", "suivantes": ["essais"]},
    {"id": "essais", "nom": "Essais cliniques",
     "requete": "Chagas clinical trial", "suivantes": ["acces"]},
    {"id": "acces", "nom": "Accès / coût",
     "requete": "Chagas access treatment", "suivantes": ["decision"]},
]


def appel(params):
    """Appelle l'API OpenAlex et renvoie le JSON."""
    headers = {"Authorization": f"Bearer {KEY}"} if KEY else {}
    r = requests.get(API, params=params, headers=headers, timeout=30)
    r.raise_for_status()
    return r.json()


def analyser(etape):
    filtre = f"title_and_abstract.search:{etape['requete']}"

    # 1. Nombre total d'études + 3 plus citées
    data = appel({
        "filter": filtre,
        "sort": "cited_by_count:desc",
        "per_page": 3,
        "select": "title,publication_year,cited_by_count,doi,id",
    })
    total = data["meta"]["count"]
    articles = [
        {
            "titre": w.get("title") or "(sans titre)",
            "annee": w.get("publication_year"),
            "citations": w.get("cited_by_count", 0),
            "lien": w.get("doi") or w.get("id"),
        }
        for w in data["results"]
    ]

    # 2. Nombre d'études récentes
    recent = appel({
        "filter": f"{filtre},publication_year:>{ANNEE_RECENTE - 1}",
        "per_page": 1,
        "select": "id",
    })["meta"]["count"]

    # 3. Tendance : part des études publiées récemment
    part_recente = round(recent / total, 2) if total else 0
    en_essor = part_recente >= SEUIL_TENDANCE

    return {**etape, "total": total, "recent": recent,
            "part_recente": part_recente, "en_essor": en_essor,
            "articles": articles}


def colorier(resultats):
    """Couleur relative : compare chaque étape à la mieux documentée."""
    maximum = max(r["total"] for r in resultats) or 1
    for r in resultats:
        ratio = r["total"] / maximum
        r["couverture"] = round(ratio, 2)
        if ratio >= SEUIL_VERT:
            r["couleur"] = "vert"
        elif ratio >= SEUIL_JAUNE:
            r["couleur"] = "jaune"
        else:
            r["couleur"] = "rouge"


def generer_html(resultats):
    couleurs = {"vert": "#2e9e5b", "jaune": "#e0a800", "rouge": "#d64545"}
    donnees = json.dumps(resultats, ensure_ascii=False)
    noeuds = "".join(
        f'<button class="noeud" style="border-color:{couleurs[r["couleur"]]}" '
        f'onclick="voir({i})"><span class="pastille" '
        f'style="background:{couleurs[r["couleur"]]}"></span>'
        f'{html.escape(r["nom"])}{" 📈" if r["en_essor"] else ""}'
        f'<small>{r["total"]} études · {round(r["part_recente"] * 100)} % récentes</small></button>'
        f'<span class="fleche">→</span>'
        for i, r in enumerate(resultats)
    )
    return f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Carte DNDi Chagas</title>
<style>
 body {{ font-family: system-ui, sans-serif; margin: 24px; background:#f7f7f9; color:#1d1d1f; }}
 h1 {{ font-size: 1.3rem; }}
 .carte {{ display:flex; flex-wrap:wrap; align-items:center; gap:8px; margin:24px 0; }}
 .noeud {{ background:#fff; border:3px solid; border-radius:12px; padding:12px 16px;
          cursor:pointer; font-size:1rem; display:flex; flex-direction:column; align-items:center; gap:4px; }}
 .noeud small {{ color:#666; }}
 .pastille {{ width:14px; height:14px; border-radius:50%; }}
 .fleche {{ font-size:1.4rem; color:#888; }}
 .decision {{ background:#1d1d1f; color:#fff; border-radius:12px; padding:12px 16px; font-weight:600; }}
 #panneau {{ background:#fff; border-radius:12px; padding:16px 20px; max-width:760px; }}
 .legende span {{ margin-right:16px; }}
</style></head><body>
<h1>Quelle piste de traitement DNDi doit-elle prioriser contre la maladie de Chagas ?</h1>
<p class="legende">Couverture comparée à l'étape la mieux documentée :
<span>🟢 ≥ {round(SEUIL_VERT * 100)} %</span><span>🟡 {round(SEUIL_JAUNE * 100)}–{round(SEUIL_VERT * 100)} %</span><span>🔴 &lt; {round(SEUIL_JAUNE * 100)} % (angle mort)</span><span>📈 sujet en essor (≥ {round(SEUIL_TENDANCE * 100)} % d'études depuis {ANNEE_RECENTE})</span></p>
<div class="carte">{noeuds}<span class="decision">Décision</span></div>
<div id="panneau">Clique sur une étape pour voir ce que dit la science.</div>
<p><small>Source : OpenAlex. Couleur = volume d'études, pas leur qualité.</small></p>
<script>
const D = {donnees};
function esc(s) {{ const d = document.createElement('div'); d.textContent = s; return d.innerHTML; }}
function voir(i) {{
  const e = D[i];
  const arts = e.articles.map(a =>
    `<li><a href="${{esc(a.lien)}}" target="_blank">${{esc(a.titre)}}</a> (${{a.annee}}, ${{a.citations}} citations)</li>`
  ).join('');
  document.getElementById('panneau').innerHTML =
    `<h2>${{esc(e.nom)}}</h2>
     <p><b>${{e.total}}</b> études, dont <b>${{e.recent}}</b> depuis {ANNEE_RECENTE}
        (${{Math.round(e.part_recente * 100)}} %)${{e.en_essor ? ' : <b>sujet en essor 📈</b>' : ''}}.</p>
     <p>Requête : <code>${{esc(e.requete)}}</code></p>
     <h3>Articles les plus cités</h3><ul>${{arts}}</ul>`;
}}
</script></body></html>"""


def main():
    if not KEY:
        print("Attention : OPENALEX_API_KEY n'est pas définie, requêtes sans clé.")

    resultats = []
    for etape in ETAPES:
        print(f"→ {etape['nom']}…", end=" ", flush=True)
        try:
            r = analyser(etape)
        except requests.RequestException as err:
            print(f"ERREUR ({err})")
            sys.exit(1)
        resultats.append(r)
        print(f"{r['total']} études")

    colorier(resultats)

    print("\nRésultat :")
    for r in resultats:
        tendance = " 📈 en essor" if r["en_essor"] else ""
        print(f"  {r['nom']:<22} {r['total']:>5} études | "
              f"couverture {round(r['couverture'] * 100):>3} % | "
              f"récentes {round(r['part_recente'] * 100):>3} % → {r['couleur']}{tendance}")

    with open("resultats.json", "w", encoding="utf-8") as f:
        json.dump(resultats, f, ensure_ascii=False, indent=2)
    with open("carte.html", "w", encoding="utf-8") as f:
        f.write(generer_html(resultats))

    print("\nFichiers créés : resultats.json et carte.html")
    print("Ouvre carte.html dans ton navigateur.")


if __name__ == "__main__":
    main()
