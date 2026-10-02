# =========================================================
# CORRECTION TP — Visualisation (Matplotlib) & Stats à la main
# Fichier : correction_tp_viz.py  (VERSION SANS FONCTIONS, TRÈS COMMENTÉE)
# =========================================================
# Objectifs pédagogiques :
#   - Construire des graphiques simples avec Matplotlib (histogrammes, boxplots)
#   - Calculer des statistiques descriptives "à la main" (moyenne, médiane, étendue, écart-type)
#   - Comprendre la logique de chaque ligne de code et la relier au résultat
# =========================================================

# ---- Imports standard ----
import os                    # pour vérifier la création des fichiers images (chemins, existence)
import math                  # pour sqrt (racine carrée) ; on pourrait faire **0.5 à la place
import matplotlib.pyplot as plt  # bibliothèque de visualisation

# -----------------------------
# Données utilisées dans tout le script
# -----------------------------
# Une petite liste de notes pour l’histogramme simple (A.1)
notes = [12, 14, 10, 8, 16, 15, 9]

# Deux jeux de notes (A et B) pour comparer deux groupes (A.2 à A.4)
A = [12, 14, 10, 8, 16, 15, 9]
B = [11, 13, 12, 7, 17, 14, 10]

print("=== CORRECTION TP — Visualisation & Stats à la main (sans fonctions) ===\n")

# =========================================================
#        A.1 — Histogramme des notes (liste "notes")
# =========================================================
# 1) Créer une nouvelle figure → évite que les graphes se superposent par erreur
plt.figure()

# 2) Tracer l’histogramme :
#    - notes : données à représenter
#    - bins=5 : nombre de classes (barres). Ici 5 barres couvrant la plage (0,20)
#    - range=(0, 20) : bornes min/max affichées (utile pour fixer la même échelle)
#    - edgecolor="black" : bordure noire sur les barres pour bien les distinguer
plt.hist(notes, bins=5, range=(0, 20), edgecolor="black")

# 3) Habillage (labels des axes + titre) → indispensable pour un graphique lisible
plt.xlabel("Note")          # nom de l’axe horizontal
plt.ylabel("Effectif")      # nom de l’axe vertical
plt.title("Histogramme des notes")  # titre du graphique

# 4) Calcul de la moyenne (à la main) et ajout d’une ligne verticale :
#    - sum(notes)/len(notes) : moyenne arithmétique
#    - plt.axvline(...): trace une ligne verticale à x = moyenne
#    - linestyle="--" : pointillés ; linewidth=1 : épaisseur fine
m_notes = sum(notes) / len(notes)
plt.axvline(m_notes, linestyle="--", linewidth=1)

# 5) Mise en page / export / affichage :
#    - plt.tight_layout() : ajuste automatiquement les marges pour éviter que ça déborde
#    - plt.savefig(...) : export PNG (dpi 300, bonne qualité impression ; bbox_inches="tight" rogne les marges)
#    - plt.show() : affiche la figure (bloquant dans certains environnements)
plt.tight_layout()
outfile = "hist_notes.png"
plt.savefig(outfile, dpi=300, bbox_inches="tight")
plt.show()

# 6) Vérification : chemin absolu + existence (True si le fichier est bien créé)
print(f"[A.1] Fichier créé : {os.path.abspath(outfile)} -> {os.path.exists(outfile)}")

# =========================================================
#   A.2 — Deux distributions sur le même graphique (A vs B)
# =========================================================
# 1) Nouvelle figure (sinon on dessine par-dessus l’histogramme précédent)
plt.figure()

# 2) Dessiner DEUX histogrammes sur la même figure :
#    - alpha=0.6 : transparence pour voir les barres qui se recouvrent
#    - label="Classe A/B" : pour la légende
#    - edgecolor="black" : bordures visibles
#    - bins/range identiques pour rendre la comparaison pertinente
plt.hist(A, bins=5, range=(0, 20), alpha=0.6, label="Classe A", edgecolor="black")
plt.hist(B, bins=5, range=(0, 20), alpha=0.6, label="Classe B", edgecolor="black")

# 3) Calcul et tracé des moyennes de A et B (mêmes options de style que plus haut)
mA = sum(A) / len(A)
mB = sum(B) / len(B)
plt.axvline(mA, linestyle="--", linewidth=1)  # ligne verticale sur la moyenne de A
plt.axvline(mB, linestyle="--", linewidth=1)  # ligne verticale sur la moyenne de B

# 4) Habillage : labels, titre et LÉGENDE (pour identifier A vs B)
plt.xlabel("Note")
plt.ylabel("Effectif")
plt.title("Comparaison de deux distributions (A vs B)")
plt.legend()  # indispensable pour afficher label="..."

# 5) Export/affichage comme précédemment
plt.tight_layout()
outfile = "hist_compare.png"
plt.savefig(outfile, dpi=300, bbox_inches="tight")
plt.show()

print(f"[A.2] Fichier créé : {os.path.abspath(outfile)} -> {os.path.exists(outfile)}")
print("[A.2] Moyennes ~ attendues : mA = 12.00 ; mB = 12.00")  # simple repère de lecture

# =========================================================
#              A.3 — Boxplot (A vs B)
# =========================================================
# 1) Nouvelle figure
plt.figure()

