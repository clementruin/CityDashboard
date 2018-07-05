import sqlalchemy
import csv
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
import unidecode
import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import json


def no_accent(string):
    string = string.replace('é', 'e')
    string = string.replace('è', 'e')
    string = string.replace('ë', 'e')
    string = string.replace('ï', 'i')
    string = string.replace('É', 'e')
    string = string.replace('È', 'e')
    return string

def scrap_party_date(postal_code, city):
    """Scraps party and mandate year available on every french city's Wikipedia page
    """
        # open Wiki page of the city
    try:
        city = unidecode.unidecode(city)
        url = "https://www.google.fr/search?q={}+{}+{}".format(
                'wikipedia', city, postal_code)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        # tag class name to be changed regularly
        tag = soup.find_all("div", class_="hJND5c", limit=1)
        link = tag[0].cite.text

        r = requests.get(link)
        soup = BeautifulSoup(r.text, "lxml")
        mayor_table = soup.find_all(
            "table", class_="wikitable centre communes")
        # retrieves Wikitable "Liste des maires"
        data = []
        for tables in mayor_table:
            for row in tables.find_all("tr"):
                L = row.find_all("td")
                if len(L) > 2:
                    data.append([
                        date(L[0].text), 
                        date(L[1].text), 
                        clean_party_attribute(L[3].text) 
                        ])
        return(data)
    except:
        return([])

def date(string):
    try:
        return int(re.search(r"(\d{4})", string).group(1))
    except:
        if "cours" in string:
            return 2018
        else:
            return 0


# Clean party name previously scrapped

def clean_party_attribute(string):
    string = no_accent(string)
    L = []
    se = ["SE", "sans etiquette", "Sans etiquette"]
    fn = ["FN", "fn", "National"]
    ump = ["UMP", "Republicains", "LR", "RPR"]
    dvd = ["DVD", "Divers Droite", "divers droite", "Divers droite"]
    udi = ["UDI", "Indep"]
    modem = ["MoDem", "modem", "MODEM"]
    prg = ["PRG", "Radical"]
    eelv = ["EELV", "Ecologie", "ecologie"]
    dvg = ["DVG", "Divers Gauche", "divers gauche", "Divers gauche"]
    ps = ["PS", "Socialiste", "socialiste", "ps"]
    fg = ["FG", "fg", "Front de Gauche", "front de gauche", "Front de gauche"]
    pcf = ["PCF", "Communiste", "communiste"]

    if any(i in string for i in se):
        L.append("SE")
    if any(i in string for i in fn):
        L.append("FN")
    if any(i in string for i in ump):
        L.append("UMP-LR")
    if any(i in string for i in dvd):
        L.append("DVD")
    if any(i in string for i in udi):
        L.append("UDI")
    if any(i in string for i in eelv):
        L.append("EELV")
    if any(i in string for i in modem):
        L.append("MoDem")
    if any(i in string for i in dvg):
        L.append("DVG")
    if any(i in string for i in ps):
        L.append("PS")
    if any(i in string for i in fg):
        L.append("FG")
    if any(i in string for i in pcf):
        L.append("PCF")
    if any(i in string for i in prg):
        L.append("PRG")
    if len(L) == 0:
        return "NA"
    else:
        return L[-1]


city_partis = []
readfile = open('static_raw/partis.csv', 'r')
reader = csv.DictReader(readfile, delimiter=',')
for line in reader:
    code = line["code"]
    if True:
        parti2014 = line["party"]
        name = line["name"]
        current_city_partis = []
        data = scrap_party_date(code, name)
        print(code, name)
        p2001 = "NA"
        p2008 = "NA"
        p2014 = parti2014
        for l in data :
            if l[1]>2001 and l[0]<2008:
                if p2001!="NA" and l[2]!='NA':
                    p2001 = l[2]
                if p2001=="NA":
                    p2001 = l[2]
            if l[1]>2008 and l[0]<2014:
                if p2008!="NA" and l[2]!='NA':
                    p2008 = l[2]
                if p2008=="NA":
                    p2008 = l[2] 
        print(p2001, p2008, p2014)
        city_partis.append({"code":code, "partis":{"2001":p2001, "2008":p2008, "2014":p2014}})


with open('static_dic/partisidf.json', 'w') as file:
    json.dump(city_partis, file)
