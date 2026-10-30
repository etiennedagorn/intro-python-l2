# Corrigés des cinq TD Python révisés

Les corrigés suivent les cinq énoncés effectivement proposés sur le site, en
version `TP_N_revise.pdf`. Les anciennes versions et la banque d’entraînement
distincte ne sont pas des TD supplémentaires dans ce parcours.

| TD | Exercices obligatoires | Questions facultatives | Démarches en pseudo-code |
| --- | ---: | ---: | ---: |
| TD1 : scripts, variables, listes | 12 | 10 | 2 |
| TD2 : boucles, conditions, proportions | 13 | 10 | 2 |
| TD3 : fonctions, comparaison de groupes | 13 | 10 | 2 |
| TD4 : graphiques, simulation | 11 | 10 | 2 |
| TD5 : mini-projet pandas | 13 | 10 | 2 |
| Total | **62** | **50** | **10** |

## Fichiers préparés

- `docs/corriges.html` et les cinq `docs/tdN-corrige.html` : explications,
  solutions repliables, résultats exécutés et interprétations.
- `docs/supports/corr/TDN_corrige.py`, `TDN_corrige.ipynb` et `TDN_complet.zip` :
  scripts commentés, notebooks exécutés et dossiers complets pour travailler
  hors connexion. Le lien historique du script TD1 reste valide.
- `docs/supports/corr/figures/` : 13 graphiques effectivement produits.
- `docs/supports/corr/data/` : trois CSV copiés sans modification, leurs sources
  et SHA-256, ainsi que les métadonnées consultées pour le PIB.
- `tools/corriges_tdN.py`, `construire_corriges.py`, `verifier_corriges.py` et
  `requirements-corriges.txt` : sources communes et construction vérifiée.
- `tools/verifier_site.py` : contrôle facultatif avec Chrome déjà installé et
  le paquet Python playwright ; aucune installation de navigateur nécessaire.
- Navigation de l’accueil et des cinq TD, styles accessibles et
  `MISE_EN_LIGNE.md` mis à jour. Aucun énoncé ni PDF modifié.

## Vérifications réalisées le 30 octobre 2026

- Python 3.13.7, pandas 2.3.3, matplotlib 3.10.7, NumPy 2.3.3.
- Cinq scripts exécutés séparément dans des dossiers neufs et cinq notebooks
  exécutés de haut en bas dans cinq noyaux Jupyter neufs, sans réseau.
- Contrôles numériques : résultats des TD1 à TD5, alignement des populations
  sur le CSV, seuils 5 et 10, compteurs et proportions, médianes paires et
  impaires, quartiles et écart-type descriptif, bornes des simulations,
  colonnes numériques, filtre annuel et pays, classement du top 10,
  colonnes des exports, fusion sans doublon sur une année commune.
- Les 13 images produites sont des PNG valides et les cinq ZIP sont intègres,
  avec les mêmes scripts et notebooks que les téléchargements individuels.
- Trois empreintes SHA-256 conformes aux CSV de référence.
- Les PDF publics correspondent exactement aux PDF révisés des séances ;
  contrôle des titres d’exercices dans les PDF et les sources LaTeX.
- Les 12 pages HTML du site passent le contrôle de 295 liens, ressources et
  ancres locaux, sans lien manquant ni identifiant dupliqué.
- Chrome : les cinq corrigés contrôlés en 1280 et 390 pixels, ouverture et
  fermeture au clavier, absence de débordement horizontal de la page,
  présence des téléchargements et chargement des graphiques. Captures
  relues pour les graphiques de simulation et le top 10 sur mobile.

## Ambiguïtés traitées sans modifier les énoncés

- **TD1 :** le Japon ajouté à l’exercice 6 donne sept pays, malgré la mention
  ultérieure de six. Moyenne retenue : 81,87 années. Les populations de
  l’extension proviennent du CSV local en 2021 et ne remplacent pas les
  valeurs pédagogiques de l’exercice 2.
- **TD2 :** après ajout du Brésil, 4 des 9 lignes dépassent strictement 5,
  soit 44,4 %. Le 62,5 % donné dans l’énoncé n’est qu’un exemple de phrase.
  France et World sont égaux à 4,7 dans l’extrait arrondi. World est conservé
  pour suivre l’énoncé et signalé comme agrégat ; sans lui, 4/8 pays dépassent 5.
- **TD3 :** une seule hauteur peut être répétée par matplotlib sur deux barres,
  sans exception. La médiane paire est adaptée avant l’ajout d’un septième pays.
  Les extensions réassemblent des valeurs déjà fournies et nomment explicitement
  le groupe élargi « Europe + États-Unis ». Le quartile utilise le rang
  plafond(n/4). La formule d’écart-type annoncée par l’enseignant n’étant pas
  jointe, la convention descriptive avec division par n est explicitée.
  La valeur extrême de l’expérience demandée est identifiée comme test fictif,
  sans attribution à un pays ni présentation comme donnée OWID.
- **TD4 :** aucune graine n’est imposée avant l’extension qui l’introduit.
  Les sorties obligatoires sont des exemples d’exécution. La convergence ne
  doit pas être monotone ; la moyenne de la liste n’est pas le taux mondial.
  La convention de l’intervalle avancé est annoncée et limitée au mécanisme
  de simulation, avec écart-type de sa distribution connue.
- **TD5 :** la dernière colonne du CSV local est la région, pas le PIB.
  Le renommage vise donc la colonne vérifiée `GDP per capita`. Les agrégats
  sont exclus du classement des pays et territoires. Le PIB s’arrête en
  2025, l’espérance de vie en 2023 : la fusion utilise 2023, avec 196 couples
  pays/territoire-année appariés, sans mélanger des années différentes.
- La date du téléchargement initial des CSV n’est pas documentée ; aucune
  date n’est inventée. Les empreintes identifient les fichiers utilisés.

## Publication et maintenance

Point d’entrée des corrigés :
<https://etiennedagorn.github.io/intro-python-l2/corriges.html>.
Les cinq pages suivent le format `td1-corrige.html` à `td5-corrige.html`.
La publication utilise le dépôt et le GitHub Pages existants, sans changer
leurs paramètres. Le résultat effectif du push et des vérifications publiques
est indiqué dans le compte rendu de livraison.

Voir `MISE_EN_LIGNE.md` pour reconstruire et publier une mise à jour.
