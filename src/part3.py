# Your exercises should appear in this file.
 
 
def list_search(l, value):
    """Return the index of the value in the list"""
    if value in l:
        index = l.index(value)
    else:
        index = 0
    return index
 
 
def phonebook_search(phonebook, search_name):
    """Return het telefoonnummer van de gevraagde persoon
 
    Als de persoon niet in het telefoonboek staat, geef dan None terug.
 
    phonebook: een list van lists met hierin naam, telefoonnummer paren
    search_name: de naam van de te zoeken persoon
    """
    for sublist in phonebook:
        if sublist[0] == search_name:
            return sublist[1]
    return None
 
 
def phonebook_add(phonebook, name, number):
    """Voeg het telefoonnummer voor 'name' aan de lijst toe.
 
    Als het koppel name,number al in het telefoonboek zit,
    voeg het dan niet toe, maar toon "data reeds in telefoonboek"
    op het scherm.
    Als de telefoonnummer reeds voor een ander persoon in het telefoonboek
    staat, voeg het dan niet toe, maar toon "ander persoon met deze nummer
    in telefoonboek" op het scherm.
    """
    for sublist in phonebook:
        if sublist[0] == name:
            print("data reeds in telefoonboek")
            return
        if sublist[1] == number:
            print("ander persoon met deze nummer in telefoonboek")
            return
    
    data = [name, number]
    phonebook.append(data)
    return
 
 
def phonebook_remove(phonebook, name, number):
    """Verwijder het koppel name,number van het telefoonboek.
 
    Indien het koppel niet voorkomt, print dan
    "persoon niet gevonden in telefoonboek" op het scherm.
    """
    data = [name, number]
    if data in phonebook:
        phonebook.remove(data)
        return
    else:
        print("persoon niet gevonden in telefoonboek")
        return
 
 
def phonebook_print(phonebook, search_name):
    """Print de telefoonnummers van de gevraagde persoon
 
    Als de persoon niet in het telefoonboek staat, toon dan "niets gevonden".
 
    phonebook: een list van lists met hierin naam, telefoonnummer paren
    search_name: de naam van de te zoeken persoon
    """
    result = False
    for sublist in phonebook:
        if sublist[0] == search_name:
            print(sublist[1])
            result = True
 
    if result == True:
        return
    else:
        print("niets gevonden")
 