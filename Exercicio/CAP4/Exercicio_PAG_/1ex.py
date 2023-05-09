import numpy as np

''' CARREGANDO UM DATASET '''
# nome do arquivo, o delimitador, carregando os arquivos como string (caso tenha dados de varios
# tipo, ele vem como string e n altera o valor), encoding = os caracteres que estão sendo usados 
ds = np.loadtxt('space.csv', delimiter=';',dtype=str,encoding='utf-8')

''' EXERCICIO 1 '''
# Encontra uma palavra com texto igual
sucesso = np.char.startswith(ds[1:,7], 'Success') > 0
# print(sucesso)

# soma todos os itens que deram TRUE
soma = (sucesso[sucesso == True].sum())

# Acha o total de linha da coluna 7 (tirando a primeira linha de info)
total = ds[1:,7].size

print(f'percentual de sucesso: {round((soma*100)/total, 3)}')

