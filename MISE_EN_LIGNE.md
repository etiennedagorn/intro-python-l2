# Mettre en ligne le site du cours Python

Ce projet utilise un site statique simple : les pages HTML, la feuille CSS, les aperçus et les PDF publics sont dans le dossier `docs/`.

Aucun framework n'est nécessaire. La méthode la plus simple est donc GitHub Pages avec la source `main` / `docs`.

## 1. Vérifier le dossier

Ouvrir un terminal, puis se placer dans le dossier qui contient `docs/` :

```bash
cd "/Users/etienne.dagorn/Nextcloud/cours/2026_2027/S1_intro_python/01_cours"
pwd
ls docs
```

La commande `ls docs` doit afficher notamment `index.html`, `assets`, `supports` et les pages `td1.html` à `td5.html`.

## 2. Tester le site localement

Depuis le même dossier :

```bash
python3 -m http.server 8000 --directory docs
```

Ouvrir ensuite :

```text
http://localhost:8000
```

Pour arrêter le serveur local, revenir dans le terminal et appuyer sur `Ctrl+C`.

## 3. Vérifier les fichiers publics

Avant de publier, vérifier que le dossier `docs/` ne contient que les supports étudiants :

```bash
find docs -maxdepth 4 -type f | sort
```

Vérifier aussi qu'aucun fichier interne n'est présent dans le site :

```bash
find docs -iname "*corr*" -o -iname "*correction*"
```

Cette commande ne doit rien afficher.

## 4. Initialiser Git si le dossier n'est pas encore un dépôt

Dans ce dossier, aucune configuration Git locale n'a été détectée au moment de la préparation du site. Pour créer un dépôt :

```bash
git init
git branch -M main
```

Créer ensuite un dépôt vide sur GitHub, puis copier l'URL fournie par GitHub. Elle ressemble à :

```text
git@github.com:UTILISATEUR/NOM_DU_DEPOT.git
```

Associer le dépôt local au dépôt GitHub :

```bash
git remote add origin git@github.com:UTILISATEUR/NOM_DU_DEPOT.git
```

Remplacer `UTILISATEUR` et `NOM_DU_DEPOT` par les valeurs réelles.

## 5. Ajouter uniquement le site public

Pour une publication publique, ne pas utiliser `git add .` au premier envoi. Ajouter seulement le site et la documentation utile :

```bash
git add docs .gitignore MISE_EN_LIGNE.md
git commit -m "Create public Python course site"
git push -u origin main
```

Cette méthode évite d'envoyer des fichiers internes qui peuvent exister dans les dossiers de travail.

## 6. Activer GitHub Pages

Sur GitHub :

1. Ouvrir le dépôt.
2. Aller dans `Settings`.
3. Ouvrir `Pages`.
4. Dans `Build and deployment`, choisir `Deploy from a branch`.
5. Sélectionner la branche `main`.
6. Sélectionner le dossier `/docs`.
7. Enregistrer.

GitHub affiche ensuite l'URL du site. Elle prend généralement la forme :

```text
https://UTILISATEUR.github.io/NOM_DU_DEPOT/
```

La mise en ligne peut prendre quelques minutes.

## 7. Publier une modification ultérieure

Après avoir modifié un TD ou un PDF, recompiler les fichiers concernés, recopier les PDF publics dans `docs/supports`, puis tester localement.

Ensuite :

```bash
git status
git add docs MISE_EN_LIGNE.md
git commit -m "Update Python course site"
git push
```

GitHub Pages mettra le site à jour automatiquement après le `push`.

## 8. Si le dépôt doit contenir tout le cours

Si le dépôt Git contient aussi les sources LaTeX, scripts internes ou rendus étudiants, garder le dépôt privé ou vérifier très soigneusement `.gitignore` avant le premier commit :

```bash
git status --ignored
```

Pour un site étudiant public, la solution la plus robuste reste de publier uniquement `docs/`.
