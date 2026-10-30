#!/usr/bin/env python3
"""Exécuter puis rendre les cinq corrigés sans changer les énoncés.

Depuis 01_cours : python3 tools/construire_corriges.py
Outils de construction : nbformat, nbclient, ipykernel.
Les étudiants ont uniquement besoin de matplotlib et de pandas (TD5).
"""

import base64
from html import escape
from html.parser import HTMLParser
import importlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
from urllib.parse import unquote, urlsplit
import zipfile

import nbformat
from nbclient import NotebookClient

from verifier_corriges import assertions

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PUBLIC = DOCS / "supports" / "corr"
FIGURES = PUBLIC / "figures"
TITRES = ["Premiers scripts et statistiques descriptives simples",
          "Boucles, conditions et proportions avec données OWID",
          "Fonctions et comparaison de groupes",
          "Graphiques et simulation simple à partir d’OWID",
          "Mini-projet pandas avec Our World in Data"]
DONNEES = {1: ["population.csv"], 5: ["gdp-per-capita-worldbank.csv", "life-expectancy.csv"]}


def commentaire(texte):
    return "\n".join("# " + s for s in textwrap.wrap(texte, width=88))


def titres_exercices(tex):
    titres = []
    for match in re.finditer(r"\\begin\{mandatoryexercise\}\{", tex):
        debut = match.end()
        fin = debut
        profondeur = 1
        while profondeur:
            if tex[fin] == "{":
                profondeur += 1
            elif tex[fin] == "}":
                profondeur -= 1
            fin += 1
        titre = tex[debut:fin - 1]
        titre = re.sub(r"\\code\{([^}]+)\}", r"\1", titre).replace(r"\_", "_")
        titres.append(titre)
    return titres


def entete(titre, actuel=""):
    return f'''<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(titre)} - Python pour économistes</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip-link" href="#contenu">Aller au contenu</a>
<header class="site-header"><nav class="nav" aria-label="Navigation principale">
  <a class="brand" href="index.html">Python pour économistes</a>
  <div class="nav-links">
    <a href="index.html">Accueil</a><a href="index.html#seances">TD</a>
    <a href="corriges.html"{actuel}>Corrigés</a><a href="index.html#cours">Cours</a>
  </div>
</nav></header>
<main id="contenu" class="corrige">
'''


def pied():
    return '''</main><footer class="footer"><div class="footer-inner">
Python pour économistes - Université de Lille - L2 ESM
</div></footer></body></html>
'''


def fichiers(td):
    return f'''<div class="link-row">
<a class="resource-link" href="td{td}.html">Énoncé du TD{td}</a>
<a class="resource-link" href="supports/corr/TD{td}_corrige.ipynb" download>Notebook .ipynb</a>
<a class="resource-link" href="supports/corr/TD{td}_corrige.py" download>Script .py</a>
<a class="resource-link" href="supports/corr/TD{td}_complet.zip" download>Dossier complet .zip</a>
</div>'''


def sorties(cellule, prefixe, objectif):
    html = []
    compteur = 0
    for output in cellule.get("outputs", []):
        if output["output_type"] == "error":
            raise RuntimeError(output)
        if output["output_type"] == "stream":
            # La seule sortie personnelle est le diagnostic Path.cwd du TD5.
            texte = output["text"]
            texte = re.sub(r"Dossier courant : .*", "Dossier courant : <dossier TD5 de cette exécution>", texte)
            html.append('<pre tabindex="0"><code>' + escape(texte) + '</code></pre>')
        elif "image/png" in output.get("data", {}):
            compteur += 1
            nom = f"{prefixe}-{compteur}.png"
            (FIGURES / nom).write_bytes(base64.b64decode(output["data"]["image/png"]))
            html.append(f'<figure><img loading="lazy" src="supports/corr/figures/{nom}" alt="{escape(objectif)}">'
                        f'<figcaption>{escape(objectif)} Résultat de l’exécution de référence.</figcaption></figure>')
    return "\n".join(html)


def render_exercice(ex, titre, cellule, td, extension=False):
    ident = ("extension-" if extension else "exercice-") + str(ex["numero"])
    etiquette = "Question facultative" if extension else "Exercice"
    resultat = sorties(cellule, f"td{td}-{ident}", ex["objectif"])
    attention = ('<div class="callout"><strong>Point de vigilance.</strong> ' + escape(ex["vigilance"]) + '</div>') if ex["vigilance"] else ""
    return f'''<section id="{ident}" class="exercice">
<h2>{etiquette} {ex['numero']} — {escape(titre)}</h2>
<p><strong>Objectif.</strong> {escape(ex['objectif'])}</p>
<details><summary>Afficher la solution : {etiquette.lower()} {ex['numero']}</summary>
<h3>Démarche de résolution</h3><p>{escape(ex['demarche'])}</p>
<h3>Code Python commenté</h3><pre tabindex="0"><code class="language-python">{escape(ex['code'])}</code></pre>
<h3>Résultat et interprétation</h3><p>{escape(ex['resultat'])}</p>
{('<p class="execution-label">Sortie de l’exécution de référence :</p>' + resultat) if resultat else ''}
{attention}</details></section>
'''


