'''
2. Encontre a Informação

'''

import pandas as pd

#1.Importe a Base Aula 002 - Exemplo.xlsx
df = pd.read_excel('Base Aula 002 - Exemplo .xlsx')
print(df.info())

#2.1 - Qual país vendeu mais(Total)?
print(df[['País', 'Total']].groupby('País').sum().sort_values(by = 'Total', ascending=False))

#2.2 - Qual o melhor vendedor?
print(df[['Vendedor', 'Total', 'Quantidade']].groupby('Vendedor').agg(['mean', 'sum']))

#2.3 - Qual o melhor tipo de loja?
print(df[['Loja', 'Total', 'Quantidade']].groupby('Loja').agg(['mean', 'sum']))

#2.4 - Qual é o tipo de envio mais usado?
print(df['Tipo de Envio'].value_counts())
df_colidado = (df[['Tipo de Envio', 'Quantidade', 'Peso']].groupby('Tipo de Envio').agg(['mean', 'sum'])
               .sort_values(('Quantidade', 'sum'), ascending=False))

print(df_colidado)

#2.5 - Qual o público que mais atendemos (Gênero)?
print(df['Gênero'].value_counts())
df_colidado = (df[['Gênero', 'Quantidade', 'Peso']].groupby('Gênero').agg(['mean', 'sum'])
               .sort_values(('Quantidade', 'sum'), ascending=False))

print(df_colidado)

#2.6 - Quem fez as 3 maiores vendas?
print(df[['Vendedor', 'Total']].sort_values(by = 'Total', ascending=False).head(10))

#2.7 - Adicione uma nova coluna comissão (Total * 5%)
df['Comissão'] = df['Total'] * 0.05







