from math import exp

import pytest

from .t2_herhaling_datastruct import *


def test_maak_videokaart_dict_rtx3080():
    result = maak_videokaart_dict("NVIDIA", "RTX 3080", "Ampere", 10, 320, 628, 2020)
    expected = {
        "merk": "NVIDIA",
        "naam": "RTX 3080",
        "architectuur": "Ampere",
        "geheugen": 10,
        "busbreedte": 320,
        "diesize": 628,
        "jaar": 2020,
    }
    assert result == expected


def test_maak_videokaart_dict_rx6800():
    result = maak_videokaart_dict("AMD", "RX 6800", "RDNA 2", 16, 256, 520, 2020)
    expected = {
        "merk": "AMD",
        "naam": "RX 6800",
        "architectuur": "RDNA 2",
        "geheugen": 16,
        "busbreedte": 256,
        "diesize": 520,
        "jaar": 2020,
    }
    assert result == expected


def test_tel_videokaarten_1():
    videokaarten = [
        {
            "merk": "AMD",
            "naam": "RX 6800",
            "architectuur": "RDNA 2",
            "geheugen": 16,
            "busbreedte": 256,
            "diesize": 520,
            "jaar": 2020,
        }
    ]
    result = tel_videokaarten(videokaarten)
    assert result == 1


def test_tel_videokaarten_2():
    videokaarten = [
        {
            "merk": "NVIDIA",
            "naam": "RTX 3080",
            "architectuur": "Ampere",
            "geheugen": 10,
            "busbreedte": 320,
            "diesize": 628,
        },
        {
            "merk": "AMD",
            "naam": "RX 6800",
            "architectuur": "RDNA 2",
            "geheugen": 16,
            "busbreedte": 256,
            "diesize": 520,
        },
    ]
    result = tel_videokaarten(videokaarten)
    assert result == 2


def test_tel_videokaarten_per_merk_1():
    videokaarten = []
    result = tel_videokaarten_per_merk(videokaarten)
    expected = {
        "NVIDIA": 0,
        "AMD": 0,
    }
    assert result == expected


def test_tel_videokaarten_per_merk_2():
    videokaarten = [
        {
            "merk": "NVIDIA",
            "naam": "RTX 3080",
            "architectuur": "Ampere",
            "geheugen": 10,
            "busbreedte": 320,
            "diesize": 628,
        },
        {
            "merk": "AMD",
            "naam": "RX 6800",
            "architectuur": "RDNA 2",
            "geheugen": 16,
            "busbreedte": 256,
            "diesize": 520,
        },
    ]
    result = tel_videokaarten_per_merk(videokaarten)
    expected = {
        "NVIDIA": 1,
        "AMD": 1,
    }
    assert result == expected


def test_tel_videokaarten_per_merk_2():
    videokaarten = [
        {
            "merk": "NVIDIA",
            "naam": "RTX 3070 Ti",
            "architectuur": "Ampere",
            "geheugen": 10,
            "busbreedte": 256,
            "diesize": 392.5,
        },
        {
            "merk": "NVIDIA",
            "naam": "RTX 3080",
            "architectuur": "Ampere",
            "geheugen": 10,
            "busbreedte": 320,
            "diesize": 628,
        },
        {
            "merk": "NVIDIA",
            "naam": "RTX 3090 Ti",
            "architectuur": "Ampere",
            "geheugen": 24,
            "busbreedte": 384,
            "diesize": 628,
        },
        {
            "merk": "AMD",
            "naam": "RX 6800",
            "architectuur": "RDNA 2",
            "geheugen": 16,
            "busbreedte": 256,
            "diesize": 520,
        },
    ]
    result = tel_videokaarten_per_merk(videokaarten)
    expected = {
        "NVIDIA": 3,
        "AMD": 1,
    }
    assert result == expected


def test_grootste_videokaart_1():
    videokaarten = [
        {
            "merk": "NVIDIA",
            "naam": "RTX 3070 Ti",
            "architectuur": "Ampere",
            "geheugen": 10,
            "busbreedte": 256,
            "diesize": 392.5,
        },
        {
            "merk": "AMD",
            "naam": "RX 6800",
            "architectuur": "RDNA 2",
            "geheugen": 16,
            "busbreedte": 256,
            "diesize": 520,
        },
    ]
    expected = "RX 6800"
    result = grootste_videokaart(videokaarten)
    assert result == expected


