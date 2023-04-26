# IMPORTANDO NUMPY ARRAY
import numpy as np
import random

''' CRIANDO UM NUMPY ARRAY 1 DIMENSSÃO (VETOR) '''
# vect = np.array([1, 2, 3])

''' CRIANDO UM NUMPY ARRAY 2 DIMENSSÕES (MATRIZ) '''
mtz = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])

# # SLICING 
# print(mtz[:2,2:])

''' ESTRUTURANDO NUMPY ARRAYS COM FUNÇÕES DO NUMPY '''
# # Função zero
# vect_zero = np.zeros(10)
# print(vect_zero)

# # Função ones
# mtz_one = np.ones([3,3])
# print(mtz_one)

# # Função arange (inicio, ultimo elemento exclusive, contando de)
# # Podemos criar um reshape (remodelar)
# # O vetor passa a ser uma matriz 3x4
# mtz_sequencia = np.arange(1,13,1).reshape(3,4)
# print(mtz_sequencia)

# # Função linspace (inicio, fim, qtd elementos)
# # Essa função pega os elementos com intervalo uniforme
# vect = np.linspace(0,100,11)
# print(vect)

''' CONCATENAÇÃO DE NYMPY ARRAY '''
# vect_concat1 = np.array([1,2,3,4])
# vect_concat2 = np.array([5,6,7,8])
# print(vect_concat1,vect_concat2)

'''---------------------------------------------------------------------'''
''' AULA PARTE 2'''

# Gerar numeros aleatórios "iguais" (plantar uma semente - seed)
np.random.seed(5)

# inicio, fim, quantidade de numeros
vect = np.random.randint(1,10,10)
print(vect)
print(np.unique(vect, return_counts= True))

# # soma de todas as colunas
# print(mtz.sum(axis=0))
# # soma de todas as linhas
# # se colocarmos um indice retorna a soma somente daquela coluna
# print(mtz.sum(axis=1)[0])


# ''' Operação de broadcast, é fazer a operação de um array por escalar   '''
# print(mtz/10)

