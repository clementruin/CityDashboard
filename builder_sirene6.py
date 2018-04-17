from itertools import groupby
import json
import re
import copy
import numpy as np

with open('static_dic/sirene94f_01_01_18.json') as f:
        
    contents = json.load(f)
    
    # XXX: make sure to sort the content list
    # with the key you want to group by
    contents.sort(key=lambda content: content['Insee'])
    
    # then use groupby with the same key
    groups = groupby(contents, lambda content: content['Insee'])
    
#    for adult, group in groups:
#        print ('Insee')
#        for content in group:
#            print ('\t', content)
#            
with open('static_dic/sirene94f2_01_01_18.json', 'w') as file:
    json.dump(contents, file)

    print('oklm')    
    
    final=[] 

#    current_insee=int(re.search(r"(\d{5})", contents[0]['Insee']).group(1))
    current_insee=np.zeros(int(len(contents)))

    m=0 #nouvel indice supprimant les redondances des codes insee pour i
    
    final=[{ "Firms_Nb" : 0, 'Employee_0_rate' : 0, "PME_rate": 0, "ETI_rate": 0,"GE_rate": 0,"Employee_1_2_rate": 0,"Employee_3_5_rate": 0,"Employee_6_9_rate": 0,"Employee_10_19_rate": 0,"Employee_20_49_rate": 0,"Employee_50_99_rate": 0,"Employee_100_199_rate": 0,"Employee_200_249_rate": 0,"Employee_250_499_rate": 0,"Employee_500_999_rate": 0,"Employee_1000_1999_rate": 0,"Employee_2000_4999_rate": 0,"Employee_5000_9999_rate": 0,"Employee_over_10000_rate": 0} for i in range(int(len(contents)))]

    for i in range(int(len(contents))): #indice m
        current_insee[i]=int(re.search(r"(\d{5})", contents[i]['Insee']).group(1))
#        final.append(features)
        final[m]['Insee']= int(current_insee[i]) # remplacer le i dans final par m à terme

               
        if i<int(len(contents))-1: #cas i+1 dans le second if qui provoque un out of range
            if int(re.search(r"(\d{5})", contents[i+1]['Insee']).group(1)) == int(re.search(r"(\d{5})", contents[i]['Insee']).group(1)):
#                print(int(re.search(r"(\d{5})", contents[i]['Insee']).group(1)),int(re.search(r"(\d{5})", contents[i-1]['Insee']).group(1)),m)
                final[m]['Firms_Nb'] += 1
                if contents[i]['Firm_size'] == '0':
#                    print(contents[i]['Firm_size'])
                    final[m]['Employee_0_rate'] += 1
#                    print(m, i, final[0]['Employee_0_rate'])
                if contents[i]['Firm_size'] == '1/2':
                    final[m]["Employee_1_2_rate"] += 1       
                if contents[i]['Firm_size'] == '3/5':
                    final[m]["Employee_3_5_rate"] += 1
                if contents[i]['Firm_size'] == '6/9':
                    final[m]["Employee_6_9_rate"] += 1
                if contents[i]['Firm_size'] == '10/19':
                    final[m]["Employee_10_19_rate"] += 1
                if contents[i]['Firm_size'] == '20/49':
                    final[m]["Employee_20_49_rate"] += 1
                if contents[i]['Firm_size'] == '50/99':
                    final[m]["Employee_50_99_rate"] += 1
                if contents[i]['Firm_size'] == '100/199':
                    final[m]["Employee_100_199_rate"] += 1
                if contents[i]['Firm_size'] == '200/249':
                    final[m]["Employee_200_249_rate"] += 1
                if contents[i]['Firm_size'] == '250/499':
                    final[m]["Employee_250_499_rate"] += 1
                if contents[i]['Firm_size'] == '500/999':
                    final[m]["Employee_500_999_rate"] += 1  
                if contents[i]['Firm_size'] == '1000/1999':
                    final[m]["Employee_1000_1999_rate"] += 1
                if contents[i]['Firm_size'] == '2000/4999':
                    final[m]["Employee_2000_4999_rate"] += 1
                if contents[i]['Firm_size'] == '5000/9999':
                    final[m]["Employee_5000_9999_rate"] += 1                
                if contents[i]['Firm_size'] == '10000':
                    final[m]["Employee_over_10000_rate"] += 1
                if contents[i]['Firm_type'] == "PME":
                    final[m]["PME_rate"] += 1
                if contents[i]['Firm_type'] == 'ETI':
                    final[m]["ETI_rate"] += 1
                if contents[i]['Firm_type'] == 'GE':
                    final[m]["GE_rate"] += 1
    
    #######################################################
            else:
                if contents[i]['Firm_size'] == '0':
#                    print(contents[i]['Firm_size'])
                    final[m]['Employee_0_rate'] += 1
#                    print(m, i, final[0]['Employee_0_rate'])
                if contents[i]['Firm_size'] == '1/2':
                    final[m]["Employee_1_2_rate"] += 1       
                if contents[i]['Firm_size'] == '3/5':
                    final[m]["Employee_3_5_rate"] += 1
                if contents[i]['Firm_size'] == '6/9':
                    final[m]["Employee_6_9_rate"] += 1
                if contents[i]['Firm_size'] == '10/19':
                    final[m]["Employee_10_19_rate"] += 1
                if contents[i]['Firm_size'] == '20/49':
                    final[m]["Employee_20_49_rate"] += 1
                if contents[i]['Firm_size'] == '50/99':
                    final[m]["Employee_50_99_rate"] += 1
                if contents[i]['Firm_size'] == '100/199':
                    final[m]["Employee_100_199_rate"] += 1
                if contents[i]['Firm_size'] == '200/249':
                    final[m]["Employee_200_249_rate"] += 1
                if contents[i]['Firm_size'] == '250/499':
                    final[m]["Employee_250_499_rate"] += 1
                if contents[i]['Firm_size'] == '500/999':
                    final[m]["Employee_500_999_rate"] += 1  
                if contents[i]['Firm_size'] == '1000/1999':
                    final[m]["Employee_1000_1999_rate"] += 1
                if contents[i]['Firm_size'] == '2000/4999':
                    final[m]["Employee_2000_4999_rate"] += 1
                if contents[i]['Firm_size'] == '5000/9999':
                    final[m]["Employee_5000_9999_rate"] += 1                
                if contents[i]['Firm_size'] == '10000':
                    final[m]["Employee_over_10000_rate"] += 1
                if contents[i]['Firm_type'] == "PME":
                    final[m]["PME_rate"] += 1
                if contents[i]['Firm_type'] == 'ETI':
                    final[m]["ETI_rate"] += 1
                if contents[i]['Firm_type'] == 'GE':
                    final[m]["GE_rate"] += 1
                m += 1
#        if i==int(len(contents)):
#            if if int(re.search(r"(\d{5})", contents[i-1]['Insee']).group(1)) == int(re.search(r"(\d{5})", contents[i]['Insee']).group(1)):
            
final2 = final[0:(m+1)] #suppression itérations superflues à 0


with open('static_dic/sirene94f3_01_01_18.json', 'w') as file:
    json.dump(final2, file)