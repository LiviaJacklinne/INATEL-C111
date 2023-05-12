import numpy as np

arr = np.loadtxt('space.csv', delimiter=';',dtype=str,encoding='utf-8')

# # EXERCICIO 1
# missao = arr[1:,7]
# missao_sucesso = len(missao[np.char.find(missao,'Success') == 0])
# print(missao_sucesso/len(missao)*100)

# # EXERCICIO 2
# gastos = arr[1:,6].astype(float)
# print(sum(gastos[gastos>0])/len(gastos[gastos>0]))

# EXERCICIO 3
# cidades = arr[1:,2]
# usa = np.char.find(cidades,'USA') > 0
# print(len(cidades[usa]))

# EXERCICIO 4
empresas,gastos = arr[1:,1],arr[1:,6].astype(float)
missao_cara = np.where(empresas == 'SpaceX')
print(max(gastos[missao_cara]))

# # EXERCICIO 5
# empresas, num_missoes = np.unique(arr[1:,1], return_counts= True)

# for i in range(len(empresas)):
#     print(empresas[i],num_missoes[i])
