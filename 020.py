'''
1.Escreva um programa que leia, nome, idade, sexo e país de orígem.
2. Organize cada leitura como uma lista, e insira em outra lista de armazenamento.
3. Após isso, crie um data frame usando pandas com suas respectivas colunas.

4. Calcule usando pandas.
	4.1 média de idade
	4.2 moda de idade
	4.3 mediana da idade
'''

import pandas as pd
nomes = []
idades = []
sexos = []
PI = []
while True:
    nome = input('Nome [fim para parar]: ')
    if nome == 'fim':
        break
    nomes.append(nome)
    idades.append(int(input('Idade: ')))
    sexos.append(input('Sexo [M/F]: ').strip().upper()[0])
    PI.append(input('Digite o País de Origiem: '))

d = {'Nomes': nomes, 'Idades': idades, 'Sexo': sexos, 'País de Origem': PI}

df = pd.DataFrame(data = d)

print(f'A média de idade é {df['Idades'].mean()}'
      f'\nA moda da idade é \n{df['Idades'].mode()}'
      f'\nA mediana de idade é {df['Idades'].median()}')













