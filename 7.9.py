'''
7.9 – Sem pastrami: Usando a lista sandwich_orders do Exercício 7.8, garanta
que o sanduíche de 'pastrami' apareça na lista pelo menos três vezes.
Acrescente um código próximo ao início de seu programa para exibir uma
mensagem informando que a lanchonete está sem pastrami e, então, use um laço
while para remover todas as ocorrências de 'pastrami' e sandwich_orders.
Garanta que nenhum sanduíche de pastrami acabe em finished_sandwiches.
'''

# Aqui é fazer semelhante ao exercicio anterior e a remover uma instancia da lista 
# como no exercicio pets.py

# lista dos sanduiches a seres pedidos:

sandwich_orders = ['misto', 'americano', 'pastrami', 'frango salada', 'pastrami', 'queijo', 'italiano', 'pastrami', 'pastrami']

print("---ATENÇÃO: ESTAMOS SEM SANDUICHE DE PASTRAMI!!---")

# Lista vazia a ser preenchida conforme os sanduiches vao sendo preparados
finished_sandwiches = []

while sandwich_orders:
    # Primeiro vamos remover as ocorrencias de 'pastrami'
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    # Agora que foram removidos, remover cada sanduiche e transferir para a lista de preparados
    sanduiche = sandwich_orders.pop()

    # Informando que o sanduiche está sendo prepadado
    print("Em preparação: " + sanduiche )
    
    # Adiciona o sanduiche a lista de finalizados
    finished_sandwiches.append(sanduiche)

# Lista dos sansuiches prepadados:
for finalizados in finished_sandwiches:
    print("Está aqui o seu pedido de sanduiche sabor: " + finalizados)