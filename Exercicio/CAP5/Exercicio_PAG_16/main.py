import pandas as pd

# CRIANDO UM DATAFRAME 
df = pd.read_csv('paises.csv', delimiter=';')
# print(df)

''' Exercicio 1 '''
# slicing a partir da linha 0, pegando as colunas 0 e 1
region = df.iloc[0:,0:2]
paises = region[region['Region'].str.contains('OCEANIA')]
print(f'Paises da Oceania {paises}')

# Fazendo a contagem dos paises
print(f'Total de paises {paises.count()}')

# ''' Exercicio 2 '''
alfabetizados = df.iloc[0:,9].mean()
print(f'Média de alfabetização {round(alfabetizados,2)}%')

''' Exercicio 3 '''
# Comparação da coluna população do array, com o proprio array
# delimitando tambem a coluna populacao, mas usando a função max, para pegar o maior valor
populacao = df[df['Population'] == df['Population'].max()]
# print(populacao)
print(f'Nome e região do pais mais populoso {populacao.iloc[0:, 0:2]}') # PErguntar pro Renzo sobre slicing

''' Exercicio 4 '''
# Fazendo a verificação se tem costa
# 0 = true / 1 = false
sem_costa = df[df['Coastline (coast/area ratio)'] == 0]
print(f'Paises sem costa maritimica {sem_costa}')

# Salvando o arquivo
sem_costa.to_csv('PaisesSemCosta', sep=';', header=False)
