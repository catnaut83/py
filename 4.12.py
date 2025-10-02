'''
4.12 – Mais laços: Todas as versões de foods.py nesta seção evitaram usar laços
for para fazer exibições a fim de economizar espaço. Escolha uma versão de
foods.py e escreva dois laços for para exibir cada lista de comidas.
'''

my_foods = ['pizza', 'japonese', 'hamburg', 'hot dog']
friend_foods = my_foods[:]

my_foods.append('pasta')
friend_foods.append('ice cream')

print("My favorite foods are:")
for foodm in my_foods:
    print(foodm)

print("\nMy friends favorite foods are:")
for foodf in friend_foods:
    print(foodf)
