def maak_videokaart_dict(merk, naam, architectuur, geheugen, busbreedte, diesize, jaar):
    """Geef een dictionary terug met alle gegevens die als parameters aan
    de functie meegegeven werden.

    Bijvoorbeeld:
    >>> maak_videokaart_dict("NVIDIA", "RTX 3080", "Ampere", 10, 320, 628, 2020)
    {'merk': 'NVIDIA', 'naam': 'RTX 3080', 'architectuur': 'Ampere', 'geheugen': 10, 'busbreedte': 320, 'diesize': 628, 'jaar': 2020}
    """
    GPUs = {}
    GPUs["merk"] = merk
    GPUs["naam"] = naam
    GPUs["architectuur"] = architectuur
    GPUs["geheugen"] = geheugen
    GPUs["busbreedte"] = busbreedte
    GPUs["diesize"] = diesize
    GPUs["jaar"] = jaar

    return GPUs

def tel_videokaarten(lijst_videokaarten):
    """Geef het totaal aantal videokaarten in de lijst van videokaarten terug."""
    aantal = []
    aantal = len(lijst_videokaarten)
    return aantal


def tel_videokaarten_per_merk(lijst_videokaarten):
    """Geef het aantal videokaarten per merk in de lijst van videokaarten terug.

    Het resultaat is dus een dictionary met 2 keys:
    {
        "AMD": x,
        "NVIDIA": y,
    }
    Met x het aantal AMD videokaarten in de lijst en y het aantal NVIDIA
    videokaarten in de lijst.
    """
    Merk = {"NVIDIA": 0, "AMD": 0}
    for i in lijst_videokaarten:
        if i["merk"] == "NVIDIA":
            Merk["NVIDIA"]+=1
        if i["merk"] == "AMD":
            Merk["AMD"]+=1
    return Merk



def grootste_videokaart(lijst_videokaarten):
    """Gegeven een lijst met videokaarten, geef je een de naam terug
    van de grootste videokaart.

    Bijvoorbeeld:
    >>> grootste_videokaart([{'naam': 'RTX 3080', 'diesize': 628}])
    'RTX 3080'
    """
    biggest_die = max([GPU['diesize'] for GPU in lijst_videokaarten])
    data_biggest_die = [GPU for GPU in lijst_videokaarten if GPU["diesize"] == biggest_die]
    return data_biggest_die[0]["naam"]


def grootste_videokaartgrootte_per_merk(lijst_videokaarten):
    """Gegeven een lijst met videokaarten, geef je een dictionary terug met
    voor ieder merk de omvang van de grootste kaart.

    Bijvoorbeeld:
    >>> grootste_videokaartgrootte_per_merk([{'merk': 'NVIDIA', 'naam': 'RTX 3080', 'diesize': 628}])
    {'AMD': 0, 'NVIDIA': 628}
    """
    die_per_merk = {"NVIDIA": 0, "AMD": 0}

    for GPU in lijst_videokaarten:
        if GPU["merk"] == "NVIDIA":
            if GPU["diesize"] > die_per_merk["NVIDIA"]:
                die_per_merk["NVIDIA"] = GPU["diesize"]
            
        if GPU["merk"] == "AMD":
            if GPU["diesize"] > die_per_merk["AMD"]:
                die_per_merk["AMD"] = GPU["diesize"]
    return die_per_merk


def diesizes_videokaarten(lijst_videokaarten):
    """Gegeven een lijst van dictionaries met informatie over vidoekaarten,
    geef je een lijst van diesizes terug.

    Bijvoorbeeld:
    >>> diesizes_videokaarten([{"diesize": 500}, {"diesize": 300}])
    [500, 300]
    """
    dies = []
    for GPU in lijst_videokaarten:
        die = GPU["diesize"]
        dies.append(die)
    return dies



def gemiddelde_diesize_videokaarten(lijst_videokaarten):
    """Gegeven een lijst van dictionaries met informatie over videokaarten,
    geef je de gemiddelde diesize terug.

    Bijvoorbeeld:
    >>> gemiddelde_diesize_videokaarten([{"diesize": 500}, {"diesize": 300}])
    400.0
    """
    die_som = 0
    for GPU in lijst_videokaarten:
        die_som += GPU["diesize"]
        die_avg = die_som/len(lijst_videokaarten)
    return die_avg


def jaren_videokaarten(lijst_videokaarten):
    """Gegeven een lijst van dictionaries met informatie over videokaarten,
    geef je een lijst van jaartalen terug waarin de videokaarten uitgebracht werden.

    Bijvoorbeeld:
    >>> jaren_videokaarten([{"jaar": 2020, "diesize": 500}, {"jaar": 2021, "diesize": 300}])
    [2020, 2021]
    """
    jaartallen = []
    for GPU in lijst_videokaarten:
        jaartallen.append(GPU["jaar"])
    return jaartallen


def videokaarten_voor_jaar(lijst_videokaarten, jaar):
    """Gegeven een lijst van dictionaries met informatie over videokaarten,
    geef je een lijst van dictionaries terug met informatie over videokaarten
    voor het opgegeven jaar.

    Bijvoorbeeld:
    >>> videokaarten_voor_jaar([{"jaar": 2020, "diesize": 500}, {"jaar": 2021, "diesize": 300}], 2020)
    [{'jaar': 2020, 'diesize': 500}]
    """


def grootste_geheugen_per_jaar(lijst_videokaarten):
    """Gegeven een lijst van dictionaries met informatie over videokaarten,
    geef je een dictionary terug met de grootste geheugengrootte per jaar.

    Bijvoorbeeld:
    >>> grootste_geheugen_per_jaar([{"jaar": 2020, "geheugen": 4}, {"jaar": 2021, "geheugen": 8}])
    {2020: 4, 2021: 8}
    """
    GPU_jaar = []
    for GPU in lijst_videokaarten:
        if jaar == GPU["jaar"]:
            GPU_jaar.append(GPU)
    return GPU_jaar
