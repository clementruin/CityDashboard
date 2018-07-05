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


### Données de 2008 à 2011
# Scraping pdf2html

for i in range(2008,2009):
    dico = {}

    for j in range(75,76):
        lycee_number = len(BeautifulSoup(open('E:\Centrale Paris\Projet Inno - Mantic Data\IdF\pdf\Bac_%d_%d/Bac_%d_%d_ind.html' % (j, i, j, i), 'r', encoding='utf-8').read(), "html.parser").find_all('a'))
        
        for k in range(1,lycee_number+1):
            
            page = open('E:\Centrale Paris\Projet Inno - Mantic Data\IdF\pdf\Bac_%d_%d/Bac_%d_%d-%d.html' % (j, i, j, i, k), 'r', encoding='utf-8')
            r = page.read()

            soup = BeautifulSoup(r, "html.parser")

            lycee = soup.find_all("p", class_="ft00")[0].find('b').text.replace('\xa0', ' ')
    
            ville = soup.find_all("p", class_="ft01")[0].find('b').text.replace('\xa0', ' ').split('-')[0].strip()

            secteur = "Public" if "public" in soup.find_all("p", class_="ft01")[0].find('b').text.replace('\xa0', ' ').split('-')[-1] else "Privé"
            
            try:
                resultat = soup.find_all("p", class_="ft05")[1].find('b').text
            except:
                resultat = None
            
            sub_dico = {
                    "Ville" : ville,
                    "Commune" : city_to_code(ville) if ville in city_dico else None,
                    "Académie" : departement_to_academy(str(j)),
                    "Secteur" : secteur,
                    "Résultat" : resultat
                    }
            dico[lycee] = sub_dico
    
    bac_dico[i] = dico
        
### Compilation dans un fichier json

with open('Bac1.json', 'w') as file:
    json.dump(bac_dico, file)
