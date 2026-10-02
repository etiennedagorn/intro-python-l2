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

# -------------------------
# EXERCICE 4 — CARRÉS
# -------------------------
print("\n" + "="*72)
print("EXERCICE 4 — Liste de carrés")
print("="*72)

carres_boucle = []                             # Liste vide pour accumuler les carrés
for n in range(1, 11):                         # range(1,11): 1..10 inclus
    carres_boucle.append(n**2)                 # Ajoute n^2 à la fin de la liste
carres_comp = [n**2 for n in range(1, 11)]     # Écriture compacte équivalente (compréhension)

print("Carrés (boucle)        :", carres_boucle)
print("Carrés (compréhension) :", carres_comp)

carres_pairs = [x for x in carres_comp if x % 2 == 0]  # Garde les carrés pairs (modulo 2 == 0)
print("Carrés pairs :", carres_pairs)

print("Somme des carrés :", sum(carres_comp))  # Somme de la liste (O(n))

couples = [(n, n**2) for n in range(1, 11)]    # BONUS : couples (n, n^2) pour tabulation
print("Couples (n, n^2) :", couples)

# -------------------------
# EXERCICE 5 — DICTIONNAIRE
# -------------------------
print("\n" + "="*72)
print("EXERCICE 5 — Dictionnaire simple")
print("="*72)

etudiant = {"nom": "Alice", "age": 22, "note": 14}   # 3 clés : 'nom','age','note'
print("Dictionnaire initial :", etudiant)

print("Nom :", etudiant["nom"], "| Note :", etudiant["note"])  # Accès direct par clé (KeyError si absente)

etudiant["note"] = etudiant["note"] + 1             # Met à jour la valeur associée à 'note'
print("Après +1 sur la note :", etudiant)

etudiant["present"] = True                          # Ajoute une nouvelle paire clé/valeur
print("Après ajout 'present' :", etudiant)

ville = etudiant.get("ville", "inconnue")           # get(..., défaut) évite l’exception si clé absente
print("Ville (avec get) :", ville)

if "note" in etudiant:                              # Vérifie existence avant pop
    note_unique = etudiant.pop("note")              # pop('note') renvoie l’ancienne note ET supprime la clé
    etudiant["notes"] = [note_unique, 15, 16]       # Remplace par une liste de notes
    moyenne_notes = sum(etudiant["notes"]) / len(etudiant["notes"])  # Moyenne de la liste
    print("Après transformation en 'notes' :", etudiant)
    print("Moyenne des notes :", round(moyenne_notes, 2))

# -------------------------
# EXERCICE 6 — LISTE DE DICTS
# -------------------------
print("\n" + "="*72)
print("EXERCICE 6 — Liste de dictionnaires")
print("="*72)

eleves = [                                           # Liste de 3 dictionnaires
    {"nom": "Alice", "notes": [14, 16, 13]},
    {"nom": "Bob",   "notes": [10, 12, 11]},
    {"nom": "Clara", "notes": [16, 16, 15]},
]

def moyenne_liste(L):                                # Déclare une fonction utilitaire
    """Retourne la moyenne de L ou None si L est vide."""
    return sum(L)/len(L) if len(L) > 0 else None     # Ternaire : retourne None si liste vide

for e in eleves:                                     # Parcourt chaque élève (dict)
    e["moyenne"] = moyenne_liste(e["notes"])         # Ajoute/écrase la clé 'moyenne' avec la valeur calculée

print("Élèves avec moyenne :")
for e in eleves:                                     # Boucle d’affichage
    print(f"  {e['nom']} -> {round(e['moyenne'], 2)}")

classement = sorted(                                 # Trie SANS modifier eleves (retourne une nouvelle liste)
    eleves,                                          # Itérable à trier
    key=lambda d: (-d["moyenne"], d["nom"])          # Clé de tri = tuple : 1) moyenne décroissante 2) nom croissant
)
print("Classement (moyenne décroissante, tie-break nom) :")
for i, e in enumerate(classement, start=1):          # enumerate(..., start=1) pour numéroter 1,2,3,...
    print(f"  {i}. {e['nom']} ({round(e['moyenne'], 2)})")

