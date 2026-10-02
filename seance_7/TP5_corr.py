# ============================================================
# TP L2 — Correction détaillée : pandas + matplotlib
# Base : part du revenu du top 1% (France)
# Fichier source : top_1_france.csv (Entity, Year, Top_1_pretax en %)
# ============================================================

from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# A. Démarrage & aperçu
# ------------------------------------------------------------

# 1) Chargement du CSV (on tente d'être robuste aux encodages usuels)
base_dir = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
csv_path = base_dir / "top_1_france.csv"
df = pd.read_csv(csv_path, encoding="utf-8")
df = df.loc[:, ~df.columns.str.startswith("Unnamed")]

# 2) Premier aperçu
print("\n--- Aperçu ---")
print(df.head())
print("\n--- Info ---")
print(df.info())
print("\n--- Colonnes ---")
print(df.columns)

# ------------------------------------------------------------
# B. Renommage & types
# ------------------------------------------------------------
df = df.rename(columns={
    "Entity": "entity",
    "Year": "year",
    "Top_1_pretax": "top1"
})

# Conversion de types
# year → int ; top1 → float
df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
df["top1"] = pd.to_numeric(df["top1"], errors="coerce")

print("\n--- Types après conversion ---")
print(df.dtypes)

# ------------------------------------------------------------
# C. Filtrage France & tri chronologique
# ------------------------------------------------------------
fr = df.loc[df["entity"] == "France"].copy()

# Tri et réindexation propre
fr = fr.sort_values("year").reset_index(drop=True)

print("\nFrance : années min/max")
print(fr["year"].min(), fr["year"].max())

# ------------------------------------------------------------
# D. Qualité des données : NA, bornes, doublons d'années
# ------------------------------------------------------------
print("\n--- Valeurs manquantes ---")
print(fr.isna().sum())

# Contrôle : top1 doit être dans [0, 100]
out_of_bounds = fr[(fr["top1"] < 0) | (fr["top1"] > 100)]
if not out_of_bounds.empty:
    print("\nATTENTION : valeurs hors bornes [0,100] détectées :")
    print(out_of_bounds)
else:
    print("\nAucune valeur hors bornes détectée.")

# Doublons d'années
dup_years = fr["year"].duplicated().sum()
print(f"\nDoublons d'années : {dup_years}")

# ------------------------------------------------------------
# E. Statistiques descriptives de base
# ------------------------------------------------------------
top1_mean = fr["top1"].mean()
top1_median = fr["top1"].median()
top1_min = fr["top1"].min()
top1_max = fr["top1"].max()

idx_max = fr["top1"].idxmax()
idx_min = fr["top1"].idxmin()
year_max = int(fr.loc[idx_max, "year"])
year_min = int(fr.loc[idx_min, "year"])

print("\n--- Statistiques top1 (en %) ---")
print(f"Moyenne : {top1_mean:.2f} ; Médiane : {top1_median:.2f}")
print(f"Min : {top1_min:.2f} (année {year_min}) ; Max : {top1_max:.2f} (année {year_max})")

# ------------------------------------------------------------
# F. Indice base 100
# ------------------------------------------------------------

# On prend l'année de base = première année disponible
base_value = fr["top1"].iloc[0]

# Calcul de l'indice base 100
fr["indice_100"] = 100 * fr["top1"] / base_value

print(f"\nAnnée de base : {fr['year'].iloc[0]}")
print(f"Valeur base (top1) : {base_value:.2f}")
print("Indice (doit être 100) :", fr["indice_100"].iloc[0])
# ------------------------------------------------------------
# G. Variations : en points vs en %
# ------------------------------------------------------------
fr["delta_pts"] = fr["top1"].diff()  # points de pourcentage
fr["delta_pct"] = 100 * fr["top1"].pct_change()  # variation en %

# Années de plus forte hausse/baisse selon chaque métrique
idx_max_pts = fr["delta_pts"].idxmax()
idx_min_pts = fr["delta_pts"].idxmin()
idx_max_pct = fr["delta_pct"].idxmax()
idx_min_pct = fr["delta_pct"].idxmin()

