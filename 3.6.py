"""
3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
portanto agora tem mais espaço disponível. Pense em mais três convidados para o
jantar.
• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
uma instrução print no final de seu programa informando às pessoas que você
encontrou uma mesa de jantar maior.
• Utilize insert() para adicionar um novo convidado no início de sua lista.
• Utilize insert() para adicionar um novo convidado no meio de sua lista.
• Utilize append() para adicionar um novo convidado no final de sua lista.
• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que
está em sua lista.
"""
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