def ajouter_etudiant(liste, nom, notes):             # Fonction pour ajouter un élève proprement
    """Ajoute un étudiant correctement formaté dans la liste cible."""
    nom_propre = str(nom).strip().title()           # Nettoie puis met en "Nom Propre" (1re lettre majuscule)
    notes_propres = [float(x) for x in notes]        # Force les notes en float (robuste)
    moyenne = moyenne_liste(notes_propres)           # Calcule la moyenne
    liste.append({"nom": nom_propre, "notes": notes_propres, "moyenne": moyenne})  # Ajout structuré

ajouter_etudiant(eleves, "david", [12, 14, 13])      # Démonstration d’ajout
print("Après ajout de 'David' :", eleves)

# -------------------------
# EXERCICE 7 — COMPTEUR DE MOTS
# -------------------------
print("\n" + "="*72)
print("EXERCICE 7 — Comptage de mots")
print("="*72)

phrase = "Le vélo, c'est génial ! Le vélo et la mobilité, c'est important."  # Phrase d’exemple
print("Phrase :", phrase)

nettoyee = phrase.lower()                          # Normalise en minuscules

ponct = ",.;:!?"                                   # Petits signes de ponctuation à retirer
for p in ponct:                                    # Pour chaque signe...
    nettoyee = nettoyee.replace(p, " ")            # ...remplace par un espace (séparation)

mots = [m for m in nettoyee.split() if m]          # split() -> découpe en morceaux ; filtre les vides
compte = {}                                        # Dictionnaire vide pour compter
for m in mots:                                     # Parcourt chaque mot
    compte[m] = compte.get(m, 0) + 1               # Incrémente la fréquence (0 par défaut si absent)
print("Comptage des mots :", compte)

top3 = sorted(compte.items(), key=lambda kv: -kv[1])[:3]  # Trie par valeur (freq) décroissante et prend 3 premiers
print("Top 3 :", top3)

stopwords = {"le", "la", "les", "de", "du", "un", "une", "et", "à", "c'est"}  # Liste simple de mots vides
compte_filtre = {}                                  # Nouveau dictionnaire pour le comptage filtré
for m in mots:                                      # Recompte en ignorant les stopwords
    if m in stopwords:                              # Si le mot est à ignorer...
        continue                                    # ...passe au suivant
    compte_filtre[m] = compte_filtre.get(m, 0) + 1  # Sinon, incrémente normalement
print("Comptage (sans stopwords) :", compte_filtre)

# -------------------------
# MINI-PROJET — PANIER DE CONSOMMATION
# -------------------------
print("\n" + "="*72)
print("MINI-PROJET — Panier de consommation")
print("="*72)

quantites = {"riz": 2, "lait": 1, "oeufs": 6}
prix_2025 = {"riz": 2.10, "lait": 1.05, "oeufs": 0.32}
prix_2026 = {"riz": 2.35, "lait": 1.12, "oeufs": 0.36}

total_2025_boucle = 0
for produit, qte in quantites.items():
    sous_total = prix_2025[produit] * qte
    print(f"2025 - {produit}: {qte} x {prix_2025[produit]:.2f} = {sous_total:.2f} euros")
    total_2025_boucle += sous_total
print("Total 2025 (boucle) :", round(total_2025_boucle, 2), "euros")

def cout_panier(prix, quantites):
    """Renvoie le coût total du panier en euros."""
    total = 0
    for produit, qte in quantites.items():
        if produit not in prix:
            raise ValueError(f"Prix manquant pour le produit : {produit}")
        total += prix[produit] * qte
    return total

