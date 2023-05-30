import pandas as pd

dataset = pd.read_csv('db.csv', sep = ';', index_col = 0)
print(dataset[['Valor']].head())
print(type(dataset[['Valor']].head()))
print(dataset.loc[['Jetta', 'DS5'],['Motor', 'Valor']])

for index, row in dataset.iterrows():
  if(2019 - row['Ano'] != 0):
    dataset.loc[index, 'Km_media'] = row['Quilometragem'] / (2019 - row['Ano'])
  else:
    dataset.loc[index, 'Km_media'] = 0

print(dataset)