def safe_year(s, idx):
    return int(s.loc[idx]) if pd.notna(idx) else None

print("\n--- Variations ---")
print(f"Plus forte hausse (points) : {fr.loc[idx_max_pts, 'delta_pts']:.2f} pp en {safe_year(fr['year'], idx_max_pts)}")
print(f"Plus forte baisse (points) : {fr.loc[idx_min_pts, 'delta_pts']:.2f} pp en {safe_year(fr['year'], idx_min_pts)}")
print(f"Plus forte hausse (%) : {fr.loc[idx_max_pct, 'delta_pct']:.2f}% en {safe_year(fr['year'], idx_max_pct)}")
print(f"Plus forte baisse (%) : {fr.loc[idx_min_pct, 'delta_pct']:.2f}% en {safe_year(fr['year'], idx_min_pct)}")

# ============================================================
# H. Détection des trous d'années
# ============================================================
# Objectif :
#   Vérifier si la série temporelle présente des années manquantes.
#   Exemple : si l'on passe de 1980 à 1983 → gap = 3 → trou de 2 ans.
#
# Étapes :
#   1) On crée une colonne 'annee_suiv' : l'année suivante théorique
#   2) On calcule la différence (gap)
#   3) On repère les lignes où l'écart > 1
#   4) On affiche les trous (si présents)

# 1) Décalage de la colonne 'year' d'une ligne vers le haut
fr["annee_suiv"] = fr["year"].shift(-1)

# 2) Calcul de l'écart entre deux années consécutives
fr["gap"] = fr["annee_suiv"] - fr["year"]

# 3) Sélection des lignes où gap > 1 (trous dans la série)
holes = fr.loc[fr["gap"] > 1, ["year", "annee_suiv", "gap"]]

# 4) Affichage
if not holes.empty:
    print("\n=== Trous d'années détectés (écart > 1) ===")
    print("Ces lignes indiquent des sauts dans la série temporelle :")
    print(holes.to_string(index=False))

    # Option : proposer une solution de comblement
    print("\n→ Suggestion : réindexer la série sur toutes les années pour visualisation.")
else:
    print("\nAucun trou d'années (>1) détecté.")


# ============================================================
# I. Lissage : moyenne mobile 3 termes (centrée)
# ============================================================
# Objectif :
#   Produire une version lissée de la série afin de mieux voir les tendances,
#   en réduisant l'effet du bruit (variations annuelles ponctuelles).
#
# Remarques :
#   - window=3 → on utilise l'année précédente, l'année courante, l'année suivante
#   - center=True → centrer la fenêtre sur l'année courante
#   - min_periods=1 → évite de renvoyer NaN en bord de série

fr["mm3"] = fr["top1"].rolling(
    window=3,
    center=True,
    min_periods=1   # option utile pour conserver les premières/dernières années
).mean()

# ============================================================
# J. Découpage par périodes
# ============================================================
# Objectif :
#   Regrouper les années en grandes périodes historiques pour
#   calculer la moyenne du top 1% par période.
#
# Pourquoi ?
#   Cela permet d’observer les tendances longue durée :
#     - montée / baisse de l’inégalité
#     - comparaison entre époques
#
# Méthode :
#   - Définir des intervalles (bins) = bornes chronologiques
#   - Attribuer à chaque année une étiquette de période
#   - Calculer la moyenne par période
#
# Remarque :
#   Ajuster les bins selon la plage réelle de vos données !

# 1) Définition des bornes et étiquettes
bins = [1820, 1899, 1945, 1980, 2025]           # bornes inclusives
labels = ["1820–1899", "1900–1945", "1946–1980", "1981–2025"]

# 2) Découpage en périodes
#   - pd.cut place chaque année dans un intervalle
#   - include_lowest=True → la première borne inclut sa limite min
#   - right=True → l’intervalle inclut sa borne supérieure
fr["periode"] = pd.cut(
    fr["year"],
    bins=bins,
    labels=labels,
    include_lowest=True,
    right=True
)

