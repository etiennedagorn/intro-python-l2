# Mettre à jour le site du cours Python

Le site est en HTML et CSS dans `docs/`, sans framework ni compilation générale.
Le dépôt existant est `etiennedagorn/intro-python-l2`, branche `main` ; GitHub
Pages publie `docs/` à l’adresse <https://etiennedagorn.github.io/intro-python-l2/>.
Conserver cette procédure et les paramètres distants existants.

## Corrigés publics

Les cinq TD révisés disposent d’une page `docs/tdN-corrige.html`, accessible
depuis le TD et depuis `docs/corriges.html`. Les scripts, notebooks exécutés,
figures et dossiers ZIP sont dans `docs/supports/corr/`.

Les contenus à publier sont les supports du cours et les corrigés explicitement
préparés pour les étudiants. Les listes d’inscription, rendus étudiants et
anciens fichiers personnels restent hors du site.

## Reconstruire et vérifier les corrigés

Depuis `01_cours`, créer un environnement de construction :

```bash
python3 -m venv /tmp/corriges-venv
/tmp/corriges-venv/bin/python -m pip install -r tools/requirements-corriges.txt
/tmp/corriges-venv/bin/python tools/construire_corriges.py
```

Les contenus pédagogiques se trouvent dans `tools/corriges_td1.py` à
`tools/corriges_td5.py`. Modifier ces sources puis reconstruire, plutôt que
d’éditer séparément le HTML, le script et le notebook.

Pour modifier uniquement la présentation et réutiliser les sorties déjà
validées, sans réexécuter Python ni modifier les téléchargements :

```bash
/tmp/corriges-venv/bin/python tools/construire_corriges.py --rendu-seul
```

Ce mode vérifie que les cellules du notebook correspondent aux sources.
Si le code ou les explications pédagogiques changent, refaire la construction
complète avec exécution.

La construction :

- vérifie les titres et le nombre d’exercices avec les cinq `TP_N_revise.tex` ;
- exécute chaque script dans un dossier neuf avec ses seules données ;
- exécute chaque notebook dans un nouveau noyau Jupyter, de haut en bas ;
- vérifie les résultats numériques, les seuils, les exports et les images ;
- génère le HTML statique, les scripts, notebooks et ZIP ;
- contrôle les liens locaux et les ancres de toutes les pages HTML du site.

Les CSV de référence sont inclus dans `docs/supports/corr/data/`. Ils sont copiés
sans modification depuis les fichiers de travail du cours ; leurs sources et
SHA-256 sont dans `provenance.json`. Leur date initiale de téléchargement n’est
pas connue. La construction ne les télécharge pas à nouveau.
Les métadonnées du PIB sont une consultation distincte datée du 30 octobre 2026 :
elles documentent l’indicateur, sans prétendre dater les CSV locaux.

Les étudiants ont besoin de Python 3, matplotlib et, pour le TD5, pandas.
Les dépendances Jupyter servent à ouvrir les notebooks ou reconstruire les rendus.

## Prévisualiser

```bash
python3 -m http.server 8000 --directory docs
```

Ouvrir <http://localhost:8000/corriges.html>. Tester une solution repliable avec
Tab puis Entrée ou Espace, ainsi que l’affichage sur petit écran. Les fichiers
de code longs défilent horizontalement ; les graphiques s’adaptent à la largeur.
La compilation LaTeX n’est pas nécessaire : les énoncés et PDF ne changent pas.

## Publier

Relire le contenu exact du commit avant de pousser. Ne pas ajouter les fichiers
internes avec un `git add .` global.

```bash
git status --short
git add docs tools MISE_EN_LIGNE.md
git diff --cached --stat
git commit -m "Publier les corrigés pédagogiques des cinq TD Python"
git push origin main
```

Le push déclenche la publication GitHub Pages existante. Vérifier ensuite
<https://etiennedagorn.github.io/intro-python-l2/corriges.html> et les cinq pages,
ainsi que les téléchargements. Un push réussi ne prouve pas à lui seul que les
nouvelles pages sont déjà accessibles.
