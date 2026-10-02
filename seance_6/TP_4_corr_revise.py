#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TP4 revise - corrige minimal aligne sur l'enonce actif.

Objectif : graphique, random.choice, simulation simple et interpretation.
"""

import random
import matplotlib.pyplot as plt

# Exercice 1 - donnees
fertilite = {
    "World": 2.3,
    "France": 1.8,
    "United States": 1.6,
    "Japan": 1.2,
    "India": 2.0,
    "Nigeria": 4.5,
    "Niger": 6.1,
    "Brazil": 1.6,
    "Ethiopia": 3.9,
    "China": 1.0,
}

pays = list(fertilite.keys())
valeurs = list(fertilite.values())
moyenne_initiale = sum(valeurs) / len(valeurs)

print("Nombre d'observations :", len(fertilite))
print(f"Moyenne initiale : {moyenne_initiale:.2f} enfants par femme")

# Exercice 2 - graphique en barres
plt.figure()
plt.bar(pays, valeurs)
plt.xticks(rotation=45, ha="right")
plt.ylabel("Enfants par femme")
plt.title("Taux de fecondite - extrait OWID")
plt.tight_layout()
plt.savefig("fertilite_barres.png", dpi=300)
plt.close()

# Exercice 3 - interpretation du graphique
# Niger a le taux le plus eleve dans cet extrait.
# China a le taux le plus faible.
# Le graphique rend les comparaisons plus visibles qu'une liste brute.

# Exercice 4 - un tirage aleatoire
random.seed(123)
tirage = random.choice(valeurs)
print("Un tirage :", tirage)

# Exercice 5 - moyenne de 20 tirages
tirages = []
for i in range(20):
    tirages.append(random.choice(valeurs))

moyenne_tirages = sum(tirages) / len(tirages)
print(f"Moyenne de 20 tirages : {moyenne_tirages:.2f}")

# Debogage :
# for i in range(20) sans deux-points -> SyntaxError.
# Une ligne non indentee apres for -> IndentationError.

# Exercice 6 - stabilisation
tailles = [5, 20, 100, 1000]
for n in tailles:
    tirages = []
    for i in range(n):
        tirages.append(random.choice(valeurs))
    print(n, f"{sum(tirages) / len(tirages):.2f}")

# Exercice 7 - graphique de stabilisation
moyennes_simulees = []
for n in tailles:
    tirages = []
    for i in range(n):
        tirages.append(random.choice(valeurs))
    moyenne_n = sum(tirages) / len(tirages)
    moyennes_simulees.append(moyenne_n)

plt.figure()
plt.plot(tailles, moyennes_simulees, marker="o")
plt.axhline(moyenne_initiale, linestyle="--")
plt.xlabel("Nombre de tirages")
plt.ylabel("Moyenne simulee")
plt.tight_layout()
plt.savefig("simulation_moyenne.png", dpi=300)
plt.close()

# Exercice 8 - interpretation economique
# La moyenne de l'extrait resume les dix valeurs choisies, pas le monde entier.
# Quand le nombre de tirages augmente, la moyenne simulee tend a se rapprocher
# de la moyenne de la liste utilisee pour tirer.
# Ce resultat ne decrit pas directement la population mondiale : les pays ne
# sont pas ponderes par leur population.
# La selection des pays influence donc fortement la moyenne observee.
