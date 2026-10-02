# -*- coding: utf-8 -*-
# TP : aviation_2024.csv — exploration de données
# Version propre & robuste

# ------------------------------------------------------------
# Ex.1–3 : système de fichiers & chargement
# ------------------------------------------------------------
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# 1) Répertoire courant (affichage)
print("CWD:", Path.cwd())
base_dir = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
out_dir = base_dir / "out"
out_dir.mkdir(exist_ok=True)

# 2) Dossier de travail (adapter ce chemin localement si nécessaire)
#code_dir = Path.home() / "Documents" / "code"
#code_dir.mkdir(parents=True, exist_ok=True)
#print("Target dir exists:", code_dir.exists())

# 3) Lecture du CSV (gestion d’encodage)
csv_path = base_dir / "data" / "aviation_2024.csv"
df = pd.read_csv(csv_path, encoding="utf-8")  # essayer "latin-1" si besoin
print("Loaded shape:", df.shape)

# ------------------------------------------------------------
# Harmonisation des noms de variables 
# ------------------------------------------------------------
# Recherche de la colonne d’émissions per capita (nom parfois variable)
emission_col = None
for c in df.columns:
    cl = c.lower()
    if cl.startswith("per capita total annual") and "aviation" in cl:
        emission_col = c
        break
if emission_col is None:
    raise ValueError("Colonne des émissions per capita (aviation) introuvable.")

# Renommage standard (évite les variantes CO2 / CO$_2$ / COâ‚‚)
df = df.rename(columns={
    emission_col: "co2_pc_aviation",
    "Entity": "country",
    "Code": "iso_code",
    "Year": "year",
})

# La colonne 'time' est redondante avec 'Year' dans le fichier distribué.
if "time" in df.columns:
    df = df.drop(columns="time")

# ------------------------------------------------------------
# Ex.3–5 : aperçus rapides
# ------------------------------------------------------------
print("\nAperçu (head):")
print(df.head())

print("\nInfo:")
df.info()

print("\nRésumé (describe numériques):")
print(df.describe())

print("\nValeurs manquantes (totaux):")
print(df.isna().sum())
# Ne pas conclure à l’absence de valeurs manquantes si des NaN sont listés.

# ------------------------------------------------------------
# Ex.6 : dictionnaire de variables
# country (str), iso_code (str), year (int),
# co2_pc_aviation (float) = émissions annuelles de CO2 par habitant (aviation)



# ------------------------------------------------------------
# Ex.7 : tri décroissant par émissions per capita
# ------------------------------------------------------------
top = df.sort_values(by="co2_pc_aviation", ascending=False)
print("\nTop (tri décroissant) — aperçu :")
print(top[["country", "co2_pc_aviation"]].head(10).to_string(index=False))

# ------------------------------------------------------------
# Ex.8 : Moyenne, médiane, min, max
# ------------------------------------------------------------
mean_val   = df["co2_pc_aviation"].mean()
median_val = df["co2_pc_aviation"].median()
min_val    = df["co2_pc_aviation"].min()
max_val    = df["co2_pc_aviation"].max()

print("\nStatistiques (co2_pc_aviation):")
print(f"  Moyenne  : {mean_val:.3f}")
print(f"  Médiane  : {median_val:.3f}")
print(f"  Min      : {min_val:.3f}")
print(f"  Max      : {max_val:.3f}")
# Si moyenne > médiane, distribution asymétrique à droite (quelques pays très émetteurs).

# ------------------------------------------------------------
# Ex.9 : France
# ------------------------------------------------------------
fr = df.loc[df["country"] == "France", ["country", "co2_pc_aviation"]]
print("\nFrance — émissions per capita :")
print(fr.to_string(index=False) if not fr.empty else "France absente (année retenue).")

# ------------------------------------------------------------
# Ex.10 : Graphique — 10 pays les plus émetteurs
# ------------------------------------------------------------
top10 = top.head(10)
ax = top10.plot(kind="bar", x="country", y="co2_pc_aviation", legend=False)
ax.set_xlabel("Pays")
ax.set_ylabel("Émissions CO₂ aviation par habitant")
ax.set_title(f"Top 10 — Aviation per capita")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(out_dir / "top10_aviation.png", dpi=150, bbox_inches="tight")
plt.show()

# ------------------------------------------------------------
# Ex.11 : describe sur la variable
# ------------------------------------------------------------
print("\nDescribe sur co2_pc_aviation :")
print(df["co2_pc_aviation"].describe())

# ------------------------------------------------------------
# Ex.12 : 5 plus faibles / 5 plus fortes valeurs
# ------------------------------------------------------------
bottom5 = df.sort_values(by="co2_pc_aviation", ascending=True).head(5)
top5    = df.sort_values(by="co2_pc_aviation", ascending=False).head(5)

print("\n5 pays les moins émetteurs (per capita) :")
print(bottom5[["country", "co2_pc_aviation"]].to_string(index=False))

print("\n5 pays les plus émetteurs (per capita) :")
print(top5[["country", "co2_pc_aviation"]].to_string(index=False))
# Éviter les explications causales sans variables de contrôle.

# ------------------------------------------------------------
# Ex.13 : variance & écart-type (échantillonnal)
# ------------------------------------------------------------
var_val = df["co2_pc_aviation"].var(ddof=1)
std_val = df["co2_pc_aviation"].std(ddof=1)
print("\nDispersion :")
print(f"  Variance   : {var_val:.3f}")
print(f"  Écart-type : {std_val:.3f}")

# ------------------------------------------------------------
# Ex.14 : Écart France vs moyenne monde (année retenue)
# ------------------------------------------------------------
if not fr.empty:
    fr_value = float(fr["co2_pc_aviation"].iloc[0])
    diff = fr_value - mean_val
    position = "au-dessus" if diff > 0 else ("en dessous" if diff < 0 else "égale à")
    print(f"\nFrance vs moyenne  : {diff:+.3f} ⇒ France {position} de la moyenne.")
else:
    print("\nFrance absente : comparaison non effectuée.")

# ------------------------------------------------------------
# Ex.15 : Histogramme
# ------------------------------------------------------------
ax = df["co2_pc_aviation"].hist(bins=30)
ax.set_xlabel("Émissions CO₂ aviation par habitant")
ax.set_ylabel("Nombre de pays")
ax.set_title(f"Distribution (per capita)")
plt.tight_layout()
plt.savefig(out_dir / "distribution_aviation.png", dpi=150, bbox_inches="tight")
plt.show()
# Lecture attendue : asymétrie à droite fréquente.
