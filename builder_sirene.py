import csv
import re
import json

economy = []
readfile = open('static_raw/sirene_01_01_18.csv', 'r')
reader = csv.DictReader(readfile, delimiter=';')
for line in reader:
    siren = line["SIREN"]
    
#    # to extract postal code only :
#    code = int(re.search(r"(\d{5})", L6_NORMALISEE).group(1)) #L6_DECLAREE ? cf sirene.fr
    
    postal_code = line["CODPOS"] # warning : will differ from insee code
    dept = line["DEPET"]
    
    business_area = line["LIBAPET"]
    employees = line["LIBTEFET"]
    employees = str(str(employees).replace('Unités non employeuses','Not applicable'))
    
    company_type=line['CATEGORIE']
    
    if dept==77 or dept==78 or dept==91 or dept==92 or dept==92 or dept==75:
        economy.append({"SIREN":siren, "CODPOS": postal_code, "LIBAPET":business_area, "CATEGORIE":company_type})


with open('static_dic/sirene_01_01_18.json', 'w') as file:
    json.dump(economy, file)
