"""import json
import csv

readfile = open('static_raw/city_budgets_idf.csv', 'r')
reader = csv.DictReader(readfile, delimiter=',')
city_dico = {}
for line in reader:
	#if line["inseecode"][:2]=="92":
	if True :
		code = line["inseecode"]
		if code in city_dico:
			city_dico[code]["dette"][line["annee"]] = float(line["encours total de la dette au 31/12/n"])
		else :
			label_dico = {
				"dette": {line["annee"] : float(line["encours total de la dette au 31/12/n"])}
				}
			city_dico[code]=label_dico

readfile.close()

with open('static_dic/dette.json', 'w') as file:
    json.dump(city_dico, file)"""

import csv

readfile = open('static_raw/city_budgets_idf.csv', 'r')
writefile = open('static_raw/dette.csv','w')
outcsv = csv.writer(writefile)
reader = csv.DictReader(readfile, delimiter=',')
outcsv.writerow(['inseecode','dette'])
for line in reader:
	a = float(line['inseecode'])
	b = float(line['encours total de la dette au 31/12/n'])
	outcsv.writerow([a,b])
readfile.close()
writefile.close()