def test_grootste_videokaart_2():
    videokaarten = [
        {
            "merk": "NVIDIA",
            "naam": "RTX 2080 Ti",
            "architectuur": "Turing",
            "geheugen": 11,
            "busbreedte": 384,
            "diesize": 754,
        },
        {
            "merk": "NVIDIA",
            "naam": "RTX 3070 Ti",
            "architectuur": "Ampere",
            "geheugen": 10,
            "busbreedte": 256,
            "diesize": 392.5,
        },
        {
            "merk": "AMD",
            "naam": "RX 6800",
            "architectuur": "RDNA 2",
            "geheugen": 16,
            "busbreedte": 256,
            "diesize": 520,
        },
    ]
    expected = "RTX 2080 Ti"
    result = grootste_videokaart(videokaarten)
    assert result == expected


def test_grootste_videokaartgrootte_per_merk_1():
    videokaarten = [
        {
            "merk": "NVIDIA",
            "naam": "RTX 3070 Ti",
            "architectuur": "Ampere",
            "geheugen": 10,
            "busbreedte": 256,
            "diesize": 392.5,
        },
        {
            "merk": "AMD",
            "naam": "RX 6800",
            "architectuur": "RDNA 2",
            "geheugen": 16,
            "busbreedte": 256,
            "diesize": 520,
        },
    ]
    expected = {
        "NVIDIA": 392.5,
        "AMD": 520,
    }
    result = grootste_videokaartgrootte_per_merk(videokaarten)
    assert result == expected


def test_grootste_videokaartgrootte_per_merk_2():
    videokaarten = [
        {
            "merk": "NVIDIA",
            "naam": "RTX 2080 Ti",
            "architectuur": "Turing",
            "geheugen": 11,
            "busbreedte": 384,
            "diesize": 754,
        },
        {
            "merk": "NVIDIA",
            "naam": "RTX 3070 Ti",
            "architectuur": "Ampere",
            "geheugen": 10,
            "busbreedte": 256,
            "diesize": 392.5,
        },
        {
            "merk": "NVIDIA",
            "naam": "RTX 3080",
            "architectuur": "Ampere",
            "geheugen": 10,
            "busbreedte": 320,
            "diesize": 628,
        },
        {
            "merk": "NVIDIA",
            "naam": "RTX 3090 Ti",
            "architectuur": "Ampere",
            "geheugen": 24,
            "busbreedte": 384,
            "diesize": 628,
        },
        {
            "merk": "AMD",
            "naam": "RX 6800",
            "architectuur": "RDNA 2",
            "geheugen": 16,
            "busbreedte": 256,
            "diesize": 520,
        },
    ]
    expected = {
        "NVIDIA": 754,
        "AMD": 520,
    }
    result = grootste_videokaartgrootte_per_merk(videokaarten)
    assert result == expected


def test_diesizes_videokaarten_1():
    videokaarten = [
        {
            "merk": "AMD",
            "naam": "RX 6800",
            "architectuur": "RDNA 2",
            "geheugen": 16,
            "busbreedte": 256,
            "diesize": 520,
        },
    ]
    expected = [520]
    result = diesizes_videokaarten(videokaarten)
    assert result == expected


