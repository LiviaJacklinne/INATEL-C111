# importando numpy
import numpy as np

# carregando o dataset
ds = np.loadtxt('artists_v2.csv', delimiter=',', dtype=str, encoding='utf-8')

''' QUESTÃO 1 '''
# usa = np.char.startswith(ds[1:,1], 'United States')>0
# soma = usa[usa == True].sum()
# total = ds[1:,1].size
# print(f'Porcentagem de cantores americanos {round((soma*100)/total,3)}%')

''' QUESTÃO 2 '''
# ativo = np.char.find(ds[1:,2], 'present') > 0
# total_ativo = ativo[ativo == True].sum()
# print(f'Artistas aposentados {ds[1:,2].size - total_ativo}')

''' QUESTÃO 3 '''
# old = ds[1:,3].astype(int).argmin()
# print(f'Disco mais antigo {ds[old+1]}') # +1 pq a primeira linha foi cortada no slicing


''' QUESTÃO 4 '''
artistas = ds[1:11]
print(f'Artistas mais vendidos: {artistas[0:,0]}')