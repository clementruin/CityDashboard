import json
import csv

readfile = open('static_raw/city_budgets_idf.csv', 'r')
reader = csv.DictReader(readfile, delimiter=',')
city_dico = {}
for line in reader:
	#if line["inseecode"][:2]=="92":
	if True :
		code = line["inseecode"]
		if code in city_dico:
			city_dico[code]["budget"][line["annee"]] = float(line["total des charges de fonctionnement = b"])+float(line["total des emplois d investissement = d"])+float(line["total des produits de fonctionnement = a"])+float(line["total des ressources d investissement = c"])
			city_dico[code]["depenses"][line["annee"]] = float(line["total des charges de fonctionnement = b"])+float(line["total des emplois d investissement = d"])
			city_dico[code]["d1"][line["annee"]] = float(line["total des charges de fonctionnement = b"])
			city_dico[code]["d1.1"][line["annee"]] = float(line["achats et charges externes"])
			city_dico[code]["d1.2"][line["annee"]] = float(line["charges de personnel"])
			city_dico[code]["d1.3"][line["annee"]] = float(line["charges financieres"])
			city_dico[code]["d1.4"][line["annee"]] = float(line["contingents"])
			city_dico[code]["d1.5"][line["annee"]] = float(line["subventions versees"])
			city_dico[code]["d2"][line["annee"]] = float(line["total des emplois d investissement = d"])
			city_dico[code]["d2.1"][line["annee"]] = float(line["charges a repartir"])
			city_dico[code]["d2.2"][line["annee"]] = float(line["depenses d’equipement"])
			city_dico[code]["d2.3"][line["annee"]] = float(line["remboursement d'emprunts et dettes assimilees"])
			city_dico[code]["recettes"][line["annee"]] = float(line["total des produits de fonctionnement = a"])+float(line["total des ressources d investissement = c"])
			city_dico[code]["r1"][line["annee"]] = float(line["total des produits de fonctionnement = a"])
			city_dico[code]["r1.1"][line["annee"]] = float(line["autres impots et taxes"])
			city_dico[code]["r1.2"][line["annee"]] = float(line["dotation globale de fonctionnement"])
			city_dico[code]["r1.3"][line["annee"]] = float(line["impots locaux"])
			city_dico[code]["r2"][line["annee"]] = float(line["total des ressources d investissement = c"])
			city_dico[code]["r2.1"][line["annee"]] = float(line["emprunts bancaires et dettes assimilees"])
			city_dico[code]["r2.2"][line["annee"]] = float(line["subventions recues"])
		else :
			label_dico = {
				"budget": {line["annee"] : float(line["total des charges de fonctionnement = b"])+float(line["total des emplois d investissement = d"])+float(line["total des produits de fonctionnement = a"])+float(line["total des ressources d investissement = c"])},
				"depenses": {line["annee"] : float(line["total des charges de fonctionnement = b"])+float(line["total des emplois d investissement = d"])},
				"d1": {line["annee"] : float(line["total des charges de fonctionnement = b"])},
				"d1.1": {line["annee"] : float(line["achats et charges externes"])},
				"d1.2": {line["annee"] : float(line["charges de personnel"])},
				"d1.3": {line["annee"] : float(line["charges financieres"])},
				"d1.4": {line["annee"] : float(line["contingents"])},
				"d1.5": {line["annee"] : float(line["subventions versees"])},
				"d2": {line["annee"] : float(line["total des emplois d investissement = d"])},
				"d2.1": {line["annee"] : float(line["charges a repartir"])},
				"d2.2": {line["annee"] : float(line["depenses d’equipement"])},
				"d2.3": {line["annee"] : float(line["remboursement d'emprunts et dettes assimilees"])},
				"recettes": {line["annee"] : float(line["total des produits de fonctionnement = a"])+float(line["total des ressources d investissement = c"])},
				"r1": {line["annee"] : float(line["total des produits de fonctionnement = a"])},
				"r1.1": {line["annee"] : float(line["autres impots et taxes"])},
				"r1.2": {line["annee"] : float(line["dotation globale de fonctionnement"])},
				"r1.3": {line["annee"] : float(line["impots locaux"])},
				"r2": {line["annee"] : float(line["total des ressources d investissement = c"])},
				"r2.1": {line["annee"] : float(line["emprunts bancaires et dettes assimilees"])},
				"r2.2": {line["annee"] : float(line["subventions recues"])} }
			city_dico[code]=label_dico

readfile.close()

with open('static_dic/my_dict.json', 'w') as file:
    json.dump(city_dico, file)

