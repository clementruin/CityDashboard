# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 23:13:52 2018

@author: Hervé
"""

import json
import csv

readfile = open('static_raw/Pop active socio-pro 2007.csv', 'r')
reader = csv.DictReader(readfile, delimiter=';')
city_dico = {}
for line in reader:
	code = line["INSEE"]
	dico = {
		"Agricole" : float(line["ActAgr"]),
		"Artisan" : float(line["ActArtcfen"]),
		"Cadre" : float(line["ActCadre"]),
		"Proint" : float(line["ActProint"]),
		"Employe" : float(line["ActEmplo"]),
		"Ouvrier" : float(line["ActOuvri"]),
		"Actif" : float(line["Actifs"])
	}
	city_dico[code] = dico

readfile.close()

with open('static_dic/Activte_categorie.json', 'w') as file:
    json.dump(city_dico, file)