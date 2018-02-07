"""
import csv

readfile = open('database.csv', 'r')
writefile = open('budgets.csv','w')
outcsv = csv.writer(writefile)
reader = csv.DictReader(readfile, delimiter=',')
outcsv.writerow(['budget','population'])
for line in reader:
	a = float(line['total des produits de fonctionnement'])+float(line['total des charges de fonctionnement'])
	b = float(line['population'])
	outcsv.writerow([a,b])
readfile.close()
writefile.close()
"""
import json
import csv

readfile = open('city_budgets_idf.csv', 'r')
reader = csv.DictReader(readfile, delimiter=',')
city_list = []
codes = []
for line in reader:
	if True :
		code = line["inseecode"]
		if code in codes:
			for city in city_list:
				if city["code"]==code:
					current_year_dico = {
						"year" : line["annee"],
						"values" : {
							"budget": float(line["total des charges de fonctionnement = b"])+float(line["total des emplois d investissement = d"])+float(line["total des produits de fonctionnement = a"])+float(line["total des ressources d investissement = c"]),
							"depenses": float(line["total des charges de fonctionnement = b"])+float(line["total des emplois d investissement = d"]),
							"d1": float(line["total des charges de fonctionnement = b"]),
							"d1.1": float(line["achats et charges externes"]),
							"d1.2": float(line["charges de personnel"]),
							"d1.3": float(line["charges financieres"]),
							"d1.4": float(line["contingents"]),
							"d1.5": float(line["subventions versees"]),
							"d2": float(line["total des emplois d investissement = d"]),
							"d2.1": float(line["charges a repartir"]),
							"d2.2": float(line["depenses d’equipement"]),
							"d2.3": float(line["remboursement d'emprunts et dettes assimilees"]),
							"recettes": float(line["total des produits de fonctionnement = a"])+float(line["total des ressources d investissement = c"]),
							"r1": float(line["total des produits de fonctionnement = a"]),
							"r1.1": float(line["autres impots et taxes"]),
							"r1.2": float(line["dotation globale de fonctionnement"]),
							"r1.3": float(line["impots locaux"]),
							"r2": float(line["total des ressources d investissement = c"]),
							"r2.1": float(line["emprunts bancaires et dettes assimilees"]),
							"r2.2": float(line["subventions recues"]) 
								}
							}
					city["years"].append(current_year_dico)
		else :
			codes.append(code)
			current_year_dico = {
				"year" : line["annee"],
				"values" : {
					"budget": float(line["total des charges de fonctionnement = b"])+float(line["total des emplois d investissement = d"])+float(line["total des produits de fonctionnement = a"])+float(line["total des ressources d investissement = c"]),
					"depenses": float(line["total des charges de fonctionnement = b"])+float(line["total des emplois d investissement = d"]),
					"d1": float(line["total des charges de fonctionnement = b"]),
					"d1.1": float(line["achats et charges externes"]),
					"d1.2": float(line["charges de personnel"]),
					"d1.3": float(line["charges financieres"]),
					"d1.4": float(line["contingents"]),
					"d1.5": float(line["subventions versees"]),
					"d2": float(line["total des emplois d investissement = d"]),
					"d2.1": float(line["charges a repartir"]),
					"d2.2": float(line["depenses d’equipement"]),
					"d2.3": float(line["remboursement d'emprunts et dettes assimilees"]),
					"recettes": float(line["total des produits de fonctionnement = a"])+float(line["total des ressources d investissement = c"]),
					"r1": float(line["total des produits de fonctionnement = a"]),
					"r1.1": float(line["autres impots et taxes"]),
					"r1.2": float(line["dotation globale de fonctionnement"]),
					"r1.3": float(line["impots locaux"]),
					"r2": float(line["total des ressources d investissement = c"]),
					"r2.1": float(line["emprunts bancaires et dettes assimilees"]),
					"r2.2": float(line["subventions recues"]) 
						}
					}
			city_list.append({"code":code, "years":[current_year_dico]})

readfile.close()

with open('budgets.json', 'w') as file:
    json.dump(city_list, file)

