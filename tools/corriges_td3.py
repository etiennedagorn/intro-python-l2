from corriges_common import exercice as e

INTRO = "Les valeurs sont les extraits arrondis de l’énoncé, en milliers de dollars internationaux par habitant. Le groupe nommé Monde est une sélection de six pays, pas une moyenne mondiale. Les fonctions obligatoires supposent des listes non vides ; mediane_paire suppose une longueur paire."

EXERCICES = [
e(1, "Créer et documenter les deux groupes.", "Conserver l’ordre des pays et des valeurs pour savoir à quel pays correspond chaque montant.", '''
groupe_europe = [46.0, 54.0, 34.0, 38.0, 22.0, 61.0]
groupe_monde = [46.0, 76.0, 19.0, 10.0, 7.0, 3.0]
pays_europe = ["France", "Germany", "Spain", "Italy", "Poland", "Sweden"]
pays_monde = ["France", "United States", "China", "Brazil", "India", "Ethiopia"]
print(pays_europe, groupe_europe)
print(pays_monde, groupe_monde)
''', "Deux groupes de six pays, avec France présente dans les deux. Les observations des groupes ne sont donc pas toutes distinctes."),
e(2, "Prédire les opérations avant de créer des fonctions.", "Vérifier d’abord les données sur des opérations connues : longueur, somme, tri et comparaison.", '''
print(len(groupe_europe))
print(sum(groupe_monde))
print(sorted(groupe_monde))
print(groupe_europe[0] > groupe_monde[0])
# Ces contrôles permettent de séparer une erreur de données d'une erreur
# dans la fonction que l'on écrira ensuite.
''', "6 ; 161.0 ; [3.0, 7.0, 10.0, 19.0, 46.0, 76.0] ; False, car 46.0 égale 46.0."),
e(3, "Rappeler le sens des statistiques.", "Décrire ce que chaque mesure résume avant d’écrire son calcul.", '''
# La moyenne additionne les valeurs et divise par leur nombre : niveau moyen.
# La médiane partage la liste triée en deux moitiés ; si la longueur est
# paire, on prend ici la moyenne des deux valeurs centrales.
# Le minimum et le maximum donnent les bornes des valeurs observées ;
# leur différence est l'étendue.
''', "La moyenne est sensible aux grandes valeurs ; la médiane renseigne sur le centre de la liste triée."),
e(4, "Lire une définition et un appel de fonction.", "Une fonction est définie avant son appel. Elle calcule une valeur et return la rend disponible pour la suite.", '''
def ajouter_trois(x):
    resultat = x + 3
    return resultat

print(ajouter_trois(10))
# Paramètre : x ; argument de cet appel : 10.
# return resultat renvoie 13 ; print(...) affiche 13.
''', "13."),
e(5, "Convertir des milliers de dollars en dollars.", "Un millier vaut 1000 unités. Après changement du nom ou du paramètre, modifier aussi les endroits qui l’utilisent.", '''
def convertir_en_dollars(valeur_milliers):
    return valeur_milliers * 1000

print(convertir_en_dollars(46.0))

# Variante demandée : nouveau nom et nouveau paramètre cohérents.
def milliers_vers_dollars(montant):
    return montant * 1000

print(milliers_vers_dollars(46.0))
''', "46000.0 dans les deux cas ; changer seulement l’appel provoquerait NameError."),
e(6, "Écrire et tester la fonction moyenne.", "La liste donnée en argument devient valeurs pendant l’appel. Vérifier un résultat facile avant les groupes du TD.", '''
def moyenne(valeurs):
    return sum(valeurs) / len(valeurs)

print("Test attendu 12.0 :", moyenne([10, 12, 14]))
moyenne_europe = moyenne(groupe_europe)
moyenne_monde = moyenne(groupe_monde)
print(f"Europe : {moyenne_europe:.2f} milliers de dollars par habitant")
print(f"Monde : {moyenne_monde:.2f} milliers de dollars par habitant")
''', "Test : 12.0 ; Europe : 42.50 ; Monde : 26.83.", "Une liste vide provoquerait une division par zéro. Ici les deux groupes ont six valeurs."),
e(7, "Calculer une médiane sur une liste de longueur paire.", "Trier sans modifier la liste originale. Pour six valeurs, les indices centraux sont 2 et 3, car les indices commencent à 0. // est la division entière.", '''
def mediane_paire(valeurs):
    valeurs_triees = sorted(valeurs)
    n = len(valeurs_triees)
    milieu_droit = n // 2
    milieu_gauche = milieu_droit - 1
    return (valeurs_triees[milieu_gauche] + valeurs_triees[milieu_droit]) / 2

print("Test attendu 11.0 :", mediane_paire([8, 10, 12, 14]))
mediane_europe = mediane_paire(groupe_europe)
mediane_monde = mediane_paire(groupe_monde)
print("Médianes Europe et Monde :", mediane_europe, mediane_monde)
''', "11.0 ; Europe : 42.0 ; Monde : 14.5.", "Cette fonction ne convient ni à une liste vide, ni à une longueur impaire. L’extension 1 propose l’adaptation."),
e(8, "Corriger un nom et un retour manquant.", "valeur et valeurs sont deux noms distincts. Une fonction sans return renvoie None même si elle affiche un nombre.", '''
# Premier bug : sum(valeur) utiliserait un nom non défini (NameError).
def moyenne_corrigee(valeurs):
    resultat = sum(valeurs) / len(valeurs)
    return resultat

# Deuxième bug : print seul ne renvoie pas le résultat à l'appelant.
def moyenne_avec_return(valeurs):
    return sum(valeurs) / len(valeurs)

m = moyenne_avec_return([10, 12, 14])
print(m + 1)
''', "13.0. Dans le fragment initial, None + 1 provoquerait TypeError après l’affichage de 12.0."),
e(9, "Calculer min, max et proportion au-dessus de 30.", "Écrire un compteur pour chaque groupe ; le seuil est strict. Les deux divisions ont pour dénominateur six.", '''
compteur_europe = 0
for valeur in groupe_europe:
    if valeur > 30:
        compteur_europe = compteur_europe + 1
part_europe = compteur_europe / len(groupe_europe) * 100

compteur_monde = 0
for valeur in groupe_monde:
    if valeur > 30:
        compteur_monde = compteur_monde + 1
part_monde = compteur_monde / len(groupe_monde) * 100

print("Europe min, max :", min(groupe_europe), max(groupe_europe))
print("Monde min, max :", min(groupe_monde), max(groupe_monde))
print(f"Parts au-dessus de 30 : Europe {part_europe:.2f} %, Monde {part_monde:.2f} %")
''', "Europe : min 22, max 61, 5/6 = 83.33 % ; Monde : min 3, max 76, 2/6 = 33.33 %."),
e(10, "Tracer les moyennes puis les médianes.", "Appeler les fonctions déjà testées et placer deux résultats face aux deux noms de groupes. Utiliser des fichiers différents pour comparer les deux versions.", '''
import matplotlib.pyplot as plt

groupes = ["Europe", "Monde"]
moyennes = [moyenne(groupe_europe), moyenne(groupe_monde)]
plt.figure()
plt.bar(groupes, moyennes)
plt.ylabel("Milliers de dollars internationaux par habitant")
plt.title("PIB par habitant moyen - extrait OWID")
plt.tight_layout()
plt.savefig("comparaison_pib_td3.png", dpi=300)
plt.show()
plt.close()

medianes = [mediane_paire(groupe_europe), mediane_paire(groupe_monde)]
plt.figure()
plt.bar(groupes, medianes)
plt.ylabel("Milliers de dollars internationaux par habitant")
plt.title("PIB par habitant médian - extrait OWID")
plt.tight_layout()
plt.savefig("comparaison_medianes_td3.png", dpi=300)
plt.show()
plt.close()
''', "Le groupe Europe dépasse le groupe Monde dans les deux figures. L’écart des médianes est plus grand que celui des moyennes."),
e(11, "Diagnostiquer deux graphiques trompeurs ou incomplets.", "Il faut une valeur calculée pour chacun des deux groupes et créer medianes avant son emploi. Attention : matplotlib peut répéter une valeur unique pour deux étiquettes sans signaler d’erreur.", '''
# A : fournir une seule moyenne risque de la répéter sur les deux barres.
moyennes = [moyenne(groupe_europe), moyenne(groupe_monde)]
print("Longueurs pour A :", len(groupes), len(moyennes))
# B : sans définition préalable, medianes provoquerait NameError.
# Ici elle existe déjà après l'exercice 10, mais il faut vérifier sa création.
medianes = [mediane_paire(groupe_europe), mediane_paire(groupe_monde)]
print("Données corrigées A et B :", moyennes, medianes)
# Les appels plt.bar(groupes, moyennes) et plt.bar(groupes, medianes)
# sont ceux des deux graphiques corrigés à l'exercice 10.
''', "Longueurs 2 et 2 ; moyennes [42.5, 26.833…] ; médianes [42.0, 14.5]. Le fragment A est une erreur de données, même s’il ne déclenche pas d’exception."),
e(12, "Afficher un tableau avec les six colonnes demandées.", "Une ligne par groupe, mêmes unités et mêmes arrondis. Aucun tableau pandas n’est nécessaire.", '''
print("groupe | moyenne | mediane | min | max | part_au_dessus_30")
print(f"Europe | {moyenne_europe:.2f} | {mediane_europe:.2f} | "
      f"{min(groupe_europe):.1f} | {max(groupe_europe):.1f} | {part_europe:.2f} %")
print(f"Monde | {moyenne_monde:.2f} | {mediane_monde:.2f} | "
      f"{min(groupe_monde):.1f} | {max(groupe_monde):.1f} | {part_monde:.2f} %")
# Les niveaux sont en milliers de dollars internationaux par habitant.
''', "Europe : 42.50 | 42.00 | 22.0 | 61.0 | 83.33 % ; Monde : 26.83 | 14.50 | 3.0 | 76.0 | 33.33 %. Le tableau affiché peut être copié dans le rendu."),
e(13, "Formuler cinq observations prudentes.", "Comparer les statistiques des deux sélections, sans transformer leur différence en résultat sur tous les pays.", '''
# Le groupe Europe a la moyenne la plus élevée : 42,50 contre 26,83.
# Il a aussi la médiane la plus élevée : 42,0 contre 14,5.
# Les grandes valeurs du groupe Monde tirent davantage sa moyenne vers le haut.
# Ajouter ou retirer un pays change ces résumés ; France est dans les deux groupes.
# Six pays par groupe ne forment pas un échantillon représentatif des continents
# ou du monde : la comparaison est descriptive et dépend du choix des pays.
''', "Les deux indicateurs classent ces groupes dans le même ordre, mais décrivent différemment leur répartition."),
]

