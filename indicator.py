# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 17:09:32 2018

@author: Hervé
"""

import json

def population92(code):
    reader_pop = open('static_dic/population92.json', 'r')
    file_pop = json.load(reader_pop)
    data = file_pop[code]
    print('Commune : ', code)
    print('Part de la population de moins de 25 ans : ', data['25'], '%')
    print('Part de la population de moins de 65 ans : ', data['25']+data['64'], '%')
    print('Part de la population de plus de 65 ans : ', data['65+'], '%')
    print('Evolution de la population entre 2009 et 2014 : ', data['evol'], '%')

def logement92(code):
    reader_log = open('static_dic/Logement92.json', 'r')
    file_log = json.load(reader_log)
    data = file_log[code]
    print('Commune : ', code)
    print('Nombre total de logements : ', int(data['housing']))
    print('Part de résidences principales : ', round(data['main_res']/data['housing'],2), '%')
    print('Part des locataires HLM : ', data['portion_hlm_tenant'], '%')
    print('Part des logements sociaux : ', round(data['social_housing']/data['housing'],2), '%')