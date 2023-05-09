import numpy as np

''' CARREGANDO UM DATASET '''
# nome do arquivo, o delimitador, carregando os arquivos como string (caso tenha dados de varios
# tipo, ele vem como string e n altera o valor), encoding = os caracteres que estão sendo usados 
ds = np.loadtxt('space.csv', delimiter=';',dtype=str,encoding='utf-8')

''' EXERCICIO 3 '''
# Procurando quais missões foram realizadas pelo USA
USA = np.char.find(ds[1:,2], 'USA') > 0

# somando as missões (somando os itens TRUE do vetor)
print(USA[USA == True].sum())
