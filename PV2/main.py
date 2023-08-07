import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('pokemon.csv', delimiter=',')
ds = np.loadtxt('pokemon.csv', delimiter=',',dtype=str)

''' QUESTÃO 1 '''
print('------- QUESTÃO 1 -------')
# maior_ataque = df.nlargest(10,'Attack')
# print(maior_ataque.loc[[163,232,424,426,429,494,711,387,454,527],['Name','Attack']])

''' QUESTÃO 3 '''
print('------- QUESTÃO 3 -------')
lendario = df [df['Legendary'] == 1]
# lendario_mais_forte = lendario[lendario['Attack'] == lendario['Attack'].max()]
# print(lendario_mais_forte.loc[[163],['Name','Defense','Generation']])

''' QUESTÃO 4 '''
print('------- QUESTÃO 4 -------')
tipos = (lendario.iloc[0:,2:3])
tipo,repeticao = np.unique(tipos, return_counts=True)
menor_repeticao = repeticao.min()
indice = np.where(repeticao == menor_repeticao)
print(f'Menos popular {tipo[indice]}')

''' QUESTÃO 2 '''
# print('------- QUESTÃO 2 -------')
# print(f'total de tipos {tipo.sum()}')
# plt.bar([tipo],[repeticao])

# plt.bar(['Dark', 'Dragon', 'Electric', 'Fairy', 'Fire', 'Flying', 'Ghost',
#        'Grass', 'Ground', 'Ice', 'Normal', 'Psychic', 'Rock', 'Steel',
#        'Water'], dtype=object), array([ 2, 12,  4,  1,  5,  2,  2,  3,  4,  2,  2, 14,  4,  4,  4]])
# plt.bar(['Dark',2])
# plt.show()
