'''
6.9 – Lugares favoritos: Crie um dicionário chamado favorite_places. Pense em
três nomes para usar como chaves do dicionário e armazene de um a três lugares
favoritos para cada pessoa. Para deixar este exercício um pouco mais interessante,
peça a alguns amigos que nomeiem alguns de seus lugares favoritos. Percorra o
dicionário com um laço e apresente o nome de cada pessoa e seus lugares
favoritos.
'''

favorite_places = {
        'carol': ['home', 'beach', 'montain'],
        'fabi': ['home', 'ubatuba', 'tiradentes'],
        'sueli': ['home', 'travelling', 'italy'],
    }


for people, places in favorite_places.items():
    print("\nName: " + people.title())
    for favorite in places:
        print('\tPlaces: ' + favorite)


