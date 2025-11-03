'''
7.2 - Lugares em um restaurante: Escreva um programa que pergunte ao usuário
quantas pessoas estão em seu grupo para jantar. Se a resposta for maior que oito,
exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso contrário,
informe que sua mesa está pronta.
'''

convidados = input("Mesa para quantos? ")
convidados = int(convidados)

if convidados > 8:
    print("Como estão em " + str(convidados) + " terão de aguardar uma mesa.")
else:
    print("Mesa para " + str(convidados) + " convidados está pronta!")