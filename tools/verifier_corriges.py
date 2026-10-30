"""Vérifications numériques communes aux scripts et aux notebooks des TD."""

import os
from pathlib import Path
import runpy
import sys


def assertions(td):
    commun = '''
from pathlib import Path as _QAPath
import math as _qa_math
'''
    specifiques = {
        1: '''
assert pays == ["France", "Germany", "Spain", "Italy", "Poland", "Sweden", "Japan"]
assert len(esperance_vie) == 7
assert _qa_math.isclose(moyenne, 573.1 / 7)
assert (minimum, maximum) == (76.5, 84.5)
assert _qa_math.isclose(taux_evolution, 3.4 / 79.1 * 100)
assert _qa_math.isclose(sum(valeurs_test) / len(valeurs_test), 490.6 / 7)
import csv as _qa_csv
with open("data/population.csv") as _qa_f:
    _qa_rows = list(_qa_csv.DictReader(_qa_f))
_qa_pop = {r["Entity"]: int(r["Population"]) for r in _qa_rows if r["Year"] == "2021"}
assert all(_qa_math.isclose(populations_millions[i] * 1_000_000, _qa_pop[pays[i]]) for i in range(7))
_qa_figures = ["esperance_vie_td1.png", "esperance_vie_td1_version2.png"]
''',
        2: '''
assert len(donnees) == 9 and donnees[-1]["pays"] == "Brazil"
assert compteur == 4
assert _qa_math.isclose(proportion, 400 / 9)
assert [classe_co2(x) for x in [4.9, 5.0, 9.9, 10.0]] == ["faible", "intermediaire", "intermediaire", "eleve"]
assert (nombre_faibles, nombre_intermediaires, nombre_eleves) == (4, 4, 1)
assert pays_eleves == ["United States"]
assert au_dessus_seuil(5, 5) is False
assert len(donnees_test) == 9
_qa_figures = ["co2_td2.png"]
''',
        3: '''
assert moyenne([10, 12, 14]) == 12
assert mediane_paire([8, 10, 12, 14]) == 11
assert moyenne_europe == 42.5 and _qa_math.isclose(moyenne_monde, 161 / 6)
assert (mediane_europe, mediane_monde) == (42, 14.5)
assert _qa_math.isclose(part_europe, 500 / 6) and _qa_math.isclose(part_monde, 200 / 6)
assert mediane(groupe_europe_et_usa) == 46 and mediane(groupe_monde_et_italie) == 19
assert premier_quartile(groupe_europe) == 34 and premier_quartile(groupe_monde) == 7
import statistics as _qa_stats
assert _qa_math.isclose(ecart_type_descriptif(groupe_europe), _qa_stats.pstdev(groupe_europe))
assert _qa_math.isclose(ecart_type_descriptif(groupe_monde), _qa_stats.pstdev(groupe_monde))
# Le fragment A de l'énoncé est réellement accepté par matplotlib (diffusion).
_qa_bars = plt.bar(["Europe", "Monde"], [42.5])
assert [b.get_height() for b in _qa_bars] == [42.5, 42.5]
plt.close()
_qa_figures = ["comparaison_pib_td3.png", "comparaison_medianes_td3.png"]
''',
        4: '''
assert len(fertilite) == 10 and _qa_math.isclose(moyenne_initiale, 2.6)
assert min(valeurs) == 1 and max(valeurs) == 6.1
assert len(moyennes_simulees) == 4
assert all(min(valeurs) <= v <= max(valeurs) for v in moyennes_simulees)
assert serie_a == serie_b
assert len(moyennes_20) == 10 and len(tirages_1000) == 1000
assert all(v in valeurs for v in tirages_1000)
assert _qa_math.isclose(moyenne_sans_niger, 19.9 / 9)
assert _qa_math.isclose(mediane_initiale, 1.9)
assert _qa_math.isclose(ecart_type, (sum((v - 2.6)**2 for v in valeurs) / 10)**0.5)
assert borne_basse < moyenne_intervalle < borne_haute
_qa_figures = ["fertilite_barres.png", "fertilite_barres_version2.png", "simulation_moyenne.png", "histogramme_tirages.png", "simulation_mediane.png"]
''',
        5: '''
assert df.shape == (7445, 5)
assert value_col == "GDP per capita"
assert pd.api.types.is_numeric_dtype(df["gdp_pc"])
assert latest_year == 2025 and latest.shape == (198, 5)
assert len(selection) == 8 and len(selection_test) == 7
assert _qa_math.isclose(moyenne, 43281.575875)
assert _qa_math.isclose(mediane, 48121.3475)
assert _qa_math.isclose(minimum, 10039.071) and _qa_math.isclose(maximum, 76931.310)
assert part_au_dessus == 62.5
assert len(top10) == 10 and top10.iloc[0]["country"] == "Singapore"
assert top10.iloc[-1]["country"] == "United States"
assert top10["code"].str.len().eq(3).all()
_qa_export = pd.read_csv("out/gdp_selection.csv")
assert _qa_export.columns.tolist() == ["country", "code", "year", "gdp_pc"]
assert len(_qa_export) == 8
assert len(pd.read_csv("out/gdp_top10.csv")) == 10
assert selection["above_selection_mean"].sum() == 5
assert len(selection_2020) == 8
assert annee_commune == 2023 and len(fusion) > 150
assert fusion["year"].eq(2023).all()
assert not fusion.duplicated(["code", "year"]).any()
assert not fusion[["gdp_pc", "life_expectancy"]].isna().any().any()
assert len(selection_avec_monde) == 9
_qa_figures = ["out/gdp_top10.png", "out/gdp_pays_selection.png", "out/gdp_france_depuis_1990.png"]
''',
    }
    return commun + specifiques[td] + '''
for _qa_name in _qa_figures:
    _qa_path = _QAPath(_qa_name)
    assert _qa_path.stat().st_size > 5000, _qa_name
    assert _qa_path.read_bytes().startswith(b"\\x89PNG\\r\\n\\x1a\\n"), _qa_name
'''


if __name__ == "__main__":
    os.environ.setdefault("MPLBACKEND", "Agg")
    td = int(sys.argv[1])
    variables = runpy.run_path(sys.argv[2])
    exec(assertions(td), variables)
    print(f"TD{td} : calculs, données, exports et graphiques vérifiés.")
