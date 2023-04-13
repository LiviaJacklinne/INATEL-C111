# IMPORTANDO A BIBLIOTECA NUMPY
import numpy as np

''' EXERCICIO 1 '''
# vect1 = np.linspace(0,1,21)
# print(vect1)

''' EXERCICIO 2 '''
# vect1_par = np.arange(0,51,2)
# print("Array de 0 - 51", vect1_par, "\n")

# vect2_par = np.arange(100,50,-2)
# print("Array de 100 - 50", vect2_par, "\n")

# vect_concat = np.concatenate((vect1_par,vect2_par))
# print("Arrays concatenados", vect_concat, "\n")

# vect_ordened = np.sort(vect_concat)
# print("Arrays ordenados", vect_ordened, "\n")

''' EXERCICIO 3 '''
# vect_decrescente = np.flip(vect_ordened)
# print("Array decrescente", vect_decrescente)

''' EXERCICIO 4 '''
# mtz_ones = np.ones([3,4])
# print("Matriz", mtz_ones)
# vect_ones = mtz_ones.reshape(12)
# print("Array", vect_ones)

''' EXERCICIO 5 '''
mtz = np.arange(1,16,1).reshape(3,5)
print(mtz)
linha, coluna = np.shape(mtz)

tamanho = linha * coluna
if tamanho % 2 == 0:
    print("Número par de elementos", tamanho)
else:
    print('Numero impar de elementos', tamanho)
