'''
6.10 – Números favoritos: Modifique o seu programa do Exercício 6.2 (página
147) para que cada pessoa possa ter mais de um número favorito. Em seguida,
apresente o nome de cada pessoa, juntamente com seus números favoritos.
'''

num = {
    'carol': [11, 33, 144],
    'fabi': [12, 18, 76],
    'sirius': [11, 24, 111],
    'thoth': [1, 0, 101],
    'orion': [22, 83, 999],
}

for name, number in num.items():
    print('\nFavorite numbers of ' + name.title() + ' are:')
    for fnum in number:
        print('\t'+ str(fnum)) 
