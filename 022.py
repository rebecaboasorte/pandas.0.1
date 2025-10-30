'''
1. Importe a Vendas_Incorreto
2. Trate todos os dados incorretos
3. Analise estatisticamente o arquivo
'''

import pandas as pd

df = pd.read_excel('Vendas_Incorreto.xlsx')
print(df.info())
#
print(df.isnull().sum())
df_consolidado = df.dropna(how = 'all').dropna(how = 'all', axis = 1)
print(df_consolidado.info())
print(df.columns)