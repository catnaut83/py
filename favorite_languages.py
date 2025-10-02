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

