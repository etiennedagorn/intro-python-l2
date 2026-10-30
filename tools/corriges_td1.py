from corriges_common import exercice as e

INTRO = "Les exercices se suivent : le Japon ajouté à l’exercice 6 reste présent ensuite. Les statistiques portent donc sur sept pays. Aucun recours à pandas, aux boucles ou aux fonctions personnelles n’est nécessaire dans ce TD."

EXERCICES = [
e(1, "Créer, sauvegarder et exécuter un premier script.",
  "Créer le dossier TD1 dans l’explorateur de fichiers, l’ouvrir dans VS Code, puis enregistrer td1_nom_prenom.py dedans. Dans le terminal de ce dossier, lancer python3 td1_nom_prenom.py (ou py sous Windows). Modifier le message puis sauvegarder avant de relancer.", '''
# Le dossier courant est celui du terminal ; le fichier exécuté est le .py nommé.
print("test TD1")
# Après modification et sauvegarde, c'est ce nouveau message qui apparaît.
print("test TD1 modifié")
''', "Le terminal affiche les deux messages. Le fichier peut être enregistré dans un autre dossier que celui du terminal : vérifier le dossier courant si Python ne le trouve pas."),
e(2, "Afficher les quatre variables, leurs types et une phrase lisible.",
  "Les guillemets désignent du texte ; un nombre sans partie décimale est un entier. Une f-string insère les valeurs entre accolades.", '''
pays = "France"
annee = 2021
esperance_vie = 82.5
population_millions = 67.7
print(pays, type(pays))
print(annee, type(annee))
print(esperance_vie, type(esperance_vie))
print(population_millions, type(population_millions))
print(f"En {annee}, {pays} compte environ {population_millions} millions d'habitants.")
''', "Types attendus : str, int, float, float. La phrase contient 2021, France et 67.7 millions. Ce sont les valeurs pédagogiques de l’énoncé, sans mise à jour à partir du CSV."),
e(3, "Prédire l’effet d’une nouvelle affectation.",
  "Python lit les lignes dans l’ordre : la deuxième affectation remplace la première. Refaire ensuite l’essai en remplaçant seulement 68.0 par 68.2.", '''
population_millions = 67.7
population_millions = 68.0
# Prédiction : 68.0, car la deuxième ligne remplace 67.7.
print(population_millions)

population_millions = 67.7
population_millions = 68.2
print(population_millions)
''', "Premier essai : 68.0 ; deuxième essai : 68.2."),
e(4, "Identifier puis corriger trois erreurs.",
  "Tester les lignes fautives séparément. Le dernier mot du message indique le type d’erreur, et le numéro de ligne désigne la ligne à examiner dans votre fichier. La numérotation dépend de son contenu.", '''
# print("Bonjour" : SyntaxError sur cette ligne, parenthèse non fermée.
print("Bonjour")
# print(pay) : NameError sur cette ligne, nom absent ; le nom créé est pays.
print(pays)
# print("Population : " + population_millions) : TypeError sur cette ligne.
# La f-string accepte à la fois du texte et un nombre.
print(f"Population : {population_millions}")
''', "Les corrections affichent Bonjour, France et Population : 68.2. Les lignes fautives restent en commentaires pour permettre l’exécution complète."),
e(5, "Créer deux listes alignées et utiliser leurs indices.",
  "À une position donnée, le pays et son espérance de vie se correspondent. Le premier indice vaut 0 ; -1 désigne le dernier élément.", '''
pays = ["France", "Germany", "Spain", "Italy", "Poland", "Sweden"]
esperance_vie = [82.5, 80.6, 83.0, 82.9, 76.5, 83.1]
print("Premier pays :", pays[0])
print("Première valeur :", esperance_vie[0])
print("Dernière valeur :", esperance_vie[-1])
print("Nombre de pays :", len(pays))
# esperance_vie[10] provoquerait IndexError : seuls 0 à 5 sont disponibles.
''', "France ; 82.5 ; 83.1 ; 6 pays."),
e(6, "Ajouter le Japon et vérifier les longueurs.",
  "Ajouter un élément dans chacune des deux listes. Retirer temporairement la dernière valeur montre le désalignement ; la remettre avant la suite.", '''
pays.append("Japan")
esperance_vie.append(84.5)
print("Nombre de pays :", len(pays))
print("Nombre de valeurs :", len(esperance_vie))
print("Les deux listes ont la même longueur :", len(pays) == len(esperance_vie))

# Essai temporaire : le dernier élément est retiré avec pop().
esperance_vie.pop()
print("Pendant l'essai :", len(pays) == len(esperance_vie))
esperance_vie.append(84.5)  # Rétablir la correspondance avant le graphique.
''', "7 pays et 7 valeurs ; True, puis False pendant l’essai. Les deux listes retrouvent finalement 7 éléments.",
  "Une même longueur est nécessaire, mais l’ordre doit également rester identique : ne pas trier une seule des listes."),
e(7, "Calculer le nombre, la moyenne, le minimum et le maximum.",
  "Additionner les valeurs puis diviser par leur nombre. Le nombre d’observations est un effectif ; les trois autres résultats sont exprimés en années.", '''
nombre = len(esperance_vie)
moyenne = sum(esperance_vie) / nombre
minimum = min(esperance_vie)
maximum = max(esperance_vie)
print("Nombre d'observations :", nombre)
print(f"Moyenne : {moyenne:.2f} années")
print(f"Minimum : {minimum:.1f} années")
print(f"Maximum : {maximum:.1f} années")
''', "7 observations ; moyenne 81.87 années ; minimum 76.5 ; maximum 84.5. Sans l’ajout du Japon, la moyenne des six valeurs serait 81.43 années."),
e(8, "Enregistrer un premier graphique en barres.",
  "Les pays fournissent les étiquettes et les valeurs donnent la hauteur des barres. Incliner les noms et ajuster la mise en page évite qu’ils se chevauchent.", '''
import matplotlib.pyplot as plt

plt.figure()
plt.bar(pays, esperance_vie)
plt.ylabel("Années")
plt.title("Espérance de vie de sept pays - extrait OWID")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("esperance_vie_td1.png", dpi=300)
plt.show()
plt.close()
''', "Le fichier esperance_vie_td1.png contient sept barres. Le Japon a la valeur la plus élevée ; la Pologne la plus faible.",
  "Si matplotlib manque, installer la bibliothèque dans le même Python que celui qui exécute le script : python3 -m pip install matplotlib."),
e(9, "Changer la présentation en conservant les données.",
  "Créer une nouvelle figure et changer seulement le titre, le texte de l’axe et le fichier de sortie.", '''
plt.figure()
plt.bar(pays, esperance_vie)
plt.ylabel("Espérance de vie en années")
plt.title("Comparaison de sept pays : extrait pédagogique")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("esperance_vie_td1_version2.png", dpi=300)
plt.show()
plt.close()
''', "Deux fichiers PNG distincts existent ; les hauteurs des barres sont identiques."),
e(10, "Distinguer variation en années et taux d’évolution.",
  "Soustraire la valeur initiale de la valeur finale. Pour le pourcentage, diviser cette différence par la valeur initiale, puis multiplier par 100.", '''
france_2000 = 79.1
france_2021 = 82.5
variation = france_2021 - france_2000
taux_evolution = variation / france_2000 * 100
print(f"Variation : {variation:.2f} années")
print(f"Taux d'évolution : {taux_evolution:.2f} %")
''', "Variation : 3.40 années ; taux d’évolution : 4.30 %. Le taux n’est pas 3.40 % : les unités et les opérations diffèrent."),
e(11, "Écrire les trois phrases d’interprétation demandées.",
  "Utiliser la moyenne réellement calculée après l’exercice 6 et comparer 82.5 à cette valeur.", '''
# La moyenne simple de cet extrait de sept pays est de 81,87 années.
# La France, avec 82,5 années, se situe environ 0,63 année au-dessus.
# Ces sept pays choisis ne représentent pas le monde ; la moyenne n'est
# pas pondérée par la population et dépend de la sélection.
''', "L’énoncé mentionne encore six pays dans sa limite, mais l’exercice 6 en ajoute un septième. L’interprétation retient les sept pays effectivement présents."),
e(12, "Vérifier les éléments du rendu final.",
  "Relire les exercices 1 à 11 puis relancer le fichier entier depuis un terminal neuf. Contrôler aussi les deux images dans le dossier courant.", '''
# str : les noms de pays ; int : annee ; float : france_2021.
# list : esperance_vie ; moyenne : exercice 7 ; f-strings : exercices 2 et 7.
# Graphiques : exercices 8 et 9 ; évolution : exercice 10.
# Trois phrases d'interprétation : exercice 11.
print("Contrôle final : les exercices obligatoires du TD1 sont exécutés.")
''', "Le script complet se termine sans erreur et produit les deux figures. Aucun fragment volontairement fautif n’est exécuté."),
]

