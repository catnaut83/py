# UTILIZANDO DICIONARIOS

# Um dicionario é par chave-valor

print('Criando o dicionario alien_0:')
alien_0 = { 'color': 'green', 'points': 5}

print(alien_0['color'])

print(alien_0['points'])

new_points = alien_0['points']

print("You just earned " + str(new_points) + " points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print('Adicionando novas informações ao dicionario alien_0:')
print(alien_0)

print('Começando com um dicionario vazio, vamos esvaziar alien_0')

alien_0 = {}

print(alien_0)

#agora vamos adicionar pares chave-valor

alien_0['color'] = 'green'
alien_0['points'] = 5

print('\nAgora adicionamos novos pares-valor:')
print(alien_0)

#Modificando valores em um dicionario
print('\nModificando valores em um dicionario:\n')

alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + '.')

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + '.')

# exemplo de monitorar a posição de um alienigena

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium' }
print("Original x-position: " + str(alien_0['x_position']))

# Move o alienigena para a direta
# Determina a distância que o alienigena deve se deslocar de acordo
# com sua velocidade atual

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Este deve ser um alienígena rápido
    x_increment = 3

# A nova posição é a antiga somada ao incremento

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("\nNew x-position: " + str(alien_0['x_position']))

# Removendo pares chave-valor

print("\nRemovendo chave-valor:")

alien_0 = {'color': 'green', 'points': 5}
print('Aqui é o dicionario completo com a cor e os pontos:')
print(alien_0)

# deletando

print('Aqui é apos deletar os pontos:')
del alien_0['points']
print(alien_0)
