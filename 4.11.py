'''
4.11 – Minhas pizzas, suas pizzas: Comece com seu programa do Exercício 4.1
(página 97). Faça uma cópia da lista de pizzas e chame-a de friend_pizzas.
Então faça o seguinte:
• Adicione uma nova pizza à lista original.
• Adicione uma pizza diferente à lista friend_pizzas.
• Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas
favoritas são:; em seguida, utilize um laço for para exibir a primeira lista. Exiba a
mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize um laço
for para exibir a segunda lista. Certifique-se de que cada pizza nova esteja
armazenada na lista apropriada.
'''

pizzas = ['corn & bacon', 'marguerita', 'portuguesa', 'pepperoni']

friend_pizzas = pizzas[:]

pizzas.append('palmitela')
friend_pizzas.append('frango & catupiry')

for pizza in pizzas:
    print(pizza.title() + " wowowowow bom d+!")
    print("Gosto muito de pizzas estilo pizza hut")

print("Vamos comer uma pizza hoje?")

for pizzaf in friend_pizzas:
    print(pizzaf.title() + " Voce gosta dessas ne? ")
    print("Gosto muito de pizzas brasileiras")

    