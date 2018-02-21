# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:21:31 2018

@author: Hervé
"""

from bs4 import BeautifulSoup
import requests

import json
import csv

bac_dico = {}

### Données de 2012 à 2016
# Extraction de csv

city = ['75', '77', '78', '91', '92', '93', '94', '95']
    
for i in range(2012, 2017):    
    readfile = open('CSV/Bac %d.csv' % i, 'r')
    reader = csv.DictReader(readfile, delimiter=';')

    annee = i
    dico = {}

    for line in reader:
        if line["Commune"][:2] not in city :
            continue
        else :
            lycee = line["Etablissement"]
            sub_dico = {
                    "Ville" : line["Ville"],
                    "Commune" : line["Commune"],
                    "Académie" : line["Académie"],
                    "Secteur" : "Public" if line["Secteur Public=PU Privé=PR"]=="PU" else "Privé",
                    "Résultat" : float(line["Taux Brut de Réussite Total séries"])
                    }
            
            dico[lycee] = sub_dico
    
    bac_dico[annee] = dico

    readfile.close()
    
### Données de 2017
# Scraping web

readfile = open('CSV/Bac 2015.csv', 'r')
reader = csv.DictReader(readfile, delimiter=';')
city_dico = {}
for line in reader:
    if line["Ville"] in city_dico:
        continue
    else:
        city_dico[line["Ville"]] = line["Commune"]
    
def city_to_code(city):
    return city_dico[city]

def departement_to_academy(dept_number):
    if dept_number == '75':
        return 'PARIS'
    elif dept_number in ['77', '93', '94']:
        return 'CRETEIL'
    elif dept_number in ['78', '91', '92', '95']:
        return 'VERSAILLES'


dico = {}

for i in range(1, 41):    
    r = requests.get('http://www.letudiant.fr/palmares/classement-lycees/ile-de-france/page-%d.html' % i)
    soup = BeautifulSoup(r.text, "html.parser")

    request_boxes = soup.find_all("tr")
    
    line = []
    for box in request_boxes:
        line.append(box)
    del line[0]
    
    data = []
    for row in line:
        cell = row.find_all("td")
        
        temp = []
        for value in cell:
            temp.append(value.text)
        del temp[7]
        
        data.append(temp[3:8])
    
    for line in data:
        if line[1].strip() not in city :
            continue
        else :
            lycee = str(line[0])
            sub_dico = {
                    "Ville" : line[2].strip(),
                    "Commune" : city_to_code(line[2].strip()) if (line[2].strip() in city_dico) else line[1].strip(),
                    "Académie" : departement_to_academy(line[1].strip()),
                    "Secteur" : line[3].strip(),
                    "Résultat" : float(line[-1].strip())
                    }
        dico[lycee] = sub_dico

bac_dico[2017] = dico
    
    
### Compilation dans un fichier json

with open('Bac.json', 'w') as file:
    json.dump(bac_dico, file)