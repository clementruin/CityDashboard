# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 18:57:38 2018

@author: Hervé
"""

from bs4 import BeautifulSoup
import requests

import json
import csv

bac_dico = {}

idf = ['75', '77', '78', '91', '92', '93', '94', '95']

features = [{
        "NbLycees_%d" % annee: 0,
        "Resultat_%d_(90)" % annee : 0,
        "Resultat_%d_(80-90)" % annee : 0,
        "Resultat_%d_(70-80)" % annee : 0,
        "Resultat_%d_(50-70)" % annee : 0,
        "Resultat_%d_(50)" % annee : 0,
        "Privé_%d" % annee : 0,
        "Public_%d" % annee: 0,
        } for annee in range(2008,2018)]

"""
{code : [{features of year 1}, {features of year 2},...]}
"""

### Données de 2017
# Scraping web

# Determine the accamedy or the INSEE code of a school

readfile = open('CSV/Bac 2015.csv', 'r')
reader = csv.DictReader(readfile, delimiter=';')
city_code = {}
for line in reader:
    if line["Ville"] in city_code:
        continue
    else:
        city_code[line["Ville"]] = line["Commune"]
    
def city_to_code(city):
    return city_code[city]


def departement_to_academy(dept_number):
    if dept_number == '75':
        return 'PARIS'
    elif dept_number in ['77', '93', '94']:
        return 'CRETEIL'
    elif dept_number in ['78', '91', '92', '95']:
        return 'VERSAILLES'

# data scraping

for i in range(1, 47):    
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
        if line[1].strip() not in idf :
            continue
        else :
            insee_code = city_to_code(line[2].strip()) if line[2].strip() in city_code else None
            
            if insee_code not in bac_dico :
                bac_dico[insee_code] = features
            
            bac_dico[insee_code][-1]["NbLycees_2017"] += 1
            
            resultat = float(line[-1].strip())
            if resultat >= 90 :
                bac_dico[insee_code][-1]["Resultat_2017_(90)"] += 1
            elif resultat in range(80,90):
                bac_dico[insee_code][-1]["Resultat_2017_(80-90)"] += 1
            elif resultat in range(70,80):
                bac_dico[insee_code][-1]["Resultat_2017_(70-80)"] += 1
            elif resultat in range(50,70):
                bac_dico[insee_code][-1]["Resultat_2017_(50-70)"] += 1
            else :
                bac_dico[insee_code][-1]["Resultat_2017_(50)"] += 1
            
            sector = line[3].strip()
            bac_dico[insee_code][-1]["%s_2017" % sector] += 1


### Données de 2012 à 2016
# Extraction de csv

i = 4

for annee in range(2012, 2017):
    readfile = open('CSV/Bac %d.csv' % annee, 'r')
    reader = csv.DictReader(readfile, delimiter=';')
    
    for line in reader:
        insee_code = line['Commune']
        if insee_code[:2] not in idf :
            continue
        else :
            if insee_code not in bac_dico :
                bac_dico[insee_code] = features
            
            bac_dico[insee_code][i]["NbLycees_%d" % annee] += 1
            
            resultat = float(line["Taux Brut de Réussite Total séries"])
            if resultat >= 90 :
                bac_dico[insee_code][i]["Resultat_%d_(90)" % annee] += 1
            elif resultat in range(80,90):
                bac_dico[insee_code][i]["Resultat_%d_(80-90)" % annee] += 1
            elif resultat in range(70,80):
                bac_dico[insee_code][i]["Resultat_%d_(70-80)" % annee] += 1
            elif resultat in range(50,70):
                bac_dico[insee_code][i]["Resultat_%d_(50-70)" % annee] += 1
            else :
                bac_dico[insee_code][i]["Resultat_%d_(50)" % annee] += 1
                
            if line["Secteur Public=PU Privé=PR"]=="PU":
                bac_dico[insee_code][i]["Public_%d" % annee] += 1
            else :
                bac_dico[insee_code][i]["Privé_%d" % annee] += 1

    readfile.close()
    i += 1


### Données de 2008 à 2011
# Scraping pdf2html

i=0

for annee in range(2008,2012):

    for dept in range(75,76):
        lycee_number = len(BeautifulSoup(open('E:\Centrale Paris\Projet Inno - Mantic Data\IdF\pdf\Bac_%d_%d/Bac_%d_%d_ind.html' % (dept, annee, dept, annee), 'r', encoding='utf-8').read(), "html.parser").find_all('a'))
        
        for k in range(1,lycee_number+1):
            
            page = open('E:\Centrale Paris\Projet Inno - Mantic Data\IdF\pdf\Bac_%d_%d/Bac_%d_%d-%d.html' % (dept, annee, dept, annee, k), 'r', encoding='utf-8')
            r = page.read()

            soup = BeautifulSoup(r, "html.parser")
    
            try :
                ville = soup.find_all("p", class_="ft01")[0].find('b').text.replace('\xa0', ' ').split('-')[0].strip()
                insee_code = city_to_code(ville) if ville in city_code else None
            except :
                insee_code = None
            
            try:
                resultat = float(soup.find_all("p", class_="ft05")[1].find('b').text)
            except:
                resultat = None
            
            if insee_code not in bac_dico :
                bac_dico[insee_code] = features
                
            if resultat == None :
                continue
            elif resultat >= 90 :
                bac_dico[insee_code][i]["Resultat_%d_(90)" % annee] += 1
            elif resultat in range(80,90):
                bac_dico[insee_code][i]["Resultat_%d_(80-90)" % annee] += 1
            elif resultat in range(70,80):
                bac_dico[insee_code][i]["Resultat_%d_(70-80)" % annee] += 1
            elif resultat in range(50,70):
                bac_dico[insee_code][i]["Resultat_%d_(50-70)" % annee] += 1
            else :
                bac_dico[insee_code][i]["Resultat_%d_(50)" % annee] += 1
            
            try :
                sector = "Public" if "public" in soup.find_all("p", class_="ft01")[0].find('b').text.replace('\xa0', ' ').split('-')[-1] else "Privé"
                bac_dico[insee_code][i]["%s_%d" % (sector, annee)] += 1
            except :
                continue
            
    i += 1

### Compilation dans un fichier json

with open('Bac.json', 'w') as file:
    json.dump(bac_dico, file)