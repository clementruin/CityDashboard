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

readfile = open('static_raw/city_budgets_idf.csv', 'r')
reader = csv.DictReader(readfile, delimiter=',')
city_dico = {}
for line in reader:
	code = line["inseecode"]
	year = line["annee"]
	if code in city_dico.keys():
		city_dico[code]["budget_{}".format(year)] = float(line["total des charges de fonctionnement = b"])+float(line["total des emplois d investissement = d"])+float(line["total des produits de fonctionnement = a"])+float(line["total des ressources d investissement = c"])
		city_dico[code]["depenses_{}".format(year)] = float(line["total des charges de fonctionnement = b"])+float(line["total des emplois d investissement = d"])
		city_dico[code]["d1_{}".format(year)] = float(line["total des charges de fonctionnement = b"])
		city_dico[code]["d1.1_{}".format(year)] = float(line["achats et charges externes"])
		city_dico[code]["d1.2_{}".format(year)] = float(line["charges de personnel"])
		city_dico[code]["d1.3_{}".format(year)] = float(line["charges financieres"])
		city_dico[code]["d1.4_{}".format(year)] = float(line["contingents"])
		city_dico[code]["d1.5_{}".format(year)] = float(line["subventions versees"])
		city_dico[code]["d2_{}".format(year)] = float(line["total des emplois d investissement = d"])
		city_dico[code]["d2.1_{}".format(year)] = float(line["charges a repartir"])
		city_dico[code]["d2.2_{}".format(year)] = float(line["depenses d’equipement"])
		city_dico[code]["d2.3_{}".format(year)] = float(line["remboursement d'emprunts et dettes assimilees"])
		city_dico[code]["recettes_{}".format(year)] = float(line["total des produits de fonctionnement = a"])+float(line["total des ressources d investissement = c"])
		city_dico[code]["r1_{}".format(year)] = float(line["total des produits de fonctionnement = a"])
		city_dico[code]["r1.1_{}".format(year)] = float(line["autres impots et taxes"])
		city_dico[code]["r1.2_{}".format(year)] = float(line["dotation globale de fonctionnement"])
		city_dico[code]["r1.3_{}".format(year)] = float(line["impots locaux"])
		city_dico[code]["r2_{}".format(year)] = float(line["total des ressources d investissement = c"])
		city_dico[code]["r2.1_{}".format(year)] = float(line["emprunts bancaires et dettes assimilees"])
		city_dico[code]["r2.2_{}".format(year)] = float(line["subventions recues"])
	else : 
		city_dico[code] = {}
		city_dico[code]["budget_{}".format(year)] = float(line["total des charges de fonctionnement = b"])+float(line["total des emplois d investissement = d"])+float(line["total des produits de fonctionnement = a"])+float(line["total des ressources d investissement = c"])
		city_dico[code]["depenses_{}".format(year)] = float(line["total des charges de fonctionnement = b"])+float(line["total des emplois d investissement = d"])
		city_dico[code]["d1_{}".format(year)] = float(line["total des charges de fonctionnement = b"])
		city_dico[code]["d1.1_{}".format(year)] = float(line["achats et charges externes"])
		city_dico[code]["d1.2_{}".format(year)] = float(line["charges de personnel"])
		city_dico[code]["d1.3_{}".format(year)] = float(line["charges financieres"])
		city_dico[code]["d1.4_{}".format(year)] = float(line["contingents"])
		city_dico[code]["d1.5_{}".format(year)] = float(line["subventions versees"])
		city_dico[code]["d2_{}".format(year)] = float(line["total des emplois d investissement = d"])
		city_dico[code]["d2.1_{}".format(year)] = float(line["charges a repartir"])
		city_dico[code]["d2.2_{}".format(year)] = float(line["depenses d’equipement"])
		city_dico[code]["d2.3_{}".format(year)] = float(line["remboursement d'emprunts et dettes assimilees"])
		city_dico[code]["recettes_{}".format(year)] = float(line["total des produits de fonctionnement = a"])+float(line["total des ressources d investissement = c"])
		city_dico[code]["r1_{}".format(year)] = float(line["total des produits de fonctionnement = a"])
		city_dico[code]["r1.1_{}".format(year)] = float(line["autres impots et taxes"])
		city_dico[code]["r1.2_{}".format(year)] = float(line["dotation globale de fonctionnement"])
		city_dico[code]["r1.3_{}".format(year)] = float(line["impots locaux"])
		city_dico[code]["r2_{}".format(year)] = float(line["total des ressources d investissement = c"])
		city_dico[code]["r2.1_{}".format(year)] = float(line["emprunts bancaires et dettes assimilees"])
		city_dico[code]["r2.2_{}".format(year)] = float(line["subventions recues"])

readfile.close()

city_list = []
for code in city_dico.keys():
	temp = {"code":code}
	for key in city_dico[code].keys():
		temp[key] = city_dico[code][key]
	city_list.append(temp)

with open('static_dic/budgets_idf.json', 'w') as file:
    json.dump(city_list, file)
