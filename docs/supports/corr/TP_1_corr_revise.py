#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TD1 - Correction

Objectif :
- créer et manipuler quelques variables ;
- utiliser des listes ;
- calculer des statistiques simples ;
- produire un premier graphique ;
- apprendre à lire quelques erreurs fréquentes.

Le code reste volontairement simple :
on n'utilise ni boucle, ni fonction personnalisée, ni pandas.
"""


# ============================================================
# EXERCICE 1 - Préparer un dossier de travail
# ============================================================

# Cette première ligne permet simplement de vérifier
# que le script est bien sauvegardé et exécuté.
print("test TD1")

# À retenir :
# - le dossier courant est le dossier dans lequel on se trouve
#   lorsque l'on lance la commande Python ;
# - le fichier exécuté est le fichier .py indiqué dans la commande.
#
# Par exemple :
# python3 td1_nom_prenom.py


# ============================================================
# EXERCICE 2 - Premières variables économiques
# ============================================================

# Une variable associe un nom à une valeur.
# Ici, nous utilisons trois types de données différents :
# str   : texte
# int   : nombre entier
# float : nombre avec des décimales

pays = "France"
annee = 2021
esperance_vie = 82.5
population_millions = 67.7

# type() permet de connaître le type d'une variable.
print(pays, type(pays))
print(annee, type(annee))
print(esperance_vie, type(esperance_vie))
print(population_millions, type(population_millions))

# Une f-string permet d'insérer directement
# la valeur des variables dans une phrase.
print(
    f"En {annee}, {pays} compte environ "
    f"{population_millions} millions d'habitants."
)


# ============================================================
# EXERCICE 3 - Prédire puis modifier une affectation
# ============================================================

population_millions = 67.7
population_millions = 68.0

# Python affiche 68.0.
# La deuxième affectation a remplacé la première valeur.
print(population_millions)

# Pour obtenir 68.2, il suffit de modifier
# la deuxième affectation :
population_millions = 68.2

print(population_millions)


# ============================================================
# EXERCICE 4 - Premier débogage guidé
# ============================================================

# ERREUR 1
#
# print("Bonjour"
#
# Python produit une SyntaxError car il manque
# la parenthèse fermante.
#
# Correction :
print("Bonjour")


# ERREUR 2
#
# print(pay)
#
# Python produit une NameError :
# aucune variable appelée "pay" n'a été créée.
# La variable s'appelle "pays".
#
# Correction :
print(pays)


# ERREUR 3
#
# print("Population : " + population_millions)
#
# Python produit une TypeError :
# on essaie d'additionner du texte (str)
# et un nombre décimal (float).
#
# Une solution simple consiste à transformer
# le nombre en texte avec str().
print("Population : " + str(population_millions))

# On pourrait aussi utiliser une f-string :
print(f"Population : {population_millions}")


# ============================================================
# EXERCICE 5 - Créer un extrait OWID simplifié
# ============================================================

# Nous remplaçons maintenant la variable "pays",
# qui contenait un seul texte, par une LISTE de pays.
#
# Les deux listes sont alignées :
# pays[0] correspond à esperance_vie[0],
# pays[1] correspond à esperance_vie[1], etc.

pays = [
    "France",
    "Germany",
    "Spain",
    "Italy",
    "Poland",
    "Sweden"
]

esperance_vie = [
    82.5,
    80.6,
    83.0,
    82.9,
    76.5,
    83.1
]

# En Python, le premier élément porte l'indice 0.
print("Premier pays :", pays[0])

# L'indice -1 désigne le dernier élément.
print("Dernière espérance de vie :", esperance_vie[-1])

# len() compte le nombre d'éléments d'une liste.
print("Nombre de pays :", len(pays))

# esperance_vie[10]
#
# Cette instruction produirait une IndexError.
# La liste ne contient que 6 valeurs :
# les indices disponibles vont donc de 0 à 5.


# ============================================================
# EXERCICE 6 - Modifier une liste sans la désaligner
# ============================================================

# append() ajoute un élément à la fin d'une liste.
pays.append("Japan")
esperance_vie.append(84.5)

print("Nombre de pays :", len(pays))
print(
    "Nombre de valeurs d'espérance de vie :",
    len(esperance_vie)
)

# On vérifie que les deux listes ont la même longueur.
# Le symbole == signifie "est égal à ?".
print(
    "Les deux listes ont la même longueur :",
    len(pays) == len(esperance_vie)
)

# Si l'on supprimait 84.5 de la liste esperance_vie
# sans supprimer "Japan" de la liste pays,
# les deux listes ne seraient plus alignées.
#
# On ne saurait alors plus quelle valeur correspond au Japon.
#
# Il faut donc toujours conserver le même nombre
# d'éléments dans les deux listes.


# ============================================================
# EXERCICE 7 - Moyenne, minimum et maximum
# ============================================================

# len() donne le nombre d'observations.
n = len(esperance_vie)

# sum() additionne les valeurs.
# Pour calculer la moyenne :
# somme des valeurs / nombre de valeurs.
moyenne = sum(esperance_vie) / n

# min() donne la plus petite valeur.
minimum = min(esperance_vie)

# max() donne la plus grande valeur.
maximum = max(esperance_vie)

print("Nombre d'observations :", n)

# :.1f permet d'afficher une seule décimale.
print(f"Moyenne : {moyenne:.1f} années")
print(f"Minimum : {minimum:.1f} années")
print(f"Maximum : {maximum:.1f} années")


# ============================================================
# EXERCICE 8 - Premier graphique avec matplotlib
# ============================================================

# matplotlib est une bibliothèque permettant
# notamment de créer des graphiques.
import matplotlib.pyplot as plt

# On crée une nouvelle figure.
plt.figure()

# pays donne les catégories de l'axe horizontal.
# esperance_vie donne la hauteur des barres.
plt.bar(pays, esperance_vie)

# On ajoute des informations permettant
# de comprendre le graphique.
plt.ylabel("Années")
plt.title("Espérance de vie - extrait OWID")

# On incline les noms des pays pour qu'ils restent lisibles.
plt.xticks(rotation=45, ha="right")

# Cette instruction évite que certains éléments
# dépassent de la figure.
plt.tight_layout()

# Le graphique est enregistré dans le dossier courant.
plt.savefig("esperance_vie_td1.png", dpi=300)


# ============================================================
# EXERCICE 9 - Modifier le graphique
# ============================================================

# On crée une NOUVELLE figure.
# Les données restent exactement les mêmes.
plt.figure()

plt.bar(pays, esperance_vie)

# Ici, on modifie seulement la présentation.
plt.ylabel("Espérance de vie en années")
plt.title("Espérance de vie dans sept pays")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# On choisit un autre nom pour ne pas écraser
# le premier graphique.
plt.savefig("esperance_vie_td1_version2.png", dpi=300)


# ============================================================
# EXERCICE 10 - Pourcentage d'évolution
# ============================================================

france_2000 = 79.1
france_2021 = 82.5

# Première étape :
# calculer la variation en années.
variation = france_2021 - france_2000

# Deuxième étape :
# rapporter cette variation à la valeur de départ.
taux_evolution = variation / france_2000 * 100

print(
    f"Variation France 2000-2021 : "
    f"{variation:.1f} années"
)

print(
    f"Taux d'évolution France 2000-2021 : "
    f"{taux_evolution:.2f} %"
)


# ============================================================
# EXERCICE 11 - Interpréter les résultats
# ============================================================

# 1. Dans cet extrait de sept pays,
#    l'espérance de vie moyenne est d'environ 81,9 années.

# 2. Avec 82,5 années, la France se situe au-dessus
#    de la moyenne de cet extrait.

# 3. Cet extrait ne contient que sept pays :
#    il ne permet donc pas de décrire l'ensemble du monde.
#    Le résultat dépend des pays qui ont été sélectionnés.


# ============================================================
# EXERCICE 12 - Contrôle final
# ============================================================

print("Contrôle final : le script TD1 s'exécute sans erreur.")