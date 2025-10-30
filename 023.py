'''
Crie um programa que
Importe a biblioteca pandas como pd
Leia um DataFrame “Salarios.csv” e nomei-o de df
Retorne o head do DataFrame
Use o método .info(), para descobrir quantas entradas ele tem
Qual é a média de Pagamento Base?
Qual é o maior montante pago em OvertimePay?
Qual é a profissão do ‘JOSEPH DRISCOLL’
Qual o nome da pessoa mais bem paga
Qual é a media de pagamento base por ano?
Quantas profissoes únicas existem?
'''

import pandas as pd

df = pd.read_csv('Salaries.csv')
print(df.head())
print(df.info())

print(f'A média de pagamento base é {df['BasePay'].mean()}')
print(f'O maior montante pago é {df['OvertimePay'].max()}')
print(f'A profissão do Joseph é {df['JobTitle'][df['EmployeeName'] == 'JOSEPH DRISCOLL']}')
print(f'O nome da pessoa mais bem paga é {df['EmployeeName'][df['TotalPay'] == df['TotalPay'].max()]}')
print(df[['Year', 'TotalPay']].groupby('Year').mean().sort_values(by = 'TotalPay', ascending=False))
print(f'A quantidade de profissões únicas é {df['JobTitle'].nunique()}')





