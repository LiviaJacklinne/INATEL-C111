import numpy as np
import pandas as pd

# SERIES -> usado para 1 dimensão
# DATAFRAME -> usado para +2 dimensões 

# CRIANDO UMA SERIES
# PANDAS TRABALHA COM INDICES CUSTOMIZAVEIS (vc informa o valor do indice)
series1 = pd.Series({'a':10,'b':20, 'c':30})
series2 = pd.Series({'a':10,'c':20, 'd':30})

'''
print(series1+series2)
print(series1.add(series2, fill_value=0))
print(type(series1))'''

# CONDICIONAL PANDAS
print(series1[series1>25])

# SLICING NA SERIES
# print(series1[['b','c']])
