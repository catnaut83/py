'''
6.11 – Cidades: Crie um dicionário chamado cities. Use os nomes de três
cidades como chaves em seu dicionário. Crie um dicionário com informações sobre
cada cidade e inclua o país em que a cidade está localizada, a população
aproximada e um fato sobre essa cidade. As chaves do dicionário de cada cidade
devem ser algo como country, population e fact. Apresente o nome de cada
cidade e todas as informações que você armazenou sobre ela.
'''

# Aqui o ponto chave é dicionários dentro de um dicionário

cities = {
    'dubai': {
        'country': 'Emirados Arabes',
        'population': 500000,
        'fact': 'too many bilionares',
    },
    'new york': {
        'country': 'estados unidos',
        'population': 200000000,
        'fact': 'random people', 
    },
    'beijing': {
        'country': 'china',
        'population': 50000000,
        'fact': 'china heart',
    },
    'tokyo': {
        'country': 'japan',
        'population': 10000000,
        'fact': 'china heart',
    },

}


for city, city_info in cities.items():
    print("\nCity: " + city.title())
    print("\tCountry:" + city_info['country'].title())
    print("\tPopulation: " + str(city_info['population']))
    print("\tFact: " + city_info['fact'].title())
