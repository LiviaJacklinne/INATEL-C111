import numpy as np
import random

''' QUESTÃO 1 '''
# Semente
# np.random.seed(5)
# vect = (np.random.randn(10))*100
# vect_inteiro = vect.astype(int)
# print(vect)
# print(vect_inteiro)

''' QUESTÃO 2 '''
np.random.seed(10)
mtz = np.random.randint(1,51,16).reshape(4,4)
print('Matriz\n', mtz)
print("-------------------")

''' QUESTÃO 3 '''
media_coluna = (mtz.mean(axis=0))
media_linha = (mtz.mean(axis=1))



print(f'Media das colunas {media_coluna}')
print(f'Maior média {media_coluna.max()}')
print("-------------------")

print(f'Media das linhas {media_linha}')
print(f'Maior média {media_coluna.max()}')

''' QUESTÃO 4 '''
# A função unique, retorna o array ordenado e a reptição dos numeros
vect_ordenado, repeticoes = np.unique(mtz, return_counts=True)

print(vect_ordenado) # Array ordenado
print(repeticoes) # Itens que se repetem, indice relacionado ao Array

i=0 # Variavel contadora auxiliar para acessar o indice
for cont in repeticoes:
    # print(i)
    if cont == 2: # Estamos comparando a 2, pq são 2 valores que se repetem 2x
        # Se o valor for igual a 2, acessa o vetor na posição i
        # e pega o valor que ta lá
        print(vect_ordenado[i])
    i+=1