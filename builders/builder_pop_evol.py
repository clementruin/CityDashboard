# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 15:13:10 2018

@author: Hervé
"""

import json
import csv

readfile = open('static_raw/Population 1962-2011.csv', 'r')
reader = csv.DictReader(readfile, delimiter=';')
city_dico = {}
for line in reader:
	code = line["insee"]
	dico = {
		"Pop46" : float(line["Pop1946"]),
		"Pop62" : float(line["PSDC1962"]),
		"Pop68" : float(line["PSDC1968"]),
		"Pop75" : float(line["PSDC1975"]),
		"Pop82" : float(line["PSDC1982"]),
		"Pop90" : float(line["PSDC1990"]),
		"Pop99" : float(line["POPEXH1999"]),
		"Pop06" : float(line["POPMUN2006"]),
		"Pop07" : float(line["POPMUN2007"]),
      	"Pop09" : float(line["POPMUN2009"]),
		"Pop10" : float(line["POPMUN2010"]),
     	"Pop11" : float(line["POPMUN2011"]),
	}
	city_dico[code] = dico

readfile.close()

with open('static_dic/pop_evol.json', 'w') as file:
    json.dump(city_dico, file)
