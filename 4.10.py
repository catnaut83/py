'''
4.10 – Fatias: Usando um dos programas que você escreveu neste capítulo,
acrescente várias linhas no final do programa que façam o seguinte:
• Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia
para exibir os três primeiros itens da lista desse programa.
• Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir três
itens do meio da lista.
• Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para exibir
os três últimos itens da lista.
'''

my_foods = ['pizza', 'japonese', 'hamburg', 'hot dog', 'lasanha', 'nhoque', 'lamen']

print("3 primeiros itens:")
# Percorrendo uma fatia com um laço
print("Here are the first three players on my team:")
for food in my_foods[:3]:
    print(food)

print("3 items do meio:")
for food in my_foods[2:5]:
    print(food)

print("os 3 ultimos items da lista:")
for food in my_foods[4:]:
    print(food)


