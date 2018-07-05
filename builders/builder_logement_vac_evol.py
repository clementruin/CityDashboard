# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 23:13:52 2018

@author: Hervé
"""

import json
import csv

readfile = open('static_raw/Logements_vacants_IDF_1962-2009.csv', 'r')
reader = csv.DictReader(readfile, delimiter=';')
city_dico = {}
for line in reader:
	code = line["INSEE"]
	dico = {
		"LogVac62" : float(line["lv1962"]),
		"LogVac68" : float(line["lv1968"]),
		"LogVac75" : float(line["lv1975"]),
		"LogVac82" : float(line["lv1982"]),
		"LogVac90" : float(line["lv1990"]),
		"LogVac99" : float(line["lv1999"]),
		"LogVac06" : float(line["lv2006"]),
		"LogVac07" : float(line["lv2007"]),
		"LogVac08" : float(line["lv2008"]),
      	"LogVac09" : float(line["lv2009"])
	}
	city_dico[code] = dico

readfile.close()

with open('static_dic/Logement_vac_evol.json', 'w') as file:
    json.dump(city_dico, file)