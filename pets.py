'''
Removendo todas as instâncias de valores específicos de uma lista 

Suponha que tenhamos uma lista de animais de estimação com o valor 'cat' repetido várias vezes. 
Para remover todas as instâncias desse valor, podemos usar um laço while até 'cat' não estar mais na lista.
'''

# lista de pets
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

#exibindo a lista pets
print(pets)

# Removendo todos os valores cat da lista
while 'cat' in pets:
    pets.remove('cat')

#Exibe novamente a lista dessa vez sem os valores de cat

print(pets)