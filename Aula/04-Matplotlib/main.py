# IMPORTANDO BIBLIOTECAs
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# TRAÇANDO UM GRÁFICO
x = np.array([1,2,3,4])
y = x*2 # broadcasting

y2 = x*x # operação indice a indice (np array * np array)

plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

# s = coloca marcadores quadrado / r = faz a linha do grafico ficar pontilhada
# linewidth = tamanho da linha / markersize = tamanho do marcador
# plt.plot(x,y, 's:r', linewidth=3, markersize=20)

# O = bolinha / G = green
# plt.plot(x, y2, 'o--g', linewidth=3, markersize=20)

''' 
    OBS: pode plotar dois graficos em uma linha
    plt.plot(x,y, 's:r', x, y2, 'o--g', linewidth=3, markersize=20)
'''
# linha, coluna, posição
plt.subplot(1,2,1)
plt.plot(x, y, 's:r')

plt.subplot(1,2,2)
plt.plot(x, y2, 'o--g')

plt.show()
