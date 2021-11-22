import math


def maximum(x, y):
    if x > y:
        return x
    return y


def bmi(g, l):
    """Geef de BMI terug voor een persoon met lengte l en gewicht g
    l is uitgedrukt in m
    g is uitgedrukt in kg

    Geeft -1 terug als geen BMI berekend kan worden.
    """
    return g / l ** 2


def pythagoras(a, b):
    return math.sqrt(a ** 2 + b ** 2)
