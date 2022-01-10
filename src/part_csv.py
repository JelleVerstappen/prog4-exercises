# Haal de dataset met naam "Confirmed cases by date, age, sex and province"
# in CSV-formaat af van de Sciensano-website:
# https://epistat.wiv-isp.be/covid/
#
# Dit bestand heeft naam "COVID19BE_CASES_AGESEX.csv".

import csv

def determine_total_cases(age_category, gender):
    """Geeft het totaal aantal COVID19 gevallen terug voor de gegeven leeftijdscategorie en het gegeven geslacht
    B.v.
    determine_total_cases("20-29", "M") geeft het aantal besmettingen van mannen tussen de 20 en 29 jaar oud
    terug. 
    """
    cases = 0
    f = open("src/COVID19BE_CASES_AGESEX.csv", "r")
    reader = csv.reader(f, delimiter = ',')
    for row in reader:
        if row[3] == age_category and row[4] == gender:
            cases+= int(row[5])

    return(cases)
        



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
    age1_cases = 0
    age2_cases = 0
    age3_cases = 0
    f = open("src/COVID19BE_CASES_AGESEX.csv", "r")
    reader = csv.reader(f, delimiter = ',')

    f2 = open("src/overzicht.csv", "w")
    writer = csv.writer(f2)
    for row in reader:
        if row[3] == '0-9':
            age1_cases += int(row[5])
    writer.writerow(['0-9', age1_cases])
    

     


print(output_total_cases("COVID19BE_CASES_AGESEX.csv", "overzicht.csv"))   
#print(determine_total_cases("10-19", "M"))