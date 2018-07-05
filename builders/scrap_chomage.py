# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool

with open('unemployment91.csv','w') as file:
    
    file.write('City;Unemployment rate\n')
        
    def get(i):
        if i<10:
                req=requests.get("https://www.insee.fr/fr/statistiques/1405599?geo=COM-9100"+str(i))
        elif 10<=i<100:
            req=requests.get("https://www.insee.fr/fr/statistiques/1405599?geo=COM-910"+str(i))
        elif i>=100:
            req=requests.get("https://www.insee.fr/fr/statistiques/1405599?geo=COM-91"+str(i))
        soup=BeautifulSoup(req.text)
        if len(soup.select('#produit-tableau-POP_T1M-4 > tbody > tr:nth-of-type(1) > th:nth-of-type(2)'))>0 :
            name=soup.select('#produit-tableau-POP_T1M-4 > tbody > tr:nth-of-type(1) > th:nth-of-type(2)')[0].text
            rate=soup.select('#produit-tableau-POP_T1M-4 > tbody > tr:nth-of-type(6) > td')[0].text
            return name,rate

    p=Pool(4)
    liste=p.map(get,range(1000))
    
    for ville in liste:
        if ville is not None:
            name, rate = ville
            file.write('{};{}\n'.format(name,rate))
            