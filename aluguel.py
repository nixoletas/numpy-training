import pandas as pd

def p(thing):
  print(thing)

dados = pd.read_csv("aluguel.csv", sep = ';')

tipos_de_imovel = dados['Tipo']
tipos_de_imovel.drop_duplicates(inplace = True)
tipos_de_imovel = pd.DataFrame(tipos_de_imovel)

tipos_de_imovel.index = range(tipos_de_imovel.shape[0])
tipos_de_imovel.columns.name = 'Id'
p(tipos_de_imovel)