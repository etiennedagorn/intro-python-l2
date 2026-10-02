#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TP5 revise - corrige minimal aligne sur l'enonce actif.

Objectif : pipeline pandas OWID, graphique, export et interpretation prudente.
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# Exercice 1 - preparation
out_dir = Path("out")
out_dir.mkdir(exist_ok=True)

# Exercice 2 - lecture du CSV
url = "https://ourworldindata.org/grapher/gdp-per-capita-worldbank.csv"
local_csv = Path("data/gdp-per-capita-worldbank.csv")

try:
    df = pd.read_csv(url)
    source = url
except Exception:
    if not local_csv.exists():
        raise FileNotFoundError(
            "Lecture internet impossible et fichier local absent : "
            "data/gdp-per-capita-worldbank.csv"
        )
    df = pd.read_csv(local_csv)
    source = str(local_csv)

print("Source :", source)
print(df.head())
print(df.shape)
print(df.columns)
# Exemple de commentaire attendu : le tuple df.shape donne lignes puis colonnes.

# Exercice 3 - renommage
value_col = df.columns[-1]
df = df.rename(
    columns={
        "Entity": "country",
        "Code": "code",
        "Year": "year",
        value_col: "gdp_pc",
    }
)
print(df[["country", "year", "gdp_pc"]].head())

# Exercice 4 - debogage pandas
# ModuleNotFoundError : pandas absent de l'environnement actif.
# FileNotFoundError : mauvais dossier courant ou fichier local absent.
# KeyError 'gdp_pc' : verifier df.columns et le renommage.
# selection vide : verifier latest_year, les valeurs manquantes et les noms de pays.

# Exercice 5 - annee recente
latest_year = df["year"].max()
latest = df.loc[df["year"] == latest_year].copy()
latest = latest.dropna(subset=["gdp_pc"])
print("Derniere annee :", latest_year)
print("Taille latest :", latest.shape)

# Exercice 6 - selection
pays_selection = [
    "France",
    "Germany",
    "Spain",
    "Poland",
    "United States",
    "China",
    "India",
    "Brazil",
]
selection = latest.loc[latest["country"].isin(pays_selection)].copy()
print(selection[["country", "gdp_pc"]])

# Exercice 7 - statistiques descriptives
moyenne = selection["gdp_pc"].mean()
mediane = selection["gdp_pc"].median()
minimum = selection["gdp_pc"].min()
maximum = selection["gdp_pc"].max()
part_au_dessus = (selection["gdp_pc"] > moyenne).mean() * 100

print(f"Moyenne : {moyenne:.2f}")
print(f"Mediane : {mediane:.2f}")
print(f"Minimum : {minimum:.2f}")
print(f"Maximum : {maximum:.2f}")
print(f"Part au-dessus de la moyenne : {part_au_dessus:.1f} %")

# Exercice 8 - graphique top 10
top10 = latest.sort_values("gdp_pc", ascending=False).head(10)
ax = top10.plot(kind="bar", x="country", y="gdp_pc", legend=False)
ax.set_xlabel("Pays")
ax.set_ylabel("PIB par habitant")
ax.set_title(f"Top 10 du PIB par habitant - {latest_year}")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(out_dir / "gdp_top10.png", dpi=300)
plt.close()

# Exercice 9 - export
selection[["country", "code", "year", "gdp_pc"]].to_csv(
    out_dir / "gdp_selection.csv",
    index=False,
)

# Exercice 10 - interpretation finale
top_selection = selection.loc[selection["gdp_pc"].idxmax()]
bottom_selection = selection.loc[selection["gdp_pc"].idxmin()]
france = selection.loc[selection["country"] == "France"]
if not france.empty:
    france_value = float(france["gdp_pc"].iloc[0])
    position_france = "au-dessus" if france_value > moyenne else "au-dessous"
else:
    position_france = "non disponible dans la selection"

# Annee etudiee : latest_year.
# Pays le plus eleve dans la selection : top_selection["country"].
# Pays le plus faible dans la selection : bottom_selection["country"].
# Moyenne et mediane de la selection : voir sorties ci-dessus.
# France : position_france par rapport a la moyenne.
# Limite : le choix des pays influence fortement les statistiques descriptives.
# Limite : le PIB par habitant ne mesure pas toutes les dimensions du developpement.

print("Plus eleve selection :", top_selection["country"])
print("Plus faible selection :", bottom_selection["country"])
print("Position France :", position_france)
