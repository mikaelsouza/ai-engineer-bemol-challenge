import pandas as pd
import pickle
from pathlib import Path
from os.path import join
'''
Script para remover informações da base de dados utilizada para simular
dados confidenciais.
'''

dir_path = Path('../../data/')
path_to_data = join(dir_path, 'processed/labeled_rfm.csv')
path_to_save = join(dir_path, 'processed/confidential_rfm.csv')

client_labels = {0: 'Comum', 1: 'Recorrente', 2: 'Premium', 3: 'Ex-Cliente'}

data = pd.read_csv(path_to_data).dropna()
countries = sorted(data['Country'].unique().astype(str))

country_ids = {country: idx for idx, country in enumerate(countries)}

data['Country'] = data['Country'].apply(lambda x: country_ids[x])
data = data.drop(['Recency', 'Frequency', 'Amount'], axis=1)
data.to_csv(path_to_save, index=False)

f1_path = join(dir_path, 'bin/CLIENTLABELS.BIN')
f2_path = join(dir_path, 'bin/COUNTRYIDS.BIN')

with open(f1_path, 'wb') as f1, open(f2_path, 'wb') as f2:
    pickle.dump(client_labels, f1)
    pickle.dump(country_ids, f2)