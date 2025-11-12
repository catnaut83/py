'''
7.8 – Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com os
nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada
finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e
mostre uma mensagem para cada pedido, por exemplo, Preparei seu sanduíche
de atum. À medida que cada sanduíche for preparado, transfira-o para a lista de
sanduíches prontos. Depois que todos os sanduíches estiverem prontos, mostre uma
mensagem que liste cada sanduíche preparado.
'''

# Mesmo conceito de confirmed_users2.py

# lista dos sanduiches a seres pedidos:

sandwich_orders = ['misto', 'americano', 'frango salada', 'queijo', 'italiano']

# Lista vazia a ser preenchida conforme os sanduiches vao sendo preparados
finished_sandwiches = []

# Laço para percorrer os sanduiches
while sandwich_orders:
    # Remove um item da lista e adiciona a variavel
    sanduba = sandwich_orders.pop()

    # Imprime justamente a variavel com o sanduiche removido da lista
    print("Preparando o sanduiche " + sanduba)

    # Atribui o sanduiche removido a nova lista
    finished_sandwiches.append(sanduba)

# Lista todos sanduiches preparados

for sandwich in finished_sandwiches:
    print("Finalizado o pedido do delicioso: " + sandwich)

