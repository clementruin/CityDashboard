import json
import csv

readfile = open('static_raw/Logement92.csv', 'r')
reader = csv.DictReader(readfile, delimiter=';')
city_dico = {}
for line in reader:
	code = line["Code"]
	dico = {
    
    "housing" : float(line['Nb de logements 2014']),
    "main_res" : float(line['Nb de résidences principales 2014']),
    "portion_hlm_tenant" : float(line['Part des locataires HLM dans les rés. principales 2014']),
    "social_housing" : float(line['NB_LOGEMENTS_LOCATIFS_SOCIAUX']),
  
	}
	city_dico[code] = dico

readfile.close()

with open('static_dic/Logement92.json', 'w') as file:
    json.dump(city_dico, file)
