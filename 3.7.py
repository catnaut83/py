'''
3.7 – Reduzindo a lista de convidados: Você acabou de descobrir que sua nova
mesa de jantar não chegará a tempo para o jantar e tem espaço para somente
dois convidados.
• Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
mostre uma mensagem informando que você pode convidar apenas duas pessoas
para o jantar.
• Utilize pop() para remover os convidados de sua lista, um de cada vez, até que
apenas dois nomes permaneçam em sua lista. Sempre que remover um nome de
sua lista, mostre uma mensagem a essa pessoa, permitindo que ela saiba que
você sente muito por não poder convidá-la para o jantar.
• Apresente uma mensagem para cada uma das duas pessoas que continuam na
lista, permitindo que elas saibam que ainda estão convidadas.
• Utilize del para remover os dois últimos nomes de sua lista, de modo que você
tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem uma
lista vazia no final de seu programa.
'''

matters = ['fabi', 'luh', 'barts']

print("My love "+ matters[0].title() + " come dinner with me forever!")
print(matters[1].title() + " the best cunhada :)")
print(matters[2].title() + " dear prima from heart")

cant = matters.pop(2)


print("But, " + cant.title() + " was not able to go")

matters.append('sogra')

print(matters)

print("My love "+ matters[0].title() + " come dinner with me forever!")
print(matters[1].title() + " the best cunhada :)")
print(matters[2].title() + " dear sogra from heart")

print("Nossa, tenho a informação que uma mesa maior está disponível!")
print("Vamos adicionar mais 4 convidados:")

matters.append('exu caveira')
matters.append('exu tranca ruas')
matters.insert(0, 'pombagira maria quitéria')
matters.insert(2, 'pombagira maria mulambo')


print("Salve Querida Dona " + matters[0].title() + " Laroyê Saravá, venha jantar comigo, será um prazer sua presença!")
print("Meu amor "+ matters[1].title() + " venha jantar comigo para sempre!")
print("Salve Querida Dona " + matters[2].title() + " Laroyê Saravá, venha jantar comigo, será um prazer sua presença!")
print(matters[3].title() + " A melhor cunhada, venha jantar")
print(matters[4].title() + " minha querida sogra venha jantar")
print("Salve Querido " + matters[5].title() + " Laroyê Exu, Exu é de Mojubá! Venha Jantar comigo, será uma honra recebê-lo" )
print("Salve Querido " + matters[6].title() + " Laroyê Exu, Exu é de Mojubá! Venha Jantar comigo, será uma honra recebê-lo" )

print("É uma honra receber todos vocês, mas agora creio que teremos somente dois convidados")



print("Obrigada por tudo querido " + matters.pop().title())
print("Obrigada por tudo querido " + matters.pop().title())
print("Obrigada por tudo querida " + matters.pop().title())
print("Obrigada por tudo querida " + matters.pop().title())
print("Obrigada por tudo querida " + matters.pop().title())

print("Obrigada por tudo querida " + matters[0].title())
del matters[0]
print("Obrigada por tudo querida " + matters[0].title())
del matters[0]

print(matters)