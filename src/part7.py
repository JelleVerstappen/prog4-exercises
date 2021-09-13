def write_rick_and_morty(filename):
    """Schrijf de tekst "Rick and Morty" naar het tekstbestand met naam filename"""
    file = open(filename, "wt")
    file.write("Rick and Morty")
    file.close()
    

def write_numbers(filename):
    """Schrijf de getallen van 0 tot en met 99 in het bestand met naam filename.

    Schrijf ieder getal op een aparte regel.

    Bijvoorbeeld:
    0
    1
    2
    ...
    99
    """
    file = open(filename, "wt")
    for i in range(0, 100):
        file.write(f"{i}\n")
    file.close()
    

def write_numbers_and_squares(filename):
    """Schrijf de getallen gevolgd door de kwadraten naar het bestand filename.

    Schrijf ieder getal en kwadraat ervan gescheiden door een komma op een aparte regel.

    Bijvoorbeeld:
    0,0
    1,1
    2,4
    3,9
    4,16
    ...
    """
    file = open(filename, "wt")
    for i in range (0,100):
        file.write(f"{i},{i**2}\n")
    file.close()

def sum_numbers_from_file(filename):
    """Geef de som terug van alle getallen in bestand met naam filename

    De getallen staan allen op aparte regels.

    Bijvoorbeeld, een bestand getallen.txt met inhoud:
    100
    20
    8

    Zou bij oproep read_numbers('getallen.txt') 128 teruggeven, dus:
    >> v = read_numbers('getallen.txt')
    >> print(v) # toont 128
    """
    sum = 0
    file = open(filename, "rt")
    lines = file.readlines()
    for i in lines:
        try:
            sum = sum + int(i)
        except:
            continue
    return sum



def sum_two_columns_of_numbers_from_file(filename):
    """Geef twee sommen terug van de twee kolommen in bestand met naam filename

    De getallen van alle kolommen staan allen op aparte regels. De kolommen
    zijn gescheiden door komma's.

    Bijvoorbeeld, een bestand getallen.txt met inhoud:
    12,99
    8,1
    7,4

    Heeft twee kolommen, de som van de getallen van kolom 1 is 27, de som
    van de getallen in kolom 2 is 104.

    >> v = sum_two_columns_of_numbers_from_file('getallen.txt')
    >> print(v) # toont (27, 104)
    """
    sum1 = 0
    sum2 = 0
    file = open(filename, "rt")
    lines = file.readlines()
    for i in lines:
        try:
            b = i.split(",")
            sum1 = sum1 + int(b[0])
            sum2 = sum2 + int(b[1])
        except:
            continue
    return(sum1, sum2)


def count_words_from_file(filename):
    """Geef het aantal woorden terug in bestand met naam filename"""
    words = 0
    file = open(filename, "rt")
    lines = file.readlines()
    for line in lines:
        b = line.split()
        words = words + len(b)
    return words


def count_word_frequency_from_file(filename):
    """Geef een dictionary terug met per woord het aantal keer dat het woord voorkomt

    Bijvoorbeeld voor een bestand met inhoud:
    Ik drink veel koffie en veel bruiswater. En veel koffie. En ook koffie.

    {
        "ik": 1,
        "en": 3,
        "koffie": 3,
        "drink": 1,
        "veel": 3,
        ...
    }

    Tips:
    - maak alle woorden lowercase
    - verwijder alle leestekens, zeker ",.?"
    - verwijder de newlines '\\n' mbv de method strip()
    """
    freq = {}
    file = open(filename, "rt")
    lines = file.readlines()
    for line in lines:
        NoComma = line.strip(",")
        NoQM = NoComma.strip("?")
        NoPoint = NoQM.strip(".")
        NoNewLine = NoPoint.strip("\\n")
        Lower = NoNewLine.lower()
        
 


    return None
