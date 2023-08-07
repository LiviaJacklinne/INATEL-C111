import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# importando o dataset
ds = pd.read_csv('paises.csv', delimiter=';')

# EXTRAINDO OS MAIORES PAISES
# print(ds.columns) # exibindo as colunas

# faz um slicing retornando somente os 6 maiores paises
maioresPaises = ds.nlargest(6,'Area (sq. mi.)')
print(maioresPaises)

# faz um slicing retornando somente os 6 menores paises
menoresPaises = ds.nsmallest(6,'Area (sq. mi.)')
print(menoresPaises)

plt.scatter(maioresPaises['Country'], maioresPaises['GDP ($ per capita)'], 
            maioresPaises['Area (sq. mi.)']/5000) # dividido por 5k pra diminuir o tam da bolinha
#3B78FF
#16C60C
plt.show()

