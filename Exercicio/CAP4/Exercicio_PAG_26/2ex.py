import numpy as np

''' CARREGANDO UM DATASET '''
# nome do arquivo, o delimitador, carregando os arquivos como string (caso tenha dados de varios
# tipo, ele vem como string e n altera o valor), encoding = os caracteres que estão sendo usados 
ds = np.loadtxt('space.csv', delimiter=';',dtype=str,encoding='utf-8')

''' EXERCICIO 2 '''
values = ds[1:,6].astype(float)
print(values)
print(values[values != 0].mean())
