import numpy as np

''' CARREGANDO UM DATASET '''
# nome do arquivo, o delimitador, carregando os arquivos como string (caso tenha dados de varios
# tipo, ele vem como string e n altera o valor), encoding = os caracteres que estão sendo usados 
ds = np.loadtxt('space.csv', delimiter=';',dtype=str,encoding='utf-8')

''' EXERCICIO 5 '''
empresas, repeticao = np.unique(ds[1:,1], return_counts=True)
print(empresas, repeticao)

i = 0
for cont in empresas:
    print(f'Empresa: {empresas[i]}, total de missão: {repeticao[i]}')
    i = i + 1
    