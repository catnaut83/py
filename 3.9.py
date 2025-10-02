'''
3.9 – Convidados para o jantar: Trabalhando com um dos programas dos
Exercícios de 3.4 a 3.7 (páginas 80 e 81), use len() para exibir uma mensagem
informando o número de pessoas que você está convidando para o jantar.
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

print("Quantidade de convidados:")
print(len(matters))

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