'''
5.2 – Mais testes condicionais: Você não precisa limitar o número de testes que
criar em dez. Se quiser testar mais comparações, escreva outros testes e acrescenteos
em conditional_tests.py. Tenha pelo menos um resultado True e um False para
cada um dos casos a seguir:
1• testes de igualdade e de não igualdade com strings;
2• testes usando a função lower();
3• testes numéricos que envolvam igualdade e não igualdade, maior e menor que,
maior ou igual a e menor ou igual a;
4• testes usando as palavras reservadas and e or;
5• testes para verificar se um item está em uma lista;
6• testes para verificar se um item não está em uma lista.
'''
# 1 teste de igualdade e nao igualdade com strings
star = 'sirius'
print('Is the star sirius?')
print(star == 'sirius')
print('Is the star aldebaran?')
print(star == 'aldebaran')

#2 teste usando a função lower
constelation = 'ORION'
print('is the constelation orion?')
print(constelation.lower() == 'orion')
print('is the constelation Orion?')
print(constelation == 'Orion')

# 3 teste numero com igualdade, nao igualdade, maior que, menor que, 
# maior igual e menor igual
num = 11
num2 = 18
num_list = [10, 11, 12, 13, 14]

print("Este numero é 11?")
print(num == 11)
print('Este numero é diferente de 11?')
print(num != 11)
print('Este numero é maior que 10?')
print(num > 10)
print('Este numero é menor que 10?')
print(num < 10)
print('Este numero é maior igual a 10?')
print(num >= 10)
print('Este numero é menor igual a 10?')
print(num <= 10)

# 4 teste com palavras reservadas and e or
print("Este numero esta entre 10 e 20?")
print(num >= 10 and num <= 20)
print("Este numero pode ser 10 ou 11?")
print(num == 10 or num == 11)

# 5 com para saber se está em uma lista
if num in num_list:
    print('Ok, o numero 11 esta na lista')

# 6 testa para saber se nao esta em lista
if num2 not in num_list:
    print('Ok o numero 18 nao esta na lista')