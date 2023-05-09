import numpy as np

''' CARREGANDO UM DATASET '''
# nome do arquivo, o delimitador, carregando os arquivos como string (caso tenha dados de varios
# tipo, ele vem como string e n altera o valor), encoding = os caracteres que estão sendo usados 
ds = np.loadtxt('space.csv', delimiter=';',dtype=str,encoding='utf-8')

''' EXERCICIO 3 '''
# encontrando as empresas SpaceX
spaceX = np.char.startswith(ds[0:,1], 'SpaceX') > 0

# criando uma nova mtz só com a empresa SpaceX
nova_mtz = (ds[spaceX == True])

# np.where extrai o indice
# astype(float) ta convertendo a coluna 6 em float
# np.max está nos retornando o maior valor da coluna
# estamos bucando a partir da linha 0; e somente na coluna 6

indice = np.where(nova_mtz[0:,6].astype(float) == np.max(nova_mtz[0:,6].astype(float)))
print(f'Missão mais cara: {nova_mtz[indice]}')



    