import pandas as pd

# CRIANDO UM DATAFRAME 
df = pd.read_csv('paises.csv', delimiter=';')
# print(df)

''' EXIBINDO COLUNAS '''
# print(df.columns)

''' EXIBINDO AS 3 PRIMEIRAS LINHAS'''
# print(df.head(3))

''' EXIBINDO AS 4 ULTIMAS LINHAS '''
# print(df.tail(4))

''' EXIBINDO COLUNAS '''
print(df[['Country', 'Birthrate', 'Deathrate']])