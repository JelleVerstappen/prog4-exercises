# Schrijf testen voor de functies die je in part_testing.py vindt.
from .part_testing import bmi, maximum, pythagoras

def test_maximum():
    result = maximum(0, -1)

    assert result == 0

def test_maximum_2():
    result = maximum(5, 10)

    assert result == 10

