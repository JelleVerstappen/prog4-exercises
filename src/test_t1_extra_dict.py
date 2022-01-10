import pytest

from .t1_extra_dict import *


def test_maak_persoonsinformatie_dict_jan():
    result = maak_persoonsinformatie_dict("Jan", 32, 79, 167, "blauw")
    expected = {
        "naam": "Jan",
        "leeftijd": 32,
        "gewicht": 79,
        "lengte": 167,
        "oogkleur": "blauw",
    }
    assert result == expected


def test_maak_persoonsinformatie_dict_piet():
    result = maak_persoonsinformatie_dict("Piet", 23, 66, 192, "bruin")
    expected = {
        "naam": "Piet",
        "leeftijd": 23,
        "gewicht": 66,
        "lengte": 192,
        "oogkleur": "bruin",
    }
    assert result == expected


def test_tel_autos_1():
    woorden = []
    result = tel_autos(woorden)
    expected = {
        "peugeot": 0,
        "ford": 0,
        "bmw": 0,
        "audi": 0,
        "nissan": 0,
    }
    assert result == expected


def test_tel_autos_2():
    woorden = ["bmw", "bmw"]
    result = tel_autos(woorden)
    expected = {
        "peugeot": 0,
        "ford": 0,
        "bmw": 2,
        "audi": 0,
        "nissan": 0,
    }
    assert result == expected


def test_tel_autos_3():
    woorden = ["bmw", "audi"]
    result = tel_autos(woorden)
    expected = {
        "peugeot": 0,
        "ford": 0,
        "bmw": 1,
        "audi": 1,
        "nissan": 0,
    }
    assert result == expected


def test_tel_autos_4():
    woorden = ["bmw", "audi", "audi", "ford", "bmw"]
    result = tel_autos(woorden)
    expected = {
        "peugeot": 0,
        "ford": 1,
        "bmw": 2,
        "audi": 2,
        "nissan": 0,
    }
    assert result == expected


def test_leeftijden_acteurs_1():
    acteurs = [["Will Smith", 53], ["Tom Hanks", 65]]
    result = leeftijden_acteurs(acteurs)
    expected = [53, 65]
    assert result == expected


def test_leeftijden_acteurs_2():
    acteurs = [["Tom Cruise", 59], ["Tom Hanks", 65], ["Samuel L. Jackson", 73]]
    result = leeftijden_acteurs(acteurs)
    expected = [59, 65, 73]
    assert result == expected


def test_lengtes_acteurs_1():
    acteurs = [
        {"naam": "Will Smith", "leeftijd": 53, "lengte": 188},
        {"naam": "Samuel L. Jackson", "leeftijd": 73, "lengte": 189},
        {"naam": "Tom Cruise", "leeftijd": 59, "lengte": 170},
    ]
    result = lengtes_acteurs(acteurs)
    expected = [188, 189, 170]
    assert result == expected


def test_lengtes_acteurs_2():
    acteurs = [
        {"naam": "Jennifer Lawrence", "leeftijd": 31, "lengte": 175},
        {"naam": "Scarlett Johansson", "leeftijd": 37, "lengte": 160},
        {"naam": "Tom Cruise", "leeftijd": 59, "lengte": 170},
    ]
    result = lengtes_acteurs(acteurs)
    expected = [175, 160, 170]
    assert result == expected
