import csv
import re
import json

unemployment = []
readfile = open('static_raw/chomage.csv', 'r')
reader = csv.DictReader(readfile, delimiter=';')
for line in reader:
    code = line["code"]
    # to extract insee code only :
    code = int(re.search(r"(\d{5})", code).group(1))
    rate = line['unemployment rate']
    # to convert decimal mark :
    rate = float(str(rate).replace(',', '.'))
    unemployment.append({"code":code, "chomage":rate})


with open('static_dic/chomage.json', 'w') as file:
    json.dump(unemployment, file)
