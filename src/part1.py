# Your exercises should appear in this file.


def add(x, y):
    som = x + y
    return som


def kwadraat(x):
    """Return het kwadraat van x"""
    kwad = x**2
    return kwad


def oppervlakte_kubus(z):
    """Return de oppervlakte van een kubus met zijde z"""
    opp = z**2 * 6
    return opp


def seconds_in_days(days=1):
    """Geef het aantal seconden in het opgegeven aantal dagen

    Als er geen parameter doorgegeven wordt, geef dan het aantal
    seconden in 1 dag terug.
    """
    sec = days * 86400
    return sec


def seconds_in_weeks(weeks):
    """Return het aantal seconden in 'week' weken."""
    sec =  weeks * (86400 * 7)
    return sec


def seconds_in_years(years):
    """Return het aantal seconden in 'years' jaren.

    Veronderstel dat ieder jaar uit exact 52 weken bestaat.
    """
    sec = years * (86400 * 7 * 52)
    return sec


def seconds_remaining_in_life(age, is_female=False):
    """Return het aantal seconden dat overblijft in je leven.

    Ga uit van een maximale levensduur van 80 jaren voor mannen,
    en 84 jaren voor vrouwen.
    """
    if is_female == True:
        rest = 84 - age
        return seconds_in_years(rest)

    if is_female == False:
        rest = 80 - age
        return seconds_in_years(rest)
    


def postcodes():
    """Return een dictionary met postcodes"""
    postcodes = {"3000" : "Leuven", "3650" : "Dilsen-Stokkem"}
    return postcodes


    return 0


def oneven_getallen(x):
    """Return een lijst met de eerste 'x' oneven getallen."""
    oneven = []

    for i in range(1, x*2, 2):
        if i % 2 != 0:
            oneven.append(i)

    return oneven