def test_diesizes_videokaarten_2():
    videokaarten = [
        {
            "merk": "NVIDIA",
            "naam": "RTX 2080 Ti",
            "architectuur": "Turing",
            "geheugen": 11,
            "busbreedte": 384,
            "diesize": 754,
        },
        {
            "merk": "NVIDIA",
            "naam": "RTX 3070 Ti",
            "architectuur": "Ampere",
            "geheugen": 10,
            "busbreedte": 256,
            "diesize": 392.5,
        },
        {
            "merk": "NVIDIA",
            "naam": "RTX 3080",
            "architectuur": "Ampere",
            "geheugen": 10,
            "busbreedte": 320,
            "diesize": 628,
        },
        {
            "merk": "NVIDIA",
            "naam": "RTX 3090 Ti",
            "architectuur": "Ampere",
            "geheugen": 24,
            "busbreedte": 384,
            "diesize": 628,
        },
        {
            "merk": "AMD",
            "naam": "RX 6800",
            "architectuur": "RDNA 2",
            "geheugen": 16,
            "busbreedte": 256,
            "diesize": 520,
        },
    ]
    expected = [754, 392.5, 628, 628, 520]
    result = diesizes_videokaarten(videokaarten)
    assert result == expected


def test_gemiddelde_diesize_videokaarten_1():
    videokaarten = [
        {
            "merk": "AMD",
            "naam": "RX 6800",
            "architectuur": "RDNA 2",
            "geheugen": 16,
            "busbreedte": 256,
            "diesize": 520,
        },
    ]
    result = gemiddelde_diesize_videokaarten(videokaarten)
    expected = 520
    assert result == expected


def test_gemiddelde_diesize_videokaarten_2():
    videokaarten = [
        {
            "merk": "NVIDIA",
            "naam": "RTX 2080 Ti",
            "architectuur": "Turing",
            "geheugen": 11,
            "busbreedte": 384,
            "diesize": 754,
        },
        {
            "merk": "NVIDIA",
            "naam": "RTX 3070 Ti",
            "architectuur": "Ampere",
            "geheugen": 10,
            "busbreedte": 256,
            "diesize": 392.5,
        },
        {
            "merk": "NVIDIA",
            "naam": "RTX 3080",
            "architectuur": "Ampere",
            "geheugen": 10,
            "busbreedte": 320,
            "diesize": 628,
        },
        {
            "merk": "NVIDIA",
            "naam": "RTX 3090 Ti",
            "architectuur": "Ampere",
            "geheugen": 24,
            "busbreedte": 384,
            "diesize": 628,
        },
        {
            "merk": "AMD",
            "naam": "RX 6800",
            "architectuur": "RDNA 2",
            "geheugen": 16,
            "busbreedte": 256,
            "diesize": 520,
        },
    ]
    result = gemiddelde_diesize_videokaarten(videokaarten)
    expected = 584.5
    assert abs(result - expected) < 1


def test_jaren_videokaarten_0():
    videokaarten = [
        {
            "merk": "AMD",
            "naam": "RX 6800",
            "architectuur": "RDNA 2",
            "geheugen": 16,
            "busbreedte": 256,
            "diesize": 520,
            "jaar": 2020,
        },
    ]
    result = jaren_videokaarten(videokaarten)
    expected = [2020]
    assert result == expected


def test_videokaarten_voor_jaar_2():
    videokaarten = [
        {
            "merk": "AMD",
            "naam": "RX 6800",
            "architectuur": "RDNA 2",
            "geheugen": 16,
            "busbreedte": 256,
            "diesize": 520,
            "jaar": 2020,
        },
        {
            "merk": "NVIDIA",
            "naam": "RTX 3080",
            "architectuur": "Ampere",
            "geheugen": 10,
            "busbreedte": 320,
            "diesize": 628,
            "jaar": 2020,
        },
    ]
    result = jaren_videokaarten(videokaarten)
    expected = [2020, 2020]
    assert result == expected


def test_jaren_videokaarten_3():
    videokaarten = [
        {
            "merk": "NVIDIA",
            "naam": "RTX 2080 Ti",
            "architectuur": "Turing",
            "geheugen": 11,
            "busbreedte": 384,
            "diesize": 754,
            "jaar": 2018,
        },
        {
            "merk": "AMD",
            "naam": "RX 6800",
            "architectuur": "RDNA 2",
            "geheugen": 16,
            "busbreedte": 256,
            "diesize": 520,
            "jaar": 2020,
        },
        {
            "merk": "NVIDIA",
            "naam": "RTX 3080",
            "architectuur": "Ampere",
            "geheugen": 10,
            "busbreedte": 320,
            "diesize": 628,
            "jaar": 2020,
        },
    ]
    result = jaren_videokaarten(videokaarten)
    expected = [2018, 2020, 2020]
    assert result == expected