def construire_td(td):
    contenu = importlib.import_module(f"corriges_td{td}")
    source = ROOT / f"seance_{td + 2}" / f"TP_{td}_revise.tex"
    tex = source.read_text()
    titres = titres_exercices(tex)
    assert len(titres) == len(contenu.EXERCICES)
    assert [e["numero"] for e in contenu.EXERCICES] == list(range(1, len(titres) + 1))
    assert [e["numero"] for e in contenu.EXTENSIONS] == list(range(1, 11))
    pseudos = re.findall(r"\\begin\{pseudocodeexercise\}\{([^}]+)\}(.*?)\\end\{pseudocodeexercise\}", tex, re.S)
    notebook = nbformat.v4.new_notebook(metadata={
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": ".".join(map(str, sys.version_info[:3]))},
    })
    introduction = f"# TD{td} — Corrigé\n\n{TITRES[td - 1]}\n\n{contenu.INTRO}\n\nExécuter toutes les cellules dans l’ordre, depuis une session neuve. Pour les données, extraire le dossier complet et ouvrir le notebook à sa racine. Les sorties sont celles d’une exécution de référence.\n\nBibliothèques : matplotlib ; pandas en plus au TD5."
    notebook.cells.append(nbformat.v4.new_markdown_cell(introduction))
    notebook.cells.append(nbformat.v4.new_code_cell("# Afficher les figures dans le notebook.\n%matplotlib inline"))
    script = ["#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n", commentaire(introduction.replace("# ", ""))]
    pseudo_html = []
    for n, (titre, corps) in enumerate(pseudos, 1):
        code = re.search(r"\\begin\{lstlisting\}(.*?)\\end\{lstlisting\}", corps, re.S)[1].strip()
        texte = f"## Démarche en pseudo-code {n} — {titre}\n\n```text\n{code}\n```\n\nLes exercices qui suivent mettent en œuvre ce plan, étape par étape."
        notebook.cells.append(nbformat.v4.new_markdown_cell(texte))
        script.append(commentaire(f"Démarche en pseudo-code {n} — {titre}") + "\n" + code)
        pseudo_html.append(f'<details id="pseudo-{n}"><summary>Démarche en pseudo-code {n} — {escape(titre)}</summary><pre tabindex="0"><code>{escape(code)}</code></pre><p>Les exercices ci-dessous mettent en œuvre ce plan.</p></details>')
    emplacements = []
    for extension, liste in [(False, contenu.EXERCICES), (True, contenu.EXTENSIONS)]:
        for ex in liste:
            titre = ex["objectif"] if extension else titres[ex["numero"] - 1]
            label = "Question facultative" if extension else "Exercice"
            texte = f"## {label} {ex['numero']} — {titre}\n\n**Objectif.** {ex['objectif']}\n\n**Démarche.** {ex['demarche']}"
            notebook.cells.append(nbformat.v4.new_markdown_cell(texte))
            emplacements.append((ex, titre, len(notebook.cells), extension))
            notebook.cells.append(nbformat.v4.new_code_cell(ex["code"]))
            notebook.cells.append(nbformat.v4.new_markdown_cell("**Résultat et interprétation.** " + ex["resultat"] +
                ("\n\n**Point de vigilance.** " + ex["vigilance"] if ex["vigilance"] else "")))
            script.append(commentaire(f"{label} {ex['numero']} — {titre}") + "\n" +
                          commentaire("Objectif : " + ex["objectif"]) + "\n" +
                          commentaire("Démarche : " + ex["demarche"]) + "\n\n" + ex["code"] + "\n" +
                          commentaire("Résultat et interprétation : " + ex["resultat"]) + "\n" +
                          (commentaire("Vigilance : " + ex["vigilance"]) if ex["vigilance"] else ""))
    chemin_script = PUBLIC / f"TD{td}_corrige.py"
    chemin_script.write_text("\n\n".join(script).strip() + "\n")
    # Chaque version est exécutée dans un dossier neuf, avec uniquement ses données.
    with tempfile.TemporaryDirectory(prefix=f"td{td}-script-") as dossier:
        travail = Path(dossier)
        (travail / "data").mkdir()
        for nom in DONNEES.get(td, []):
            shutil.copyfile(PUBLIC / "data" / nom, travail / "data" / nom)
        resultat = subprocess.run([sys.executable, str(ROOT / "tools/verifier_corriges.py"), str(td), str(chemin_script)],
                                  cwd=travail, capture_output=True, text=True, timeout=180,
                                  env={**os.environ, "MPLBACKEND": "Agg"})
        if resultat.returncode:
            raise RuntimeError(f"TD{td}, script :\n{resultat.stdout}\n{resultat.stderr}")
    with tempfile.TemporaryDirectory(prefix=f"td{td}-notebook-") as dossier:
        travail = Path(dossier)
        (travail / "data").mkdir()
        for nom in DONNEES.get(td, []):
            shutil.copyfile(PUBLIC / "data" / nom, travail / "data" / nom)
        # Cellule de contrôle exécutée dans le vrai noyau, puis retirée du rendu étudiant.
        notebook.cells.append(nbformat.v4.new_code_cell(assertions(td)))
        NotebookClient(notebook, timeout=180, kernel_name="python3",
                       resources={"metadata": {"path": dossier}}).execute()
        notebook.cells.pop()
        for cell in notebook.cells:
            for output in cell.get("outputs", []):
                if output["output_type"] == "stream":
                    output["text"] = output["text"].replace(dossier, "<dossier TD5 de cette exécution>")
    nbformat.validate(notebook)
    nbformat.write(notebook, PUBLIC / f"TD{td}_corrige.ipynb")
    if td == 1:
        # Préserver le lien public historique vers le script du TD1.
        shutil.copyfile(chemin_script, PUBLIC / "TP_1_corr_revise.py")
    html = [entete(f"Corrigé TD{td}"), f'<p class="eyebrow">Corrigé TD{td}</p><h1>{escape(TITRES[td - 1])}</h1>',
            f'<p class="lead">{escape(contenu.INTRO)}</p>', fichiers(td),
            '<p>Les exercices se suivent. Utiliser <kbd>Tab</kbd> puis <kbd>Entrée</kbd> ou <kbd>Espace</kbd> pour ouvrir une solution au clavier. Les zones de code peuvent défiler horizontalement.</p>',
            '<p>Les sorties ci-dessous proviennent du code exécuté. Les simulations du TD4 peuvent changer à chaque exécution.</p>',
            '<nav aria-label="Sommaire du corrigé"><h2>Sommaire</h2><ol>']
    html.extend(f'<li><a href="#exercice-{i}">{escape(t)}</a></li>' for i, t in enumerate(titres, 1))
    html.append('</ol><a href="#facultatif">Les dix questions facultatives</a></nav>')
    html.extend(pseudo_html)
    for ex, titre, indice, extension in emplacements:
        if extension and ex["numero"] == 1:
            html.append('<section id="facultatif"><h2>Entraînement facultatif</h2><p>Ces dix questions sont également corrigées. Elles se lisent après le parcours obligatoire, dans l’ordre.</p></section>')
        html.append(render_exercice(ex, titre, notebook.cells[indice], td, extension))
    html.append('<section><h2>Sources et fichiers de référence</h2><p>Les extraits des TD1 à TD4 sont ceux des énoncés. Les CSV complémentaires sont des copies des fichiers du dépôt, dont la date de téléchargement initial n’est pas documentée. ')
    html.append('<a href="supports/corr/data/provenance.json">Consulter les sources et empreintes SHA-256 des CSV</a>.</p>')
    if td == 1:
        html.append('<p>Extension sur les populations : <a href="supports/corr/data/population.csv" download>population.csv</a> ; source <a href="https://ourworldindata.org/grapher/population">Our World in Data — Population</a>.</p>')
    if td == 5:
        html.append('<p><a href="supports/corr/data/gdp-per-capita-worldbank.csv" download>CSV du PIB</a> · <a href="supports/corr/data/life-expectancy.csv" download>CSV de l’espérance de vie</a> · <a href="https://ourworldindata.org/grapher/gdp-per-capita-worldbank">Indicateur PIB OWID et unités</a> · <a href="supports/corr/data/gdp-metadata-2026-10-30.json">Métadonnées consultées le 30 octobre 2026</a>. Les noms de colonnes en ligne peuvent différer de la copie du dépôt.</p>')
    html.append('</section><nav class="pager" aria-label="Navigation entre corrigés"><a href="corriges.html">Tous les corrigés</a>')
    if td > 1:
        html.append(f'<a href="td{td-1}-corrige.html">Corrigé précédent</a>')
    if td < 5:
        html.append(f'<a href="td{td+1}-corrige.html">Corrigé suivant</a>')
    html.append('</nav>' + pied())
    (DOCS / f"td{td}-corrige.html").write_text(
        "\n".join(ligne.rstrip() for ligne in "\n".join(html).splitlines()) + "\n")
    lire = f"TD{td} — Corrigé\n\nExtraire le ZIP dans un dossier, puis ouvrir ce dossier dans VS Code.\nExécuter : python3 TD{td}_corrige.py (ou py sous Windows).\nBibliothèques : matplotlib" + (" et pandas" if td == 5 else "") + ".\nInstaller dans le même Python : python3 -m pip install matplotlib" + (" pandas" if td == 5 else "") + ".\nPour le notebook, utiliser Jupyter ou l'extension Jupyter de VS Code ; sélectionner\nle même Python puis redémarrer le noyau et exécuter toutes les cellules dans l'ordre.\nLes questions facultatives suivent les exercices obligatoires et utilisent leurs variables.\nLes images sont enregistrées dans le dossier courant" + (", sous out/ au TD5" if td == 5 else "") + ".\nLes données sont des copies des CSV du dépôt. Voir data/provenance.json.\nLa date initiale de téléchargement n'est pas documentée ; les empreintes identifient la copie.\n"
    with zipfile.ZipFile(PUBLIC / f"TD{td}_complet.zip", "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for nom in [f"TD{td}_corrige.py", f"TD{td}_corrige.ipynb"]:
            archive.write(PUBLIC / nom, nom)
        for nom in DONNEES.get(td, []):
            archive.write(PUBLIC / "data" / nom, "data/" + nom)
        if DONNEES.get(td):
            archive.write(PUBLIC / "data/provenance.json", "data/provenance.json")
        archive.writestr("LISEZMOI.txt", lire)
    print(f"TD{td} : {len(titres)} exercices, 10 questions facultatives, {len(pseudos)} plans ; script et notebook OK.", flush=True)


def verifier_liens():
    class Liens(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.liens = []
            self.ids = set()

        def handle_starttag(self, tag, attrs):
            a = dict(attrs)
            if "id" in a:
                assert a["id"] not in self.ids, f"Identifiant dupliqué : {a['id']}"
                self.ids.add(a["id"])
            for cle in ("href", "src"):
                if cle in a:
                    self.liens.append(a[cle])
    pages = {}
    for chemin in DOCS.rglob("*.html"):
        parse = Liens()
        parse.feed(chemin.read_text())
        pages[chemin.resolve()] = parse
    total = 0
    for chemin, parse in pages.items():
        for lien in parse.liens:
            url = urlsplit(lien)
            if url.scheme or url.netloc:
                continue
            cible = (chemin.parent / unquote(url.path)).resolve() if url.path else chemin
            assert cible.is_relative_to(DOCS.resolve()), (chemin, lien)
            assert cible.exists(), (chemin, lien)
            if url.fragment and cible in pages:
                assert unquote(url.fragment) in pages[cible].ids, (chemin, lien)
            total += 1
    print(f"{len(pages)} pages HTML, {total} liens et ressources locaux contrôlés.")


def main():
    FIGURES.mkdir(exist_ok=True)
    for td in range(1, 6):
        construire_td(td)
    html = [entete("Corrigés des TD", ' aria-current="page"'), '<p class="eyebrow">TD1 à TD5</p><h1>Corrigés des TD Python</h1>',
            '<p class="lead">62 exercices obligatoires, les 50 questions facultatives et les 10 démarches en pseudo-code des cinq TD. Chaque solution explique le raisonnement et présente du code exécuté, ses résultats et ses limites.</p>',
            '<p>Commencez par essayer les exercices. Les solutions sont repliées dans chaque page. Les scripts et notebooks suivent les questions dans l’ordre. Le dossier complet contient aussi les données nécessaires ; extraire le ZIP avant de travailler.</p>']
    for td in range(1, 6):
        html.append(f'<section><h2><a href="td{td}-corrige.html">Corrigé TD{td} — {escape(TITRES[td-1])}</a></h2>' + fichiers(td) + '</section>')
    html.append('<section><h2>Exécuter les corrigés</h2><p>Python 3 avec matplotlib suffit pour les TD1 à TD4. Le TD5 utilise aussi pandas. Installer les bibliothèques dans le Python choisi par VS Code, puis ouvrir le dossier extrait et lancer le script depuis ce dossier. Pour les notebooks, sélectionner ce même Python dans Jupyter et exécuter les cellules dans l’ordre depuis un noyau redémarré.</p><p>Les données sont celles du dépôt. Les simulations peuvent varier ; les résultats du TD5 sont fixés par les copies CSV fournies. Les noms de fichiers des énoncés et leurs données restent inchangés.</p></section>')
    (DOCS / "corriges.html").write_text("\n".join(html) + pied())
    verifier_liens()


if __name__ == "__main__":
    main()
