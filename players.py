# Fatiando uma lista


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[2:5])

# sem informar o inicio do indice, python pega automaticamente
print("Sem um indice de inicio:")
print(players[:2])

# Agora referenciando para python ir até o final da lista a partir de um indice:
print("de um indice até o final:")
print(players[2:])

# Percorrendo uma fatia com um laço
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player)


