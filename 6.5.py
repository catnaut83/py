'''
6.5 – Rios: Crie um dicionário que contenha três rios importantes e o país que
cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.
• Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre
pelo Egito.
• Use um laço para exibir o nome de cada rio incluído no dicionário.
• Use um laço para exibir o nome de cada país incluído no dicionário.
'''

rios = {
    'nilo': 'egito',
    'amazonas': 'brasil',
    'yangtze': 'china',
        }

for rio, pais in rios.items():
    print("O colossal rio " + rio.title() + " corre pelo " + pais.title())

print('\nOs rios mencionandos são:')
for rio in rios.keys():
    print(rio.title())

print('\nOs países mencionandos são:')
for pais in rios.values():
    print(pais.title())