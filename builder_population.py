import json
import csv

readfile = open('static_raw/population92.csv', 'r')
reader = csv.DictReader(readfile, delimiter=';')
city_dico = {}
for line in reader:
	code = line["inseecode"]
	dico = {
		"evol" : float(line["evol. annuelle moy. de la population 2009-2014"]),
		"pop" : float(line["Population 2014"]),
		"25" : float(line["Part des pers. agees de - de 25 ans 2014"]),
		"64" : float(line["Part des pers. agees de 25 a 64 ans 2014"]),
		"65+" : float(line["Part des pers. agees de 65 ans ou + 2014"]),
	}
	city_dico[code] = dico

readfile.close()

with open('static_dic/population92.json', 'w') as file:
    json.dump(city_dico, file)