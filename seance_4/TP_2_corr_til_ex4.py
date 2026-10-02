# ============================================================
# TP2 – Correction LIGNE PAR LIGNE (super détaillée)
# Listes, dictionnaires, boucles, tris, fonctions utilitaires
# ============================================================

# -------------------------
# EXERCICE 1 — LISTE
# -------------------------
print("\n" + "="*72)                     # \n: saut de ligne ; "="*72 = répéter "=" 72 fois
print("EXERCICE 1 — Création d’une liste")  # Titre de section lisible à l’exécution
print("="*72)

etudiants = ["Alice", "Bob", "Clara", "David", "Emma"]  # Crée une liste (mutable, ordonnée)
print("Liste initiale :", etudiants)      # Affiche tout le contenu de la liste

print("Premier élément  :", etudiants[0]) # Index 0 = premier élément
print("Dernier élément  :", etudiants[-1])# Index -1 = dernier élément (comptage depuis la fin)

etudiants.append("Farid")                 # Ajoute "Farid" en fin de liste (in-place)
print("Après append('Farid') :", etudiants)

retire = etudiants.pop(1)                 # pop(1) enlève et RENVOIE l’élément d’indice 1
print(f"Après suppression du 2e ({retire}) :", etudiants)  # f-string pour interpoler la variable

etudiants.sort()                          # Trie alphabétiquement la liste (modifie l’objet)
print("Liste triée alphabétiquement :", etudiants)

longueur = len(etudiants)                 # len(...) = nombre d’éléments
print("Longueur de la liste :", longueur)

if "Alice" in etudiants:                  # Test d’appartenance : O(n)
    index_alice = etudiants.index("Alice")# Renvoie l’indice de la 1ère occurrence (ValueError si absent)
    print("Index de 'Alice' :", index_alice)
else:
    print("'Alice' n'est pas dans la liste.")

# BONUS : reconstruire une liste sans doublons SANS set() (conserve l’ordre d’apparition)
liste_avec_doublons = ["Alice", "Bob", "Bob", "Clara", "Alice", "Emma"]  # Démo de doublons
sans_doublons = []                           # Liste résultat, au départ vide
for nom in liste_avec_doublons:              # Parcourt chaque nom de la liste source
    if nom not in sans_doublons:             # Si on ne l’a pas déjà conservé...
        sans_doublons.append(nom)            # ...on l’ajoute
print("Sans doublons (sans set) :", sans_doublons)

# -------------------------
# EXERCICE 2 — MOYENNE
# -------------------------
print("\n" + "="*72)
print("EXERCICE 2 — Moyenne des notes")
print("="*72)

notes = [12, 14, 10, 8]                      # Liste de nombres (ints ici)
print("Notes :", notes)                       # Visualisation des données

if len(notes) > 0:                            # Toujours éviter la division par zéro
    moyenne = sum(notes) / len(notes)         # Moyenne arithmétique = somme / effectif
    print("Moyenne (arithmétique) :", round(moyenne, 1))  # round(...,1) : 1 décimale
else:
    print("Moyenne : liste vide, impossible à calculer")  # Cas limite : vide

if len(notes) > 0:                            # On réutilise 'moyenne' calculée ci-dessus
    sup_moy = [x for x in notes if x > moyenne]  # Compréhension de liste = filtre
    print("Notes > moyenne :", sup_moy)

if notes:                                     # Idiome Python : liste vide -> False
    print("Min :", min(notes), "| Max :", max(notes))  # Min/Max en O(n)
else:
    print("Min et Max : liste vide")

def ecart_type_population(L):                 # Définit une fonction (scope local)
    """Écart-type population (division par n). None si liste vide."""
    n = len(L)                                # Taille de l’échantillon
    if n == 0:                                # Sécurité : liste vide
        return None
    m = sum(L) / n                            # Moyenne
    var = sum((x - m) ** 2 for x in L) / n    # Variance population : moyenne des carrés des écarts
    return var ** 0.5                         # Racine carrée = écart-type

etp = ecart_type_population(notes)            # Appel de la fonction sur nos notes
if etp is None:                               # Test du cas vide
    print("Écart-type : liste vide, non défini")
else:
    print("Écart-type (population) :", round(etp, 3))  # Arrondi à 3 décimales

# -------------------------
# EXERCICE 3 — CHAINES
# -------------------------
print("\n" + "="*72)
print("EXERCICE 3 — Noms en majuscules")
print("="*72)

noms = ["alice", "Bob", "amélie", "clara", "ALAN", "emma"] # Mélange de casses/accents
print("Noms (bruts) :", noms)

noms_maj = [n.upper() for n in noms]           # upper() -> string en MAJUSCULE
print("Noms en MAJUSCULES :", noms_maj)

commencent_par_A = [n for n in noms            # Filtre tous les n ...
                    if len(n) > 0              # ... qui ne sont pas vides ET ...
                    and n[0].lower() == "a"]   # ... dont la 1re lettre (en minuscule) est 'a'
print("Commencent par 'A' :", commencent_par_A)

longueurs = [(n, len(n)) for n in noms]        # Crée des couples (nom, longueur)
print("Longueur de chaque prénom :", longueurs)

if noms:                                       # Vérifie qu’il y a au moins un nom
    plus_long = max(noms, key=len)             # max avec key=len renvoie la chaîne la plus longue
    print("Le plus long prénom :", plus_long, f"({len(plus_long)} caractères)")
