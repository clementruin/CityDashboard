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
    "Demo_index" : float(line['Indice Demographique']),
    "household index" : float(line['Indice Menages']),
    "household_amnt" : float(line['Nb Menages']),
    "main residences" : float(line['Nb Residences Principales']),
    "second_residences" : float(line['Nb proprietaire']),
    "housing" : float(line['Nb Logement']),
    "empty_housing" : float(line['Nb Log Vacants']),
    "women" : float(line['Nb Femme']),
    "men" : float(line['Nb Homme']),
    "juniors" : float(line['Nb Mineurs']),
    "seniors" : float(line['Nb Majeurs']),
    "company_creation" : float(line['Nb Creation Enteprises']),
    "actives" : float(line['Nb Atifs']),
    "housing_rate": float(line['Nb Log Vacants'])/(float(line['Nb Log Vacants'])+float(line['Nb Logement']))*100,
    "parity": float(line['Nb Femme'])/(float(line['Nb Femme'])+float(line['Nb Homme']))*100,
    "property_rate": float(line['Nb proprietaire'])/(float(line['Nb Logement'])-float(line['Nb Log Vacants']))*100,
    "property_access" : float(line['Nb Log Vacants'])/float(line['Indice Menages'])*100,
    "occupation_rate" : (float(line['Nb Femme'])+float(line['Nb Homme']))/(float(line['Nb Logement'])-float(line['Nb Log Vacants'])),
    "Entrepreneurship_services" : float(line['Dynamique Entrepreneuriale Service et Commerce']),
    "trade_companies" : float(line['Nb Entreprises Secteur Commerce']),
    "industry_companies" : float(line['Nb Entreprises Secteur Industrie']),
    "services_companies" : float(line['Nb Entreprises Secteur Services']),
    "construction_companies" : float(line['Nb Entreprises Secteur Construction']),
    "company_creation" : float(line['Nb Creation Enteprises']),
    "company_creation_Industry" : float(line['Nb Creation Industrielles']),
    "company_creation_Construction" : float(line['Nb Creation Construction']),
    "company_creation_trade" : float(line['Nb Creation Commerces']),
    "company_creation_Services" : float(line['Nb Cr_ation Services']),
    "nb_companies" : float(line['Nb Entreprises Secteur Commerce'])+float(line['Nb Entreprises Secteur Industrie'])+float(line['Nb Entreprises Secteur Services'])+float(line['Nb Entreprises Secteur Construction']),
    "Industry_rate" : float(line['Nb Entreprises Secteur Industrie'])/(float(line['Nb Entreprises Secteur Commerce'])+float(line['Nb Entreprises Secteur Industrie'])+float(line['Nb Entreprises Secteur Services'])+float(line['Nb Entreprises Secteur Construction']))*100,
    "trade_rate" : float(line['Nb Entreprises Secteur Commerce'])/(float(line['Nb Entreprises Secteur Commerce'])+float(line['Nb Entreprises Secteur Industrie'])+float(line['Nb Entreprises Secteur Services'])+float(line['Nb Entreprises Secteur Construction']))*100,
    "services_rate" : float(line['Nb Entreprises Secteur Services'])/(float(line['Nb Entreprises Secteur Commerce'])+float(line['Nb Entreprises Secteur Industrie'])+float(line['Nb Entreprises Secteur Services'])+float(line['Nb Entreprises Secteur Construction']))*100,
    "construction_rate" : float(line['Nb Entreprises Secteur Construction'])/(float(line['Nb Entreprises Secteur Commerce'])+float(line['Nb Entreprises Secteur Industrie'])+float(line['Nb Entreprises Secteur Services'])+float(line['Nb Entreprises Secteur Construction']))*100,
    "Industry_creation_rate" : float(line['Nb Creation Industrielles'])/float(line['Nb Creation Enteprises'])*100,
    "trade_creation_rate" : float(line['Nb Creation Commerces'])/float(line['Nb Creation Enteprises'])*100,
    "construction_creation_rate" : float(line['Nb Creation Construction'])/float(line['Nb Creation Enteprises'])*100,
    "Services_creation_rate" : float(line['Nb Cr_ation Services'])/float(line['Nb Creation Enteprises'])*100,
        
	}
	city_dico[code] = dico

readfile.close()

with open('static_dic/newdata92.json', 'w') as file:
    json.dump(city_dico, file)
