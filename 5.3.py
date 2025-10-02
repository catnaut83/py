'''
5.3 – Cores de alienígenas #1: Suponha que um alienígena acabou de ser
atingido em um jogo. Crie uma variável chamada alien_color e atribua-lhe um
valor igual a 'green', 'yellow' ou 'red'.
• Escreva uma instrução if para testar se a cor do alienígena é verde. Se for,
mostre uma mensagem informando que o jogador acabou de ganhar cinco
pontos.
• Escreva uma versão desse programa em que o teste if passe e outro em que ele
falhe. (A versão que falha não terá nenhuma saída.)
'''

alien_color = 'yellow'

if alien_color == 'red':
    points = 0
elif alien_color == 'yellow':
    points = 3
elif alien_color == 'green':
    points = 5

print("Voce acabou de ganhar " + str(points) + " pontos!")
