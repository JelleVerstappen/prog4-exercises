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
    length = len(l)
    totalsum = 0
    for i in range(0, length, 1):
        totalsum = totalsum + l[0+i]
    return totalsum
 
 
def average_of_list(l):
    """Return het gemiddelde van alle elementen uit een lijst"""
    som = sum(l)
    length = len(l)
    average = som/length
    return average
 
 
def min_max_of_list(l):
    """Return het minimum en het maximum van de elementen uit een lijst"""
    minimum = min(l)
    maximum = max(l)
    return minimum, maximum
 
 
def squared_list(l):
    """Return een nieuwe lijst met de kwadraten van de elementen uit de gegeven lijst
 
    squared_list([2,3]) == [4, 9]
    """
    length = len(l)
    squared = []
    for i in range(0, length, 1):
        squared.append(l[0+i]**2)
    return squared
 
 
def differences_list(l1, l2):
    lijst = []
    length = len(l1)
    length2 = len(l2)
 
    if length != length2:
        raise ValueError
 
    for i in range(0, length, 1):
        item = l1[0+i] - l2[0+i]
        lijst.append(item)
    return lijst
 
 
def replace_takis_mr_issaris(text):
    changedtext = text.replace("Takis", "Mr. Issaris")
    return changedtext