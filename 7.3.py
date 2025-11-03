'''
7.3 - Multiplos de dez: Peça um numero ao usuário e, em seguida, informse se 
o número é múltiplo de dez ou não.
'''


mult = input("Informe um numero: ")
mult = int(mult)

if mult % 10 == 0:
    print("O numero " + str(mult) + " é múltiplo de 10!")
else:
    print("O numero " + str(mult) + " não é múltiplo de 10!")