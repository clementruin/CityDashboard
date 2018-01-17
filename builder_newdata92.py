import json
import csv
import codecs


readfile = open('static_raw/newdata92.csv','r', encoding ="utf-8")
reader = csv.DictReader(readfile, delimiter=';')
city_dico = {}
for line in reader:
	code = line["CODGEO"]
	dico = {
    
    "Pharmacy_perfume" : float(line['Nb Pharmacies et parfumerie']),
    "Entrepreneurship" : float(line['Dynamique Entrepreneuriale']),
    "Demo_index" : line['Indice Demographique'],
    "household index" : line['Indice Menages'],
    "household_amnt" : float(line['Nb Menages']),
    "main residences" : float(line['Nb Residences Principales']),
    "second_residences" : float(line['Nb proprietaire']),
    "housing" : float(line['Nb Logement']),
    "empty_housing" : float(line['Nb Log Vacants']),
    "women" : float(line['Nb Femme']),
    "men" : float(line['Nb Homme']),
    "juniors" : float(line['Nb Mineurs']),
    "seniors" : float(line['Nb Majeurs']),
    "trade_companies" : float(line['Nb Entreprises Secteur Commerce']),
    "company_creation" : float(line['Nb Creation Enteprises']),
    "actives" : float(line['Nb Atifs']),
    "housing_rate": float(line['Nb Log Vacants'])/float(line['Nb Log Vacants']+line['Nb Logement']),
    "parity": float(line['Nb Femme'])/float(line['Nb Femme']+line['Nb Homme']),
    "property_rate": float(line['Nb proprietaire'])/(float(line['Nb Logement'])-float(line['Nb Log Vacants'])),
    "property_access" : float(line['Nb Log Vacants'])/float(line['Indice Menages']),
    "occupation_rate" : float(line['Nb Logement'])-float(line['Nb Log Vacants'])/float(line['Nb Menages']),
        
	}
	city_dico[code] = dico

readfile.close()

with open('static_dic/newdata92.json', 'w') as file:
    json.dump(city_dico, file)