total_2025 = cout_panier(prix_2025, quantites)
total_2026 = cout_panier(prix_2026, quantites)
variation_euros = total_2026 - total_2025
taux_evolution = variation_euros / total_2025 * 100

print(f"Total 2025 : {total_2025:.2f} euros")
print(f"Total 2026 : {total_2026:.2f} euros")
print(f"Variation : {variation_euros:+.2f} euros")
print(f"Taux d'évolution : {taux_evolution:+.1f} %")
print("Interprétation : ce panier devient plus cher, mais trois produits ne décrivent pas toute l'inflation.")

# -------------------------
# EXERCICE 8 — FUSION DICTS
# -------------------------
print("\n" + "="*72)
print("EXERCICE 8 — Fusion de dictionnaires")
print("="*72)

p1 = {"pomme": 2, "pain": 1, "riz": 1}              # 1er panier : quantités
p2 = {"pomme": 1, "yaourt": 4, "riz": 2}            # 2e panier : quantités
print("p1 :", p1)
print("p2 :", p2)

p_total = {}                                        # Dico résultat
for k, v in p1.items():                             # Copie p1 -> p_total
    p_total[k] = v
for k, v in p2.items():                             # Puis ajoute p2
    if k in p_total:                                # Si clé déjà présente,
        p_total[k] += v                             # ...additionner les valeurs
    else:
        p_total[k] = v                              # Sinon, simple affectation
print("Fusion sommée :", p_total)

p_tries = sorted(p_total.items(), key=lambda kv: -kv[1])  # Trie par quantité décroissante
print("Tri décroissant :", p_tries)

def fusion(p, q, mode="somme"):                     # Fonction générique de fusion
    """
    Fusionne p et q :
      - 'somme'  : additionne quand clé commune
      - 'droite' : priorité aux valeurs de q
      - 'gauche' : priorité aux valeurs de p
    """
    r = {}                                          # Nouveau dict résultat
    for k, v in p.items():                          # Copie p dans r
        r[k] = v                                    #dans le dictionnaire r, mets la valeur v sous la clé k
    for k, v in q.items():                          # Pour chaque clé de q...
        if mode == "somme" and k in r:              # Cas "somme" ET conflit...
            r[k] += v                               # ...on additionne
        elif mode == "gauche" and k in r:           # Cas "gauche" ET conflit...
            continue                                # ...on garde la valeur de p (ne remplace pas)
        else:                                       # Sinon (mode "droite" ou nouvelle clé)...
            r[k] = v                                # ...on écrase / crée la clé
    return r                                        # Renvoie le dict fusionné

print("Fusion (somme)  :", fusion(p1, p2, "somme"))  # Démo mode "somme"
print("Fusion (droite) :", fusion(p1, p2, "droite")) # Démo mode "droite"
print("Fusion (gauche) :", fusion(p1, p2, "gauche")) # Démo mode "gauche"

# -------------------------
# EXERCICE 9 — FRÉQ. LETTRES
# -------------------------
print("\n" + "="*72)
print("EXERCICE 9 — Fréquence des lettres")
print("="*72)

mot = "banana-split"                                # Mot d’exemple (contient un tiret)
print("Mot :", mot)

freq = {}                                           # Dictionnaire lettre -> compteur
for ch in mot:                                      # Parcourt chaque caractère
    if not ch.isalpha():                            # Si ce n’est PAS une lettre...
        continue                                    # ...on ignore (tiret, espace, etc.)
    c = ch.lower()                                  # Normalise la casse (tout en minuscule)
    freq[c] = freq.get(c, 0) + 1                    # Incrémente le compteur pour cette lettre
print("Fréquences (lettres) :", freq)

tri_freq = sorted(freq.items(), key=lambda kv: -kv[1])  # Trie par fréquence décroissante
print("Tri par fréquence décroissante :", tri_freq)

# -------------------------
# EXERCICE 10 — CLASSEMENT
# -------------------------
print("\n" + "="*72)
print("EXERCICE 10 — Classement de notes")
print("="*72)

