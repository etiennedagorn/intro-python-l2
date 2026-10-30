"""Contenu pédagogique partagé par les rendus HTML, Python et notebook."""

from textwrap import dedent


def exercice(numero, objectif, demarche, code, resultat, vigilance=""):
    return dict(numero=numero, objectif=objectif, demarche=demarche,
                code=dedent(code).strip() + "\n", resultat=resultat,
                vigilance=vigilance)
