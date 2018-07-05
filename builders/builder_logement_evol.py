# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 21:55:25 2018

@author: Hervé
"""

import json
import csv

readfile = open('static_raw/Logement 1962-2009.csv', 'r')
reader = csv.DictReader(readfile, delimiter=';')
city_dico = {}
for line in reader:
	code = line["INSEE"]
	dico = {
		"Log62" : float(line["nblog62"]),
		"Log68" : float(line["nblog68"]),
		"Log75" : float(line["nblog75"]),
		"Log82" : float(line["nblog82"]),
		"Log90" : float(line["nblog90"]),
		"Log99" : float(line["nblog99"]),
		"Log06" : float(line["nblog2006"]),
		"Log07" : float(line["nbLOG2007"]),
		"Log08" : float(line["nblog2008"]),
      "Log09" : float(line["nblog2009"])
	}
	city_dico[code] = dico

readfile.close()

with open('static_dic/Logement_evol.json', 'w') as file:
    json.dump(city_dico, file)