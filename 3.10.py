'''
3.10 – Todas as funções: Pensa em algo que você poderia armazenar em uma
lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países,
cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que crie
uma lista contendo esses itens e então utilize cada função apresentada neste
capítulo pelo menos uma vez.
'''
# uma vida
lista = ['cidade', 'pais', 'continente', 'planeta', 'sistema estelar', 'quadrante galático',
         'galaxia', 'sessão de galaxias', 'universo', 'multiverso']

# acrescentando elementos

lista.append('EU SOU')

print(lista)

del lista[0]

print(lista)

print(sorted(lista))

print(sorted(lista, reverse=True))

print(lista[9].upper())

print(len(lista))


