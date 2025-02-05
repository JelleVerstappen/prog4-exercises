# Schrijf voor onderstaande oefeningen eerst de testen in test_part_tdd.py
# Implementeer ze vervolgens in dit bestand.

# Oefening 1
# ==========
# Schrijf een functie palindroom, die controlleert of een bepaalde string
# een palindroom is.
# > palindroom("lol")
# True

from datetime import timedelta


def palindroom(message):
    reverse = message[::-1]
    if message == reverse:
        return True
    else:
        return False




# Oefening 2
# ==========
# Schrijf een functie anagram, die controlleert of een twee gegeven woorden
# anagrammen zijn van elkaar.
# > anagram("lol", "lot")
# False
# > anagram("tol", "lot")
# True
def anagram(word1, word2):

    replace1 = word1.replace(" ","")
    replace2 = word2.replace(" ","")

    low1 = replace1.lower()
    low2 = replace2.lower()

    sort1 = sorted(low1)
    sort2 = sorted(low2)

    if sort1 == sort2:
        return True
    else:
        return False

# Oefening 3
# ==========
# Schrijf een functie leeftijd, die gegeven een datum, je leeftijd in jaren
# teruggeeft:
# > leeftijd(1976, 12, 20)
# 44
# > leeftijd(1976, 2, 10)
# 45
# 
# Tip: Gebruik de datetime module:
# datetime.date.now() geeft de huidige datum
# datetime.date.date(year=2021, month=1, day=1) stelt 1 januari voor
# Je kan data van elkaar aftrekken.

def leeftijd(year, month, day):
    import datetime
    difference = datetime.date.today() - datetime.date(year, month, day)
    sec = difference.total_seconds()
    age = sec//(365*24*60*60)
    return age