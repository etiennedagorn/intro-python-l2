#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TP3 revise - corrige minimal aligne sur l'enonce actif.

Objectif : fonctions, tests simples, statistiques descriptives et comparaison.
"""

# Exercice 1 - donnees
groupe_europe = [46.0, 54.0, 34.0, 38.0, 22.0, 61.0]
groupe_monde = [46.0, 76.0, 19.0, 10.0, 7.0, 3.0]

pays_europe = ["France", "Germany", "Spain", "Italy", "Poland", "Sweden"]
pays_monde = ["France", "United States", "China", "Brazil", "India", "Ethiopia"]

print("Europe :", pays_europe)
print("Monde :", pays_monde)

# Exercice 2 - rappel intuitif
# La moyenne resume un niveau general.
# La mediane est la valeur centrale apres tri.
# Min et max donnent l'etendue des valeurs observees.

# Exercice 3 - lire une fonction
def ajouter_trois(x):
    resultat = x + 3
    return resultat


print(ajouter_trois(10))
# Parametre : x. Argument : 10. return renvoie ; print affiche.

# Exercice 4 - fonction moyenne
def moyenne(valeurs):
    return sum(valeurs) / len(valeurs)


print("Test moyenne attendu 12.0 :", moyenne([10, 12, 14]))
moy_europe = moyenne(groupe_europe)
moy_monde = moyenne(groupe_monde)
print(f"Moyenne Europe : {moy_europe:.1f} milliers de dollars par habitant")
print(f"Moyenne monde : {moy_monde:.1f} milliers de dollars par habitant")

# Exercice 5 - mediane paire
def mediane_paire(valeurs):
    valeurs_triees = sorted(valeurs)
    n = len(valeurs_triees)
    milieu_droit = n // 2
    milieu_gauche = milieu_droit - 1
    return (valeurs_triees[milieu_gauche] + valeurs_triees[milieu_droit]) / 2


print("Test mediane attendu 11.0 :", mediane_paire([8, 10, 12, 14]))
med_europe = mediane_paire(groupe_europe)
med_monde = mediane_paire(groupe_monde)
print(f"Mediane Europe : {med_europe:.1f}")
print(f"Mediane monde : {med_monde:.1f}")

# Exercice 6 - debogage de fonction
# moyenne_bug : NameError, car valeur n'existe pas ; il faut valeurs.
# moyenne_sans_return : la fonction affiche mais renvoie None ; print(m + 1) cause TypeError.

# Exercice 7 - min, max, proportion
def proportion_au_dessus(valeurs, seuil):
    compteur = 0
    for valeur in valeurs:
        if valeur > seuil:
            compteur = compteur + 1
    return compteur / len(valeurs) * 100


min_europe = min(groupe_europe)
max_europe = max(groupe_europe)
part_europe = proportion_au_dessus(groupe_europe, 30)

min_monde = min(groupe_monde)
max_monde = max(groupe_monde)
part_monde = proportion_au_dessus(groupe_monde, 30)

# Exercice 8 - tableau texte
print("groupe | moyenne | mediane | min | max | part_au_dessus_30")
print(f"Europe | {moy_europe:.1f} | {med_europe:.1f} | {min_europe:.1f} | {max_europe:.1f} | {part_europe:.1f} %")
print(f"Monde  | {moy_monde:.1f} | {med_monde:.1f} | {min_monde:.1f} | {max_monde:.1f} | {part_monde:.1f} %")

# Exercice 9 - interpretation
# Le groupe Europe a la moyenne la plus elevee dans cet extrait.
# Le groupe Europe a aussi la mediane la plus elevee.
# Moyenne et mediane peuvent diverger lorsque quelques valeurs extremes tirent la moyenne.
# Le choix des pays influence fortement le resultat.
# Six pays par groupe ne suffisent pas a decrire tous les pays du monde.
