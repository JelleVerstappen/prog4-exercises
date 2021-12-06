# Implementeer onderstaande functies.

def zoek_palindroom(filename):
    lijst = []
    bestand = open(filename, "rt")
    lines = bestand.readlines()

    for line in lines:
        stripped = line.strip()

        if stripped[::-1] == stripped:
           lijst.append(stripped)
    return lijst

def zoek_anagram(filename, woord):
    lijst = []
    bestand = open(filename, "rt")
    lines = bestand.readlines()

    for line in lines:
        stripped = line.strip()

        if sorted(woord) == sorted(stripped):
           lijst.append(stripped)
           lijst.remove(woord)
    return lijst

