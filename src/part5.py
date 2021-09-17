# We gaan nu een adresboek opstellen met behulp van
# een enkele dictionary.
# Deze datastructuur maakt het implementeren van
# onderstaande functies eenvoudiger en efficienter.
 
 
def addressbook_search(addressbook, search_name):
    """Return het adres van de gevraagde persoon
 
    Als de persoon niet in het adresboek staat, geef dan None terug.
 
    addressbook: een list van lists met hierin naam, adres paren
    search_name: de naam van de te zoeken persoon
    """
    if search_name in addressbook:
        return addressbook[search_name]
    return None
 
 
def addressbook_add(addressbook, name, address):
    """Voeg het 'adres' voor 'name' aan de lijst toe.
 
    Als voor deze persoon al een adres in het adresboek zit,
    voeg het dan niet toe, maar toon "persoon reeds in adresboek"
    op het scherm.
    """
    if name in addressbook:
        print("persoon reeds in adresboek")
        return None
    
    addressbook[name] = address
    return addressbook