# 2) Boxplot côte à côte :
#    - on passe [A, B] (liste de listes) → 2 boîtes produites
#    - labels : étiquettes sous chaque boîte
#    - showmeans=True : affiche aussi la moyenne (petit symbole) en plus de la médiane
plt.boxplot([A, B], labels=["Classe A", "Classe B"], showmeans=True)

# 3) Habillage
plt.ylabel("Note")
plt.title("Boîtes à moustaches — A vs B")

# 4) Export + affichage
plt.tight_layout()
outfile = "boxplot_classes.png"
plt.savefig(outfile, dpi=300, bbox_inches="tight")
plt.show()

print(f"[A.3] Fichier créé : {os.path.abspath(outfile)} -> {os.path.exists(outfile)}")
print("[A.3] Lecture : boîte = IQR (Q3−Q1), trait = médiane, moustaches ≈ 1.5×IQR.")

# =========================================================
#   A.4 — Statistiques descriptives (100% à la main)
#       (tout en ligne, sans aucune fonction)
# =========================================================
print("\n[A.4] Statistiques descriptives (calculées à la main)")

# ---- Calculs pour A ----
# n : taille de l’échantillon, somme : utile pour la moyenne
nA = len(A)
sA = sum(A)
moyA = sA / nA  # moyenne = somme / effectif

# Pour la médiane, on trie une COPIE (pour ne pas modifier A)
TA = sorted(A)
midA = nA // 2      # indice du milieu
# Si nA impair → valeur centrale ; si nA pair → moyenne des deux centrales
if nA % 2 == 1:
    medA = TA[midA]
else:
    medA = (TA[midA - 1] + TA[midA]) / 2

# Min/Max/Étendue (amplitude)
minA = min(A)
maxA = max(A)
etendueA = maxA - minA

# Variance (population) = moyenne des carrés des écarts à la moyenne
#  somme((x - moy)^2) / n ; écart-type = racine carrée de la variance
var_pop_A = sum((x - moyA) ** 2 for x in A) / nA
sd_pop_A = math.sqrt(var_pop_A)

# Variance (échantillon) = somme((x - moy)^2) / (n-1) → correction de Bessel
# Attention : nA doit être > 1 pour éviter division par zéro
if nA > 1:
    var_ech_A = sum((x - moyA) ** 2 for x in A) / (nA - 1)
    sd_ech_A = math.sqrt(var_ech_A)
else:
    sd_ech_A = float("nan")  # "not a number" si pas définissable

# ---- Calculs pour B (même logique, recopiée pour la clarté) ----
nB = len(B)
sB = sum(B)
moyB = sB / nB

TB = sorted(B)
midB = nB // 2
if nB % 2 == 1:
    medB = TB[midB]
else:
    medB = (TB[midB - 1] + TB[midB]) / 2

minB = min(B)
maxB = max(B)
etendueB = maxB - minB

var_pop_B = sum((x - moyB) ** 2 for x in B) / nB
sd_pop_B = math.sqrt(var_pop_B)

if nB > 1:
    var_ech_B = sum((x - moyB) ** 2 for x in B) / (nB - 1)
    sd_ech_B = math.sqrt(var_ech_B)
else:
    sd_ech_B = float("nan")

# ---- Affichage sous forme de tableau aligné ----
# On prépare une ligne d’en-têtes avec formatage d’alignement :
#  - {:<8}  = aligné à gauche sur 8 caractères
#  - {:>3}  = aligné à droite sur 3 caractères
#  - {:>6.2f} = nombre flottant sur 6 colonnes avec 2 décimales
entetes = ["Classe", "n", "Somme", "Moy", "Med", "Min", "Max", "Étendue", "SD(pop)", "SD(éch)"]
print("{:<8} {:>3} {:>6} {:>6} {:>6} {:>5} {:>5} {:>8} {:>8} {:>8}".format(*entetes))

# Ligne pour A (on reprend les variables calculées ci-dessus)
print("{:<8} {:>3d} {:>6d} {:>6.2f} {:>6.2f} {:>5d} {:>5d} {:>8d} {:>8.3f} {:>8.3f}".format(
    "A", nA, sA, moyA, medA, minA, maxA, etendueA, sd_pop_A, sd_ech_A
))

# Ligne pour B
print("{:<8} {:>3d} {:>6d} {:>6.2f} {:>6.2f} {:>5d} {:>5d} {:>8d} {:>8.3f} {:>8.3f}".format(
    "B", nB, sB, moyB, medB, minB, maxB, etendueB, sd_pop_B, sd_ech_B
))

# ---- Commentaires pour guider la lecture des résultats ----
print("\n[A.4] Commentaires :")
print("- Les deux classes ont la même moyenne (≈ 12.00), mais des dispersions légèrement différentes.")
print(f"- SD(pop) A ≈ {sd_pop_A:.3f} ; SD(pop) B ≈ {sd_pop_B:.3f}  → B un peu plus dispersée ici.")
print("- La moyenne est sensible aux valeurs extrêmes, la médiane et l’IQR (boxplot) le sont moins.")

# ---- Récapitulatif des fichiers produits ----
print("\nTerminé. Vérifiez les images générées dans le dossier courant :")
print(" - hist_notes.png")        # histogramme simple (A.1)
print(" - hist_compare.png")      # deux histogrammes superposés (A.2)
print(" - boxplot_classes.png")   # boîtes à moustaches A vs B (A.3)
