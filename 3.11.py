'''
3.11 – Erro proposital: Se você ainda não recebeu um erro de índice em um de
seus programas, tente fazer um erro desse tipo acontecer. Altere um índice em um
de seus programas de modo a gerar um erro de índice. Não se esqueça de corrigir
o erro antes de fechar o programa.

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

# Erro proposital
#print(lista[-11])
