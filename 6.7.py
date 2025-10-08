'''
6.7 – Pessoas: Comece com o programa que você escreveu no Exercício 6.1
(página 147). Crie dois novos dicionários que representem pessoas diferentes e
armazene os três dicionários em uma lista chamada people. Percorra sua lista de
pessoas com um laço. À medida que percorrer a lista, apresente tudo que você
sabe sobre cada pessoa.
'''

#Observação:
# A estrutura do dicionário não deve ser encavalada dentro da lista.

people = []

person = {
    'first_name': 'fabiana',
    'last_name': 'menezes',
    'age': 49,
    'city': 'nova odessa',
}

people.append(person)

person = {
    'first_name': 'caroline',
    'last_name': 'lopez',
    'age': 42,
    'city': 'nova odessa',
}
people.append(person)
person = {
    'first_name': 'vitoria',
    'last_name': 'lopez',
    'age': 21,
    'city': 'campinas',
}
people.append(person)

for person in people:
    print('First Name: ' + person['first_name'].title())
    print('Last Name: ' + person['last_name'].title())
    print('Age: ' + str(person['age']))
    print('City: ' + person['city'].title())



