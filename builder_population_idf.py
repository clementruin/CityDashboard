import json
import csv

readfile = open('static_raw/Pop1999-2015.csv', 'r', encoding = "ISO-8859-1")
reader = csv.DictReader(readfile, delimiter=';')
cities_pop = []
for line in reader:
	city = {
		"code" : line["insee"],
		"nom" : line['nom'],
		"Pop1999" : float(line["pop1999"]),
		"Pop2006" : float(line["pop2006"]),
		"Pop2007" : float(line["pop2007"]),
		"Pop2008" : float(line["pop2008"]),
		"Pop2009" : float(line["pop2009"]),
		"Pop2010" : float(line["pop2010"]),
		"Pop2011" : float(line["pop2011"]),
		"Pop2012" : float(line["pop2012"]),
		"Pop2013" : float(line["pop2013"]),
      	"Pop2014" : float(line["pop2014"]),
		"Pop2015" : float(line["pop2015"])
	}
	cities_pop.append(city)

readfile.close()

with open('static_dic/population.json', 'w') as file:
    json.dump(cities_pop, file)