EXTENSIONS = [
e(1, "Ajouter le Japon une seule fois.", "L’ajout demandé a déjà été réalisé à l’exercice 6. Vérifier le dernier couple plutôt que dupliquer l’observation.", '''
print(pays[-1], esperance_vie[-1])
''', "Japan 84.5. Ajouter le Japon une deuxième fois lui donnerait un poids double."),
e(2, "Créer une liste de populations documentées.", "L’énoncé ne donne pas ces nombres. On utilise les effectifs de 2021 du CSV population.csv du dépôt, convertis en millions et rangés dans le même ordre que les pays. Ce fichier source est fourni avec le corrigé.", '''
# Source : population.csv du dépôt, année 2021 ; valeurs en millions.
populations_millions = [
    66.083547, 83.697080, 47.735670, 59.729353,
    38.040303, 10.416134, 125.679342
]
print("Populations en millions :", populations_millions)
print("Longueurs identiques :", len(pays) == len(populations_millions))
''', "Sept valeurs alignées de France à Japan. Le CSV donne 66.083547 millions pour la France ; cette série diffère de la valeur pédagogique 67.7 de l’exercice 2 et ne la remplace pas."),
e(3, "Calculer la population totale de l’extrait.", "Additionner les sept populations exprimées dans la même unité.", '''
population_totale = sum(populations_millions)
print(f"Population totale : {population_totale:.3f} millions")
''', "Le total porte sur ces sept pays en 2021 ; la sortie ci-dessous donne sa valeur calculée."),
e(4, "Calculer la part de la France dans le total.", "La France est à l’indice 0. Diviser sa population par le total puis multiplier par 100.", '''
part_france = populations_millions[0] / population_totale * 100
print(f"Part de la France : {part_france:.2f} %")
''', "Ce pourcentage concerne la population de l’extrait, pas la population mondiale."),
e(5, "Afficher un couple pays-valeur.", "Utiliser le même indice dans les deux listes.", '''
print(f"{pays[0]} : {esperance_vie[0]} années")
''', "France : 82.5 années."),
e(6, "Interpréter un booléen.", "Le signe > pose une question : la valeur dépasse-t-elle 80 ?", '''
print(esperance_vie[0] > 80)
''', "True : 82.5 est strictement supérieur à 80."),
e(7, "Observer l’effet d’un faux zéro.", "Faire une copie avec [:] pour préserver la liste originale, puis remplacer la valeur française par 0 uniquement dans cette expérience demandée.", '''
valeurs_test = esperance_vie[:]
valeurs_test[0] = 0  # Faux zéro : expérience de l'énoncé, pas donnée OWID.
print(f"Moyenne avec faux zéro : {sum(valeurs_test) / len(valeurs_test):.2f} années")
print(f"Moyenne initiale conservée : {moyenne:.2f} années")
''', "La moyenne tombe à 70.09 années. Un zéro est traité comme une observation réelle ; il ne représente pas une valeur manquante."),
e(8, "Nommer la source.", "Conserver le nom dans une chaîne et l’inclure dans une f-string.", '''
source = "Our World in Data"
print(f"Source des extraits pédagogiques : {source}")
''', "Source des extraits pédagogiques : Our World in Data."),
e(9, "Arrondir la moyenne.", "round renvoie un nombre arrondi ; le calcul précédent reste conservé dans moyenne.", '''
print(round(moyenne, 1))
''', "81.9."),
e(10, "Expliquer le rôle des unités.", "Un résultat chiffré a besoin de son unité pour être compris et comparé.", '''
# Une espérance de vie se mesure en années ; une population peut être en
# habitants ou en millions : mélanger ces unités fausse les comparaisons.
''', "Toujours préciser l’unité dans les axes, les phrases et les tableaux."),
]