EXTENSIONS = [
e(1, "Adapter les fonctions après ajout d’un septième pays.", "Utiliser des valeurs déjà données : ajouter United States au premier groupe et Italy au second. Le premier devient explicitement Europe + États-Unis. Une longueur impaire impose une nouvelle médiane qui prend la seule valeur centrale.", '''
groupe_europe_et_usa = groupe_europe + [76.0]
groupe_monde_et_italie = groupe_monde + [38.0]
# Les noms élargis évitent de présenter les États-Unis comme un pays européen.
pays_europe_et_usa = pays_europe + ["United States"]
pays_monde_et_italie = pays_monde + ["Italy"]

def mediane(valeurs):
    valeurs_triees = sorted(valeurs)
    n = len(valeurs_triees)
    milieu = n // 2
    if n % 2 == 0:  # Reste de la division par 2 : zéro signifie pair.
        return (valeurs_triees[milieu - 1] + valeurs_triees[milieu]) / 2
    return valeurs_triees[milieu]

print(moyenne(groupe_europe_et_usa), mediane(groupe_europe_et_usa))
print(moyenne(groupe_monde_et_italie), mediane(groupe_monde_et_italie))
''', "Médianes 46.0 et 19.0. moyenne reste correcte ; mediane_paire aurait renvoyé des résultats faux (42.0 et 14.5). Les groupes originaux sont conservés."),
e(2, "Calculer l’étendue des deux groupes.", "Soustraire la plus petite valeur à la plus grande.", '''
print("Étendue Europe :", max(groupe_europe) - min(groupe_europe))
print("Étendue Monde :", max(groupe_monde) - min(groupe_monde))
''', "39.0 et 73.0 milliers de dollars internationaux par habitant."),
e(3, "Créer une fonction de proportion.", "Compter les valeurs qui vérifient la condition puis renvoyer un pourcentage.", '''
def proportion_au_dessus(valeurs, seuil):
    compteur = 0
    for valeur in valeurs:
        if valeur > seuil:
            compteur = compteur + 1
    return compteur / len(valeurs) * 100

print(proportion_au_dessus(groupe_europe, 30))
print(proportion_au_dessus(groupe_monde, 30))
''', "83.33… % et 33.33… %. La fonction suppose une liste non vide."),
e(4, "Tester un seuil de 50.", "Changer seulement l’argument seuil.", '''
print(f"Europe > 50 : {proportion_au_dessus(groupe_europe, 50):.2f} %")
print(f"Monde > 50 : {proportion_au_dessus(groupe_monde, 50):.2f} %")
''', "Europe : 2/6 = 33.33 % ; Monde : 1/6 = 16.67 %."),
e(5, "Afficher un résumé avec une fonction.", "La fonction resume sert ici à afficher ; elle n’a pas de valeur numérique de retour à réutiliser.", '''
def resume(valeurs):
    print("Moyenne :", moyenne(valeurs))
    print("Médiane :", mediane(valeurs))
    print("Minimum :", min(valeurs))
    print("Maximum :", max(valeurs))

resume(groupe_europe)
resume(groupe_monde)
''', "On retrouve les statistiques du tableau. mediane est la fonction générale de l’extension 1."),
e(6, "Observer l’influence d’une valeur très élevée.", "L’énoncé demande une expérience : utiliser une valeur test égale à dix fois le maximum, sans l’attribuer à un pays ni la présenter comme une donnée OWID.", '''
valeur_test = max(groupe_monde) * 10  # Test fictif : aucun pays associé.
groupe_test = groupe_monde + [valeur_test]
print("Avant :", moyenne(groupe_monde))
print("Après ajout du test :", moyenne(groupe_test))
''', "La moyenne passe de 26.83 à 131.57. L’expérience illustre sa sensibilité à une valeur extrême ; le groupe original reste intact."),
e(7, "Calculer un premier quartile avec une convention annoncée.", "On choisit la méthode du rang plafond(n/4) : le premier quartile est la plus petite valeur atteignant au moins 25 % des observations triées. D’autres conventions interpolent et donnent des résultats différents.", '''
def premier_quartile(valeurs):
    valeurs_triees = sorted(valeurs)
    n = len(valeurs_triees)
    rang = (n + 3) // 4  # Plafond de n/4 pour un entier positif.
    return valeurs_triees[rang - 1]

print(premier_quartile(groupe_europe))
print(premier_quartile(groupe_monde))
''', "34.0 et 7.0 : rang 2 dans chaque liste de six valeurs. Toujours préciser la méthode de quartile."),
e(8, "Calculer un écart-type avec une formule explicite.", "La formule annoncée comme fournie par l’enseignant n’est pas jointe. À titre de convention descriptive, on choisit la racine de la moyenne des carrés des écarts à la moyenne, avec division par n. Ce n’est pas l’écart-type corrigé avec n−1.", '''
def ecart_type_descriptif(valeurs):
    centre = moyenne(valeurs)
    somme_carres = 0
    for valeur in valeurs:
        somme_carres = somme_carres + (valeur - centre) ** 2
    return (somme_carres / len(valeurs)) ** 0.5

print(f"Écart-type Europe : {ecart_type_descriptif(groupe_europe):.2f}")
print(f"Écart-type Monde : {ecart_type_descriptif(groupe_monde):.2f}")
''', "Résultats en milliers de dollars internationaux par habitant. Confirmer la convention avec l’enseignant si sa formule est distribuée séparément."),
e(9, "Interpréter la dispersion.", "Les carrés des distances à la moyenne augmentent quand les observations sont éloignées du centre.", '''
# Un écart-type plus grand indique des valeurs plus dispersées autour
# de leur moyenne ; il est exprimé dans la même unité que les valeurs.
''', "L’écart-type ne mesure pas le niveau moyen ; deux groupes peuvent avoir la même moyenne et des dispersions différentes."),
e(10, "Convertir les deux listes en dollars.", "Réutiliser la fonction de conversion dans des boucles simples.", '''
europe_dollars = []
for valeur in groupe_europe:
    europe_dollars.append(convertir_en_dollars(valeur))
monde_dollars = []
for valeur in groupe_monde:
    monde_dollars.append(convertir_en_dollars(valeur))
print(europe_dollars)
print(monde_dollars)
''', "Les niveaux sont multipliés par 1000 ; les proportions et le classement des pays restent identiques."),
]
