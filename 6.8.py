'''
6.8 – Animais de estimação: Crie vários dicionários, em que o nome de cada
dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua o
tipo do animal e o nome do dono. Armazene esses dicionários em uma lista
chamada pets. Em seguida, percorra sua lista com um laço e, à medida que fizer
isso, apresente tudo que você sabe sobre cada animal de estimação.
'''

# Lista vazia

pets = []

pet = {
    'name': 'sirius',
    'type': 'cat',
    'tutor': 'carol',
    'color': 'black',
    'eats': 'meat',
}

pets.append(pet)

pet = {
    'name': 'thoth',
    'type': 'cat',
    'tutor': 'carol',
    'color': 'tabby',
    'eats': 'meat',
}

pets.append(pet)

pet = {
    'name': 'juno',
    'type': 'cat',
    'tutor': 'carol',
    'color': 'tuxedo',
    'eats': 'meat',
}

pets.append(pet)

pet = {
    'name': 'fujiko',
    'type': 'cat',
    'tutor': 'carol',
    'color': 'calico',
    'eats': 'meat',
}

pets.append(pet)

pet = {
    'name': 'cibele',
    'type': 'cat',
    'tutor': 'carol',
    'color': 'tabby',
    'eats': 'meat',
}

pets.append(pet)

pet = {
    'name': 'orion',
    'type': 'cat',
    'tutor': 'carol',
    'color': 'bicolor',
    'eats': 'meat',
}

pets.append(pet)

pet = {
    'name': 'lyon',
    'type': 'cat',
    'tutor': 'carol',
    'color': 'yellow',
    'eats': 'meat',
}

pets.append(pet)

pet = {
    'name': 'athena',
    'type': 'cat',
    'tutor': 'carol',
    'color': 'blue',
    'eats': 'meat',
}

pets.append(pet)

pet = {
    'name': 'luan',
    'type': 'cat',
    'tutor': 'carol',
    'color': 'siamese',
    'eats': 'meat',
}

pets.append(pet)

pet = {
    'name': 'joaquim',
    'type': 'cat',
    'tutor': 'carol',
    'color': 'tabby',
    'eats': 'meat',
}

pets.append(pet)

#for pet in pets:
#    print("\n### This cute information:")
#    print('Name: ' + pet['name'].title())
#    print('Type: ' + pet['type'].title())
#    print('Tutor: ' + pet['tutor'].title())

# Outra maneira, o que é mais interessante pois já lista todos os atributos


for pet in pets:
    print("\nHere's is what we know about this cute baby called " + pet['name'].title() + ':')
    for key, value in pet.items():
        print(key + ': ' + value)