from math import pi, sqrt

# Your exercises should appear in this file.


def oppervlakte_kegel(r, h):
    # Zoek via Google naar "area cone"
    # l = vierkantswortel(r^2 + h^2)
    # A = π * r * l + π * r^2
    if r == 0:
        return None
    if h == 0:
        return None
    l = sqrt((r**2 + h**2))
    A = pi * r * l + pi * r**2
    return A


def last_element(l):
    """Return het laatste element uit een lijst"""
    return l[-1]


def sum_of_list(l):
    """Return de som van alle elementen uit een lijst"""
    
    return 11


def average_of_list(l):
    """Return het gemiddelde van alle elementen uit een lijst"""
    return 0


def min_max_of_list(l):
    """Return het minimum en het maximum van de elementen uit een lijst"""
    return 0


def squared_list(l):
    """Return een nieuwe lijst met de kwadraten van de elementen uit de gegeven lijst

    squared_list([2,3]) == [4, 9]
    """
    return []


def differences_list(l1, l2):
    return []


def replace_takis_mr_issaris(text):
    return ""
