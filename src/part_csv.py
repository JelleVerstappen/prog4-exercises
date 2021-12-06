# Haal de dataset met naam "Confirmed cases by date, age, sex and province"
# in CSV-formaat af van de Sciensano-website:
# https://epistat.wiv-isp.be/covid/
#
# Dit bestand heeft naam "COVID19BE_CASES_AGESEX.csv".

import csv
import 
def determine_total_cases(age_category, gender):
    """Geeft het totaal aantal COVID19 gevallen terug voor de gegeven leeftijdscategorie en het gegeven geslacht
    B.v.
    determine_total_cases("20-29", "M") geeft het aantal besmettingen van mannen tussen de 20 en 29 jaar oud
    terug. 
    """
    rows = []
    f = open("csv_dataset.csv", "r")
    reader = csv.reader(f, delimiter = ',')
    for row in reader:
        rows = rows.append[row]
    print(rows) 
        



def output_total_cases(input_filename, output_filename):
    """Schrijf een functie die het invoerbestand inleest
    en per leeftijdscategorie het totaal aantal besmettingen toont.
    Dus, volgende aanroep:
    create_total_cases("COVID19BE_CASES_AGESEX.csv", "overzicht.csv") 
    Maakt een bestand "overzicht.csv" met hierin:
    "0-9", 19999
    "10-19", 10020
    "29-39", 31231
    ...
    "90+", 123123
    """
    return 0

determine_total_cases(1-2, "M")