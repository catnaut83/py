# Métodos de Ordenamento de uma lista

#sort()

cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()

# a lista aparecerá em ordem alfabética de maneira permanente 
# (nao é possivel voltar a ordem original)

print(cars)

# ordem inversa

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)

print(cars)

# Ordenamento temporário com sorted()
# para preservar a ordem original

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("Here is the list sorted")
print(sorted(cars))

print("Here is the list original again:")
print(cars)

print("HEre is the list inverted")
print(sorted(cars, reverse=True))

print("o.o and list original again")
print(cars)

# Invertendo a lista em ordem inversa: nao ordem alfabetica e sim inverte a ordem da lista

print(cars)
cars.reverse()

print(cars)


# Descobrindo o tamanho de uma lista
print("Tamanho da lista")
print(len(cars))


# Utilizando a estrutura if/else
print("Utilizando a estrutura if/else:")

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())  