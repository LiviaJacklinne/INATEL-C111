import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pydataset as pds

df_space = pd.read_csv('space.csv',delimiter=';') 
df_paises = pd.read_csv('paises.csv',delimiter=';')


''' EXERCICIO 1 '''
# empresas_eua = df_space['Location'].str.contains('USA')
# x = len(np.unique(df_space['Company Name'][empresas_eua]))
# print(x)

# empresas_china = (df_space['Location'].str.contains('China'))
# y = len(np.unique(df_space['Company Name'][empresas_china]))
# print(y)
# plt.bar(['USA','China'],[x,y])
# plt.show()

''' EXERCICIO 2 '''
# america = df_paises['Region'].str.contains('NORTHERN AMERICA')
# # print(america.iloc[0:24])
# nomes_paises = df_paises['Country'][america]
# nascimento = df_paises['Birthrate'][america]
# morte = df_paises['Deathrate'][america]
# plt.plot(nomes_paises,nascimento, 'r--', nomes_paises, morte, 'b--')
# plt.show()

