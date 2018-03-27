import matplotlib.pyplot as plt
import json
import pandas as pd
from pandas.io.json import json_normalize

# open 1st dataframe
with open('static/logement.json') as file:
    data = json.load(file)

df1 = pd.DataFrame.from_dict(json_normalize(data), orient='columns')
df1.set_index('inseecode', inplace=True)

# open second dataframe
with open('static_dic/partisidf.json') as file:
    data = json.load(file)

df2 = pd.DataFrame.from_dict(json_normalize(data), orient='columns')
df2.set_index('code', inplace=True)

# concatenate dataframes 
df = pd.concat([df1, df2], axis=1, join='inner')

# select useful columns 
df = df[['portion_hlm_tenant','housing','partis.2014']]

# correlation
print(df['portion_hlm_tenant'].corr(df['housing']))
print(df1.corr())