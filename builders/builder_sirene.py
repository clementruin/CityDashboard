import csv
import json
import csv


economy = []
readfile = open('static_raw/sirene_01_01_18.csv', 'r')
reader = csv.DictReader(readfile, delimiter=';')

#readfile2 = open('static_raw/correspondances-code-insee-code-postal.csv', 'r')
#reader2 = csv.DictReader(readfile2, delimiter=';')

 
def extractioncsv(fichiercsv):
    liste = []
    with open(fichiercsv, 'r') as fcsv:
        lecteur = csv.reader(fcsv, delimiter=';')
        for ligne in lecteur:
            liste.append(ligne)
    return liste


def from_postal_to_csv(postal_code):
    
    liste = extractioncsv("static_raw/insee_postal.csv") #recuperer le csv insee postal sous forme de liste python
    
    insee_code = 0
    
    for i in range(len(liste)-1):
        if liste[i][2]==postal_code:
            insee_code=liste[i][0]
    
    return insee_code

compteur=0

for line in reader:
    siren = line["SIREN"]
    
#    # to extract postal code only :
#    code = int(re.search(r"(\d{5})", L6_NORMALISEE).group(1)) #L6_DECLAREE ? cf sirene.fr
    
    postal_code = str(line["CODPOS"]) # warning : will differ from insee code
    
    dept = line["DEPET"]
    
#    business_area = line["LIBAPET"]
    employees = line["LIBTEFET"]
    employees = str(str(employees).replace('Unités non employeuses','Not applicable'))
    
    #remise en forme de la chaine de carac
    employees = str(str(employees).replace('salariés',''))
    employees = str(str(employees).replace(' salari\u00e9',''))
    employees = str(str(employees).replace(' ou ','/'))


    if ' à ' in employees:
        employees = employees.replace(' à ','/')
    
    employees = employees.strip()
    
    company_type=str(line['CATEGORIE'])
    
    if dept=='93':
        
        insee_code=from_postal_to_csv(postal_code)
        
#       economy.append({"Siren":siren, "Code":code, "Dept": dept, "Business_area":business_area, "Company_type":company_type})
        economy.append({"Insee": insee_code,"Company_type":company_type, "Employee_nb":employees})
        compteur += 1
        print(compteur)

        
with open('static_dic/sirene93f_01_01_18.json', 'w') as file:
    json.dump(economy, file)
    
# encoding='utf8' ?
