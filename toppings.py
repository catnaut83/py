# Estes exemplos começam baseados no capitulo 5
# Estruturas if/else +++

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")


# Verificando se um item está em uma lista

requested_topping = ['mushrooms', 'onions', 'pineapple']

if 'mushrooms' in requested_topping:
    print('Sim, temos cogumelos')

if 'pepperoni' in requested_topping:
    print('Sim, temos peperoni')

#------------
# IF com várias opções validas

if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni.")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese.")

print("\nFinished making your pizza")


requested_topping = []

if requested_topping:
    for requested_top in requested_topping:
        print('Adding ' + requested_top + '.')
    print('\Fininshed making your pizza! Finally! ":)"')
else:
    print('\nAre you sure you want to plain a pizza?')

# Usando várias listas

print("### USANDO VÁRIAS LISTAS ###\n")

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + '.')
    else:
        print("Sorry, we don't have " + requested_topping + '.')

print("\n Finished making your pizza!")