notes_dict = {"Alice": 14, "Bob": 10, "Clara": 16}  # Dictionnaire nom -> note
print("Dictionnaire :", notes_dict)

classement = sorted(notes_dict.items(),             # items() -> paires (nom, note)
                    key=lambda kv: -kv[1])          # clé de tri = note (kv[1]) décroissante
print("Tri (nom, note) par note décroissante :", classement)

premier = classement[0]                             # Tuple du premier (meilleure note)
dernier = classement[-1]                            # Tuple du dernier (moins bonne note)
print("Premier :", premier, "| Dernier :", dernier)

def top_k(d, k):                                    # Fonction utilitaire
    """Retourne les k premiers (nom, note) par note décroissante."""
    tr = sorted(d.items(), key=lambda kv: -kv[1])   # Trie décroissant
    return tr[:k]                                   # Coupe la liste aux k premiers

print("Top 2 :", top_k(notes_dict, 2))              # Démo : top 2

# -------------------------
# EXERCICE 11 — INVENTAIRE
# -------------------------
print("\n" + "="*72)
print("EXERCICE 11 — Inventaire (prix & stock)")
print("="*72)


inventaire = {                                      # Dictionnaire imbriqué : produit -> (prix, stock)
  "pomme": {"prix": 0.5, "stock": 20},
  "pain":  {"prix": 1.2, "stock": 10},
  "riz":   {"prix": 2.0, "stock": 5}
}
print("Inventaire initial :", inventaire)


#inventaire.items() renvoie des paires (clé, valeur) :
#produit reçoit la clé (ex. "pomme"),
#infos reçoit le sous-dictionnaire (ex. {"prix": 0.5, "stock": 20}).
#À chaque tour : on calcule prix × stock du produit et on l’ajoute à valeur.

valeur = 0.0                                        # Accumulateur flottant
for produit, infos in inventaire.items():           # Parcourt chaque (clé, valeur)
    valeur += infos["prix"] * infos["stock"]        # Ajoute la valeur du stock (prix*stock)
print("Valeur totale :", round(valeur, 2))          # Arrondi 2 décimales


#Ce bloc vérifie d’abord qu’une commande est exécutable avant de modifier l’inventaire : 
# on parcourt chaque ligne produit → quantité de commande et, pour chacune, on contrôle que le produit existe dans inventaire et que le stock disponible est suffisant (inventaire[prod]["stock"] ≥ qte). 
# Au premier problème (produit absent ou stock insuffisant), on met le drapeau ok à False, on affiche un message d’erreur et on interrompt la vérification avec break, 
# ce qui évite d’appliquer une sortie de stock partielle. Si, après cette phase de contrôle, ok vaut toujours True, on refait un passage sur la commande pour décrémenter les stocks correspondants, puis on affiche l’inventaire mis à jour. Autrement dit, la logique sépare bien une phase de validation (tout doit passer) d’une phase d’exécution (on met à jour uniquement si tout était valide).


commande = {"pomme": 3, "riz": 2}                   # Commande à exécuter
ok = True                                           # Drapeau de validité
for prod, qte in commande.items():                  # Parcourt chaque ligne de commande
    if prod not in inventaire or inventaire[prod]["stock"] < qte:  # Si produit absent ou stock insuffisant
        ok = False                                  # On invalide la commande
        print(f"Stock insuffisant pour '{prod}' (demandé {qte})")  # Message d’erreur
        break                                       # On arrête la vérification

if ok:                                              # Si tout est OK...
    for prod, qte in commande.items():              # ...on applique la sortie de stock
        inventaire[prod]["stock"] -= qte            # Dé décrémente le stock
    print("Commande effectuée. Inventaire mis à jour :", inventaire)

inventaire["riz"]["prix"] *= 0.9                    # Remise -10% : multiplie par 0.9
print("Après remise 10% sur riz :", inventaire)