# Vérification rapide : affichage des premières lignes
print("\nAperçu période :")
print(fr[["year", "periode"]].head(10))

# 3) Calcul des moyennes du top1 par période
period_means = (
    fr.groupby("periode", dropna=False)["top1"]
      .mean()
      .round(2)   # arrondi pour lisibilité
)

# 4) Affichage
print("\n=== Moyenne de top1 (en %) par période ===")
for per, val in period_means.items():
    print(f"{per} : {val if pd.notna(val) else 'NA'}")

# Option : Contrôle si certaines années n'ont pas été classées
nb_na = fr["periode"].isna().sum()
if nb_na > 0:
    print(f"\n⚠ Attention : {nb_na} années n'appartiennent à aucune période !")
    print("→ Vérifiez la plage des bins.")
else:
    print("\nToutes les années appartiennent à une période.")

# ------------------------------------------------------------
# K. Graphiques (matplotlib)
# ------------------------------------------------------------
out_dir = base_dir / "out"
out_dir.mkdir(exist_ok=True)

# 1) Série top1 + mm3
plt.figure(figsize=(9, 4.5))
plt.plot(fr["year"], fr["top1"], marker="o", linestyle="-", label="Top 1% (%, point)")
plt.plot(fr["year"], fr["mm3"], linestyle="-", label="Moyenne mobile (3)")
plt.title("France — Part du revenu du top 1% (série et lissage)")
plt.xlabel("Année")
plt.ylabel("Part du top 1% (en %)")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig(out_dir / "serie_top1_mm3.png", dpi=150, bbox_inches="tight")
# plt.show();  # décommenter si nécessaire en local

# 2) Indice base 100
plt.figure(figsize=(9, 4.5))
plt.plot(fr["year"], fr["indice_100"], marker="o", linestyle="-")
plt.axhline(100, linestyle="--", linewidth=1)
plt.title(f"France — Indice base 100")
plt.xlabel("Année")
plt.ylabel("Indice (base 100)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(out_dir / "indice_base100.png", dpi=150, bbox_inches="tight")

# 3) Barres des variations (delta_pts)
plt.figure(figsize=(9, 4.5))
colors = np.where(fr["delta_pts"] >= 0, "tab:blue", "tab:red")
plt.bar(fr["year"], fr["delta_pts"], color=colors, width=0.8)
plt.axhline(0, color="black", linewidth=0.8)
plt.title("France — Variation annuelle en points de % (Top 1%)")
plt.xlabel("Année")
plt.ylabel("Δ en points de %")
plt.grid(alpha=0.2, axis="y")
plt.tight_layout()
plt.savefig(out_dir / "delta_points.png", dpi=150, bbox_inches="tight")

print("\nFigures enregistrées dans le dossier 'out/'.")

# ------------------------------------------------------------
# L. Export CSV propre
# ------------------------------------------------------------
cols_keep = ["year", "top1", "indice_100", "delta_pts", "delta_pct", "mm3", "periode"]
export_df = fr[cols_keep].copy()
export_path = out_dir / "france_top1_L2.csv"
export_df.to_csv(export_path, index=False, encoding="utf-8")
print(f"\nCSV exporté : {export_path}")

# ------------------------------------------------------------
# M. Mini-interprétation (imprimée en console)
# ------------------------------------------------------------
first_year = int(fr["year"].iloc[0])
last_year = int(fr["year"].iloc[-1])
first_top1 = fr["top1"].iloc[0]
last_top1 = fr["top1"].iloc[-1]
ecart_points = last_top1 - first_top1

print("\n--- Mini-interprétation (bref) ---")
print(f"Sur {first_year}–{last_year}, le top 1% passe de {first_top1:.2f}% à {last_top1:.2f}% "
      f"({ecart_points:+.2f} points).")
print("La moyenne mobile (3) lisse les à-coups annuels et met en évidence les tendances.")
if not holes.empty:
    print("Attention : des trous d'années existent (voir sortie console) ; prudence dans l'interprétation fine.")
print("Comparer les périodes montre où la concentration est la plus élevée (voir moyennes par période).")
