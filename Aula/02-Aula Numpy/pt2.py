import numpy as np

# np.random.seed(10)
# mtz = np.random.randint(1,10,16).reshape(4,4)
# print(mtz)

# # CONDICIONAIS DO NUMPY
# # Verificando se o numero é impar
# print(mtz%2 == 1) # Extraindo True e False
# print([mtz%2 == 1]) # Extraindo os numeros

# MANIPULANDO TEXTOS COM SUBPACOTE CHAR
# arr = np.array(['Matheus','Vini','Leticia','Raphael','Livia'])
# # A função retorna a posição de onde ele encontrou o texto 'ia', se ele não encontra
# # ele retorna um valor negativo, no caso quando usamos > 0, é uma condição
# print(np.char.find(arr, 'ia') > 0) # Retorna True ou False
# cond = np.char.find(arr, 'ia') > 0 # Retorna True ou False
# print(arr[cond])

''' CARREGANDO UM DATASET '''
# nome do arquivo, o delimitador, carregando os arquivos como string (caso tenha dados de varios
# tipo, ele vem como string e n altera o valor), encoding = os caracteres que estão sendo usados 
ds = np.loadtxt('space.csv', delimiter=';',dtype=str,encoding='utf-8')
# print(ds)

# VISUALIZANDO APENAS AS COLUNAS DO DATASET
# printa só a linha ZERO do dataset, pegando todas as colunas
print(ds[0, :])

# EXTRAINDO APENAS AS EMPRESAS QUE JA FIZERAM MISSÕES
# printa a partir da linha 1, pegando só a primeira coluna
# return counts, reotrna os nomes e a reptição deles (2 vetores)
print(np.unique(ds[1:,1], return_counts=True))

array, repeticoes = np.unique(ds[1:,1], return_counts=True)

maximo = repeticoes.max()

i=0
for cont in repeticoes:
    if cont == maximo:
        print(array[i])
    i+=1
    