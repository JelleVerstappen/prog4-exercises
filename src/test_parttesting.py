# Schrijf testen voor de functies die je in part_testing.py vindt.
from .part_testing import bmi, maximum, pythagoras

def test_maximum():
    result = maximum(0, -1)

    assert result == 0

def test_maximum_2():
    result = maximum(5, 10)

    assert result == 10

def test_maximum():
    m = maximum(1, 2)
    assert m == 2


def test_pythagoras():
    schuine_zijde = pythagoras(3, 4)
    assert schuine_zijde == 5


def test_bmi():
    m = bmi(81, 1.83)
    assert abs(m - 24) < 0.5


def test_bmi_zero():
    m = bmi(81, 0)
    assert abs(m - 24) < 0.5
