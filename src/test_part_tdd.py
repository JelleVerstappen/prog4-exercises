# Schrijf hier testen voor je oefeningen.
# Begin iedere testfunctie met naam "test_" gevolgd door de
# naam van de functie die je gaat testen, gevold door 
# een naam die aangeeft wat je gaat testen.
# 
# B.v.
# Om een functie "kwadraat" te testen, kan je als eerste test
# een functie met naam "test_kwadraat_2" die test dat het
# kwadraat van 2 4 is.


from src.part_tdd import palindroom, anagram


def test_palindroom():
    result = palindroom("lmao")
    assert result == False

def test_palindroom_2():
    result = palindroom("lol")
    assert result == True

def test_palindroom_3():
    result = palindroom("Never gonna give you up")
    assert result == False
    
def test_anagram():
    result = anagram("Rick", "Astley")
    assert result == False

def test_anagram_2():
    result = anagram("Your", "Mom")
    assert result == False

def test_anagram_3():
     result = anagram("lef", "fel")
     assert result == True

