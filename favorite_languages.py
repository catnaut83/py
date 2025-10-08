# DICIONARIO DE OBJETOS SEMELHANTES

favorite_language= {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " +
      favorite_language['sarah'].title() +
      '.')


# Percorrendo o dicionario com um laço

print("\nAqui vamos percorrer o dicionario com um laço:\n")
for name, language in favorite_language.items():
    print(name.title() + "'s favorite language is " +
          language.title() + '.')
    

# Agora vamos percorrer semente as chaves do dicionário como laço

print("\n>>Percorrendo somente as chaves do dicionário:")

for name in favorite_language.keys():
    print(name.title())

friends = ['phil', 'sarah']

for name in favorite_language.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_language[name].title() + "!")
        
# Utilizando o metodo keys() para verificar se uma pessoa esta
# ou nao no dicionario

if 'erin' not in favorite_language.keys():
    print('Erin, please take our poll!')

# Percorrendo as chaves de um dicionario -em ordem- usando um laço

for name in sorted(favorite_language.keys()):
    print(name.title() + ", thank you for taking the poll.")

# Percorrendo todos os valores de um dicionario com um laço -sem as chaves-

print("\nThe following languages have been mentioned:")

for language in favorite_language.values():
    print(language.title())

# Para verificar o mesmo caso sem repetiçõe usamos o modo conjunto
# denominado (set):
print("\nNO REPEART:")
print("The followinf languages have been mentoned:")

for language in set(favorite_language.values()):
    print(language.title())


#Outra maneira de demonstrar valores associados em dicionarios com listas:

favorite_language = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    'carol': ['pyhton', 'c'],
}

for name, languages in favorite_language.items():
    if len(languages) > 1:
        print('\n' + name.title() + "'s favorite languages are:")
    else:
        print('\n' + name.title() + "'s favorite languages is:")
    for language in languages:
        print('\t' + language.title())




