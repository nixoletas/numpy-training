import pandas as pd

dataset = pd.read_csv('db.csv', sep = ';')

def km_media(dataset, ano_atual):
    for item in dataset.items():
        result = item[1]['km'] / (ano_atual - item[1]['ano'])
        print(result)

km_media(dataset, 2016)