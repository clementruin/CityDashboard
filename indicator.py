# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 17:09:32 2018

@author: Hervé
"""

import json
import numpy as np
import matplotlib.pyplot as plt


def population92(code):
    reader_pop = open('static_dic/population92.json', 'r')
    file_pop = json.load(reader_pop)
    data = file_pop[code]
    #print('Commune : ', code)
    #print('Part de la population de moins de 25 ans : ', data['25'], '%')
    #print('Part de la population de moins de 65 ans : ', data['25']+data['64'], '%')
    #print('Part de la population de plus de 65 ans : ', data['65+'], '%')
    #print('Evolution de la population entre 2009 et 2014 : ', data['evol'], '%')
    #printpop(code)
    indics = [ 
        'Part de la population de moins de 25 ans', 
        'Part de la population de moins de 65 ans',
        'Part de la population de plus de 65 ans',
        'Evolution de la population entre 2009 et 2014'
        ]
    values = [
        data['25'],
        data['25']+data['64'],
        data['65+'],
        data['evol']
        ]
    return [indics, values]

def logement92(code):
    reader_log = open('static_dic/Logement92.json', 'r')
    file_log = json.load(reader_log)
    data = file_log[code]
    #print('Commune : ', code)
    #print('Nombre total de logements : ', int(data['housing']))
    #print('Part de résidences principales : ', round(data['main_res']/data['housing'],2), '%')
    #print('Part des locataires HLM : ', data['portion_hlm_tenant'], '%')
    #print('Part des logements sociaux : ', round(data['social_housing']/data['housing'],2), '%')
    indics = [
        'Nombre total de logements',
        'Part de résidences principales',
        'Part des locataires HLM',
        'Part des logements sociaux'
        ]
    values = [
        int(data['housing']),
        round(data['main_res']/data['housing'],2),
        data['portion_hlm_tenant'],
        round(data['social_housing']/data['housing'],2)
        ]
    return [indics, values]
    
def printpop(code):
    
    reader_pop = open('static_dic/population92.json', 'r')
    file_pop = json.load(reader_pop)
    data = file_pop[code]

    ages = ['-25', '25-64', '65+']
    data = [data['25'], data['64'], data['65+']]
    
    explode=np.zeros(len(data))

    for i in range(len(data)):
        if i == data.index(max(data)):
            explode[i]=0.15

    plt.pie(data, explode=explode, labels=ages, autopct='%1.1f%%', startangle=90, shadow=True)
    plt.axis('equal')
    plt.show()
    

def main(code):
    T1 = population92(code)
    T2 = logement92(code)
    return [T1[0]+T2[0],T1[1]+T2[1]]
