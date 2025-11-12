'''
### TRANSFERINDO ITENS DE UMA LISTA PARA OUTRA

Considere uma lista de usuários recém-registrados em um site, porém não verificados. 
Depois de conferir esses usuários como podemos transferi-los para uma lista separada de usuários confirmados?
Uma maneira seria usar um laço while para extrair os usuários da lista de usuários não confirmados à medida que
verificamos vamos adicionando em lista separada de usuários confirmados.
'''

# Começa com os usuários que precisam ser verificados,
# e com uma lista vazia para armazenar os usuários confirmados

unconfirmed_users = ['alice', 'brian', 'candace']

confirmed_users = []

# Verifica cada usuário até que não haja mais usuários não confirmados
# Transfere cada usuário verificado para a lista de usuários confirmados

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: "  +  current_user.title())
    confirmed_users.append(current_user)

# Exibe todos os usuários confirmados

print("\nThe following users have been confirmed: ")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())