valeur2 = sum(v["prix"] * v["stock"]                # Recalcule la nouvelle valeur totale
              for v in inventaire.values())
print("Nouvelle valeur totale :", round(valeur2, 2))

classement_valeur = sorted(                         # Classe les produits par valeur de stock (prix*stock)
    inventaire.items(),                             # items() -> (produit, dict{"prix","stock"})
    key=lambda kv: -(kv[1]["prix"] * kv[1]["stock"])# Trie décroissant par valeur du stock
)
print("Tri par valeur de stock décroissante :", classement_valeur)

# -------------------------
# EXERCICE 12 — TRANSACTIONS
# -------------------------
print("\n" + "="*72)
print("EXERCICE 12 — Petites stats sur transactions")
print("="*72)

tx = [                                              # Liste d’événements (dictionnaires)
  {"nom": "Alice", "montant": 12.5},
  {"nom": "Bob",   "montant": 7.0},
  {"nom": "Alice", "montant": 3.5},
  {"nom": "Clara", "montant": 20.0}
]
print("Transactions :", tx)

totaux = {}                                         # Dico nom -> total dépensé
for t in tx:                                        # Parcourt chaque transaction
    nm = t["nom"]                                   # Récupère le nom
    mt = t["montant"]                               # Récupère le montant
    totaux[nm] = totaux.get(nm, 0) + mt             # Incrémente le cumul (0 par défaut)
print("Total par personne :", totaux)

classement_depense = sorted(                        # Classement par total décroissant
    totaux.items(), key=lambda kv: -kv[1]
)
print("Classement par dépense décroissante :", classement_depense)
if classement_depense:                              # Sécurité si liste non vide
    print("Top 1 :", classement_depense[0])         # Affiche le premier de liste

stats = {}                                          # Dico nom -> {nb, total, (puis moyen)}
for t in tx:                                        # Re-boucle pour compter nb d’achats et totaux
    nm, mt = t["nom"], t["montant"]
    if nm not in stats:                             
        stats[nm] = {"nb": 0, "total": 0.0}        # Initialise la structure à la première rencontre
    stats[nm]["nb"] += 1                            # +1 achat
    stats[nm]["total"] += mt                        # +montant

for nm, st in stats.items():                        # Post-traitement : calcule la moyenne par personne
    st["moyen"] = st["total"] / st["nb"]            # Ajoute une clé 'moyen' = total / nb
print("Stats nb achats & montant moyen :", stats)

# -------------------------
# EXERCICE 13 — FONCTIONS
# -------------------------
print("\n" + "="*72)
print("EXERCICE 13 — Fonctions utilitaires (liste de nombres)")
print("="*72)

def moyenne(L):                                     # Définit la moyenne robuste
    """Moyenne arithmétique ou None si L est vide."""
    return sum(L)/len(L) if len(L) > 0 else None

def mediane(L):                                     # Définit la médiane
    """
    Médiane :
      - n impair : élément du milieu
      - n pair   : moyenne des deux du milieu
    """
    T = sorted(L)                                   # Copie triée (ne modifie pas L)
    n = len(T)                                      # Longueur
    if n == 0:                                      # Cas vide
        return None
    mid = n // 2                                    # Milieu entier (division entière)
    if n % 2 == 1:                                  # Si impair...
        return T[mid]                               # ...prend l’élément central
    else:                                           # Si pair...
        return (T[mid - 1] + T[mid]) / 2           # ...moyenne des deux du milieu

def mode(L):                                        # Définit le mode
    """
    Mode(s) : valeur(s) la(les) plus fréquente(s).
    None si liste vide. Si ex aequo, renvoie une liste.
    """
    if len(L) == 0:                                 # Cas vide
        return None
    compte = {}                                     # Compteur de fréquences
    for x in L:                                     # Parcours des valeurs
        compte[x] = compte.get(x, 0) + 1            # Incrémente
    fmax = max(compte.values())                     # Fréquence maximale
    modes = [k for k, v in compte.items() if v == fmax]  # Toutes les valeurs au max
    return modes[0] if len(modes) == 1 else modes   # Si 1 seul -> renvoie la valeur ; sinon la liste

