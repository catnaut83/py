# INFORMAÇÕES ANINHADAS

# Uma lista de dicionários


# Estes são os dicionários:

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# Esta é uma lista com dicionários
aliens = [alien_0, alien_1, alien_2]

print(">> Lista de dicionários:")
for alien in aliens:
    print(alien)

# Num cenário mais realista envolveria mais de 3 alienígenas. 
# Vamos gerar automaticamente usando range() para criar 30 aliens.

# Cria uma lista vazia para armazenas alienígenas
aliens = []

print("\nCriada a lista vazia:\n")
# Cria 30 alienígenas verdes
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

print("Mostra os 5 primeiros alienígenas da lista nova")
# Mostra os 5 primeiros alienígenas
for alien in aliens[:5]:
    print(alien)
print('...')

# Mostra quantos alienígenas foram criados
print("Total number os aliens: " + str(len(aliens)))

