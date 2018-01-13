import json
import csv

readfile = open('static_raw/activite2014_92.csv', 'r')
reader = csv.DictReader(readfile, delimiter=';')
city_dico = {}
for line in reader:
	code = line["inseecode"]
	dico = {
		"nom" : line["Libelle"],
		"emploi" : float(line["Nb d'emplois au lieu de travail (LT) 2014"]),
		"15_24" : float(line["Taux d'activite des 15 24 ans 2014"]),
		"25_54" : float(line["Taux d'activite des 25 54 ans 2014"]),
		"55_64" : float(line["Taux d'activite des 55 64 ans 2014"]),
		"agri" : float(line["Part des agriculteurs expl. dans le nb d emplois au LT 2014"]),
		"autre" : float(line["Part des artisans, commercants, chefs d ent. dans le nb d emplois au LT 2014"]),
		"cadre" : float(line["Part des cadres et prof. intellectuelles sup. dans le nb d emplois au LT 2014"]),
		"ouvri" : float(line["Part des ouvriers dans le nb d emplois au LT 2014"])
	}
	city_dico[code] = dico

readfile.close()

with open('static_dic/activite2014.json', 'w') as file:
    json.dump(city_dico, file)