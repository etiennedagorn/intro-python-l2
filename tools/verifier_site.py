"""Contrôle facultatif du site dans Chrome installé, via playwright.

Installer playwright dans l'environnement de contrôle (aucun navigateur à
télécharger), puis : python tools/verifier_site.py
Les captures sont écrites dans un dossier temporaire, hors du site.
"""

import functools
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import tempfile
from threading import Thread

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")


class Handler(SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass


def main():
    captures = Path(tempfile.mkdtemp(prefix="corriges-captures-"))
    serveur = ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Handler, directory=str(ROOT / "docs")))
    Thread(target=serveur.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{serveur.server_port}/"
    erreurs = []
    try:
        with sync_playwright() as p:
            navigateur = p.chromium.launch(executable_path=str(CHROME), headless=True)
            for largeur in [1280, 390]:
                page = navigateur.new_page(viewport={"width": largeur, "height": 900})
                page.on("pageerror", lambda erreur: erreurs.append(str(erreur)))
                page.goto(base + "index.html")
                assert page.locator(".nav-links a").count() == 2
                assert page.locator(".td-row").count() == 5
                assert page.locator(".td-row .resource-link").count() == 10
                installation = page.locator("#installation")
                assert installation.get_attribute("open") is None
                page.screenshot(path=str(captures / f"accueil-{largeur}.png"))
                installation.locator("summary").focus()
                installation.locator("summary").press("Enter")
                assert installation.get_attribute("open") is not None
                installation.locator("summary").press("Space")
                assert installation.get_attribute("open") is None
                assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth + 1")
                for td in range(1, 6):
                    page.goto(base + f"td{td}.html")
                    assert page.locator(".nav-links a").count() == 2
                    assert page.locator(".link-row .resource-link").count() == 2
                    reponse = page.goto(base + f"td{td}-corrige.html")
                    assert reponse.status == 200
                    assert page.locator(".nav-links a").count() == 2
                    assert page.locator("a[download]:visible").count() == 1
                    assert page.locator("#facultatif").get_attribute("open") is None
                    if td == 1:
                        page.screenshot(path=str(captures / f"corrige-intro-{largeur}.png"))
                    summary = page.locator(".exercice summary").first
                    summary.focus()
                    summary.press("Enter")
                    assert page.locator(".exercice details").first.get_attribute("open") is not None
                    summary.press("Space")
                    assert page.locator(".exercice details").first.get_attribute("open") is None
                    page.locator("details").evaluate_all("nodes => nodes.forEach(node => node.open = true)")
                    page.wait_for_timeout(150)
                    assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth + 1"), (td, largeur)
                    assert page.locator('a[download]').count() >= 3
                    if td in [1, 4, 5]:
                        numero = {1: 8, 4: 10, 5: 11}[td]
                        ex = page.locator(f"#exercice-{numero}")
                        ex.scroll_into_view_if_needed()
                        image = ex.locator("img").first
                        image.scroll_into_view_if_needed()
                        image.evaluate("img => img.decode()")
                        assert image.evaluate("img => img.naturalWidth > 0")
                        page.screenshot(path=str(captures / f"td{td}-{largeur}.png"))
                    print(f"TD{td}, {largeur}px : rendu, clavier, largeur et téléchargements OK.", flush=True)
                page.goto(base + "corriges.html")
                assert page.locator(".nav-links a").count() == 2
                assert page.locator('a[href$="-corrige.html"]').count() == 5
                page.close()
            navigateur.close()
        assert not erreurs, erreurs
    finally:
        serveur.shutdown()
        serveur.server_close()
    print("Captures :", captures)


if __name__ == "__main__":
    main()