tests = [[1, 2, 2, 3], [10], []]                    # Jeux de tests (cas normal, singleton, vide)
for L in tests:                                     # Boucle de tests
    print(f"L = {L}")
    print("  moyenne ->", moyenne(L))               # Affiche moyenne
    print("  mediane ->", mediane(L))               # Affiche médiane
    print("  mode    ->", mode(L))                  # Affiche mode(s)

# -------------------------
# EXERCICE 14 — GROUPEMENTS
# -------------------------
print("\n" + "="*72)
print("EXERCICE 14 — Groupements simples (sans pandas)")
print("="*72)

catalogue = [                                       # Liste d’articles (dict)
    {"categorie": "fruits",      "produit": "pomme",     "prix": 0.5},
    {"categorie": "fruits",      "produit": "banane",    "prix": 0.7},
    {"categorie": "boulangerie", "produit": "pain",      "prix": 1.2},
    {"categorie": "boulangerie", "produit": "croissant", "prix": 1.0},
    {"categorie": "epicerie",    "produit": "riz",       "prix": 2.2},
]

groupes = {}                                        # cat -> {nb:..., somme:...}
for item in catalogue:                              # Pour chaque produit...
    cat = item["categorie"]                         # ...récupère sa catégorie
    p   = item["prix"]                              # ...et son prix
    if cat not in groupes:                          # Si 1re fois qu’on voit cette catégorie...
        groupes[cat] = {"nb": 0, "somme": 0.0}      # ...initialise le compteur
    groupes[cat]["nb"]    += 1                      # +1 produit dans cette catégorie
    groupes[cat]["somme"] += p                      # +prix pour la somme

res_cat = []                                        # Liste de tuples résultat
for cat, stats in groupes.items():                  # Parcourt chaque catégorie agrégée
    prix_moy = stats["somme"] / stats["nb"]         # Calcule le prix moyen de la catégorie
    res_cat.append((cat, stats["nb"], prix_moy))    # Empile (catégorie, nb, prix_moyen)
print("Stats par catégorie (nb, prix moyen) :", res_cat)

res_tries = sorted(res_cat, key=lambda t: -t[2])    # Trie par prix moyen décroissant (index 2 du tuple)
print("Tri par prix moyen décroissant :", res_tries)

# -------------------------
# EXERCICE 15 — NETTOYAGE
# -------------------------
print("\n" + "="*72)
print("EXERCICE 15 — Nettoyage léger")
print("="*72)

prenoms_bruts = [" alice ", "Bob", "ALICE", "bob ", "  clara"]  # Contient espaces et doublons
print("Brut :", prenoms_bruts)

def nom_propre(s):                                  # Déclare une petite fonction de normalisation
    """
    strip() : retire les espaces au début/fin
    lower() : passe en minuscules
    capitalize() : met 1re lettre en majuscule
    """
    s = s.strip()
    s = s.lower()
    return s.capitalize()

prenoms_nettoyes = [nom_propre(s) for s in prenoms_bruts]  # Applique la normalisation à chaque prénom
print("Nettoyés :", prenoms_nettoyes)

unique_ordre = []                                   # Liste pour conserver ordre d’apparition
for p in prenoms_nettoyes:                          # Parcourt les prénoms nettoyés
    if p not in unique_ordre:                       # Ajoute seulement s’il n’y est pas déjà
        unique_ordre.append(p)

unique_tries = sorted(unique_ordre)                 # Trie alphabétique final
print("Unique triée :", unique_tries)

print("\n— FIN DE LA CORRECTION COMMENTÉE (ligne par ligne) —\n")
