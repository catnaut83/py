'''
selecionar, ignorar numeros
'''

# Aqui o valor soma 2 a cada sequencia
even_numbers = list(range(0,10,2))
print(even_numbers)

squares = []
print(squares)
for value in range(1,10):
    square = value**2
    #adiciona um item a lista
    squares.append(square)

print(squares)

# ou modo conciso

cubos = []
for value in range(1,10):
    #adiciona item a lista de modo conciso
    cubos.append(value**3)

print(cubos)

# Funções estatísticas basicas

print("Trabalhando funções basicas de min, max e sum")
digits = [1,2,3,4,5,6,7,8,9,0]

print(min(digits))

print(max(digits))

print(sum(digits))



