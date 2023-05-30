import pandas as pd

data = pd.read_csv('aluguel.csv', sep = ";")
print(data.head(10))

print(list(data['Tipo'].drop_duplicates()))

residencial = ['Quitinete', 'Casa', 'Apartamento', 'Casa de Condomínio', 'Flat']