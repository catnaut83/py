motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

# Modificando items de uma lista
motorcycles[0] = 'royal enfield'

print(motorcycles)

# Adicionando elementos a uma lista com append()

motorcycles.append('honda')

print(motorcycles)


motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('triumph')
motorcycles.append('royal enfiel')

print(motorcycles)

#Inserindo elementos em uma lista usando insert() para adicionar em qualquer posição da lista.

motorcycles = ['yamaha', 'suzuki', 'honda']
print(motorcycles)

motorcycles.insert(0, 'ducati')

print(motorcycles)

# Removendo items de uma lista

#por posição
del motorcycles[0]
print(motorcycles)

del motorcycles[2]
print(motorcycles)

# Removendo pelo método pop(): remove o item mas ainda é possível trabalhar com ele
# diferente do del que remove completamente

motorcycles = ['royal enfield', 'honda', 'suzuki', 'yamaha', 'houjue']
print(motorcycles)

popped_motorcycle = motorcycles.pop()

print(motorcycles)
print(popped_motorcycle)

# Na pratica o pop() remove o ultimo item e é util por exemplo, eu quero ver o ultimo registro
# de uma motocicleta comprada

motorcycles = ['suzuki', 'yamaha', 'yamaha', 'bmw', 'yamaha', 'suzuki', 'yamaha', 'honda', 'royal enfield']
last_owned = motorcycles.pop()

print(motorcycles)
print(last_owned)

print("The last motorcycle that I owned was a " + last_owned.title()+ ".")


# Removendo itens de qualquer posição em uma lista usando o pop()

motorcycles = ['suzuki', 'yamaha', 'yamaha', 'bmw', 'yamaha', 'suzuki', 'yamaha', 'honda', 'royal enfield']
first_owned = motorcycles.pop(0)

print(motorcycles)
print('The First Motorcycle that I owned was a ' + first_owned.title() + '.')

# Removendo um item de acordo com o valor
# Neste caso não preciso saber a posição que ele está. Usaremos o remove()

motorcycles = ['honda', 'yahama', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')

print(motorcycles)

#Também podemos trabalhar os valores de remove armazenando em outra variavel
motorcycles = ['honda', 'yahama', 'suzuki', 'ducati']

print(motorcycles)
too_expensive = 'ducati'

motorcycles.remove(too_expensive)

print(motorcycles)

print("\nA " + too_expensive.title() + " is too expensive for me.")