def test_videokaarten_voor_jaar_0():
    videokaarten = [
        {
            "merk": "AMD",
            "naam": "RX 6800",
            "architectuur": "RDNA 2",
            "geheugen": 16,
            "busbreedte": 256,
            "diesize": 520,
            "jaar": 2020,
        },
    ]
    result = videokaarten_voor_jaar(videokaarten, 2019)
    expected = []
    assert result == expected


def test_videokaarten_voor_jaar_1():
    videokaarten = [
        {
            "merk": "AMD",
            "naam": "RX 6800",
            "architectuur": "RDNA 2",
            "geheugen": 16,
            "busbreedte": 256,
            "diesize": 520,
            "jaar": 2020,
        },
    ]
    result = videokaarten_voor_jaar(videokaarten, 2020)
    expected = videokaarten
    assert result == expected


def test_videokaarten_voor_jaar_2():
    videokaarten = [
        {
            "merk": "AMD",
            "naam": "RX 6800",
            "architectuur": "RDNA 2",
            "geheugen": 16,
            "busbreedte": 256,
            "diesize": 520,
            "jaar": 2020,
        },
        {
            "merk": "NVIDIA",
            "naam": "RTX 3080",
            "architectuur": "Ampere",
            "geheugen": 10,
            "busbreedte": 320,
            "diesize": 628,
            "jaar": 2020,
        },
    ]
    result = videokaarten_voor_jaar(videokaarten, 2020)
    expected = videokaarten
    assert result == expected


def test_videokaarten_voor_jaar_3():
    videokaarten = [
        {
            "merk": "NVIDIA",
            "naam": "RTX 2080 Ti",
            "architectuur": "Turing",
            "geheugen": 11,
            "busbreedte": 384,
            "diesize": 754,
            "jaar": 2018,
        },
        {
            "merk": "AMD",
            "naam": "RX 6800",
            "architectuur": "RDNA 2",
            "geheugen": 16,
            "busbreedte": 256,
            "diesize": 520,
            "jaar": 2020,
        },
        {
            "merk": "NVIDIA",
            "naam": "RTX 3080",
            "architectuur": "Ampere",
            "geheugen": 10,
            "busbreedte": 320,
            "diesize": 628,
            "jaar": 2020,
        },
    ]
    result = videokaarten_voor_jaar(videokaarten, 2018)
    expected = [
        {
            "merk": "NVIDIA",
            "naam": "RTX 2080 Ti",
            "architectuur": "Turing",
            "geheugen": 11,
            "busbreedte": 384,
            "diesize": 754,
            "jaar": 2018,
        },
    ]
    assert result == expected


def test_grootste_geheugen_per_jaar_1():
    videokaarten = [
        {
            "merk": "AMD",
            "naam": "RX 6800",
            "architectuur": "RDNA 2",
            "geheugen": 16,
            "busbreedte": 256,
            "diesize": 520,
            "jaar": 2020,
        },
    ]
    result = grootste_geheugen_per_jaar(videokaarten)
    expected = {
        2020: 16,
    }
    assert result == expected


def test_grootste_geheugen_per_jaar_2():
    videokaarten = [
        {
            "merk": "AMD",
            "naam": "RX 6800",
            "architectuur": "RDNA 2",
            "geheugen": 16,
            "busbreedte": 256,
            "diesize": 520,
            "jaar": 2020,
        },
        {
            "merk": "NVIDIA",
            "naam": "RTX 3080",
            "architectuur": "Ampere",
            "geheugen": 10,
            "busbreedte": 320,
            "diesize": 628,
            "jaar": 2020,
        },
        {
            "merk": "NVIDIA",
            "naam": "RTX 2080 Ti",
            "architectuur": "Turing",
            "geheugen": 11,
            "busbreedte": 384,
            "diesize": 754,
            "jaar": 2018,
        },
    ]
    result = grootste_geheugen_per_jaar(videokaarten)
    expected = {
        2018: 11,
        2020: 16,
    }
    assert result == expected
