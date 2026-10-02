#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TP2 revise - corrige minimal aligne sur l'enonce actif.

Objectif : boucles, conditions, compteurs, proportions et fonction simple.
"""

# Exercice 1 - observer un dictionnaire seul
obs = {"pays": "France", "co2_pc": 4.7}
print(obs["pays"])
print(obs["co2_pc"])

obs["co2_pc"] = 5.1
print("Valeur modifiee :", obs["co2_pc"])

# Exercice 2 - liste de dictionnaires
donnees = [
    {"pays": "France", "co2_pc": 4.7},
    {"pays": "Germany", "co2_pc": 7.9},
    {"pays": "Spain", "co2_pc": 5.0},
    {"pays": "Poland", "co2_pc": 8.4},
    {"pays": "United States", "co2_pc": 14.9},
    {"pays": "India", "co2_pc": 2.0},
    {"pays": "China", "co2_pc": 8.0},
    {"pays": "World", "co2_pc": 4.7},
]

print("Nombre d'observations :", len(donnees))
print("Premiere observation :", donnees[0])

# Exercice 3 - parcourir
for obs in donnees:
    print(f"{obs['pays']} : {obs['co2_pc']:.1f} tonnes par habitant")

# Exercice 4 - classer avec une condition
for obs in donnees:
    pays = obs["pays"]
    co2 = obs["co2_pc"]
    if co2 < 5:
        categorie = "faible"
    elif co2 < 10:
        categorie = "intermediaire"
    else:
        categorie = "eleve"
    print(pays, categorie)

# Exercice 5 - compteur et proportion
compteur = 0
for obs in donnees:
    if obs["co2_pc"] > 5:
        compteur = compteur + 1

proportion = compteur / len(donnees) * 100
print(f"{proportion:.1f} % des observations sont au-dessus du seuil.")

# Exercice 6 - fonction de classement
def classe_co2(valeur):
    if valeur < 5:
        return "faible"
    elif valeur < 10:
        return "intermediaire"
    else:
        return "eleve"


print(classe_co2(4.7))
print(classe_co2(7.9))
print(classe_co2(14.9))

for obs in donnees:
    print(obs["pays"], classe_co2(obs["co2_pc"]))

# Exercice 7 - debogage
# Fragment A : IndentationError, car une ligne dans la boucle doit etre indentee.
# Fragment B : NameError, car compteur doit etre initialise avant compteur = compteur + 1.
# Fragment C : IndentationError, car le corps du if doit etre indente.

# Exercice 8 - interpretation
# United States a la valeur la plus elevee dans cet extrait.
# La France est egale a la valeur mondiale dans les donnees fournies.
# 62,5 % des observations depassent 5 tonnes par habitant.
# Le CO2 par habitant ne doit pas etre confondu avec le CO2 total.

# Exercice 9 - controle final
print("Controle final : le script TP2 revise s'execute sans erreur.")
