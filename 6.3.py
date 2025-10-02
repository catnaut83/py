'''
6.3 – Glossário: Um dicionário Python pode ser usado para modelar um dicionário
de verdade. No entanto, para evitar confusão, vamos chamá-lo de glossário.
• Pense em cinco palavras relacionadas à programação que você conheceu nos
capítulos anteriores. Use essas palavras como chaves em seu glossário e
armazene seus significados como valores.
• Mostre cada palavra e seu significado em uma saída formatada de modo
elegante. Você pode exibir a palavra seguida de dois-pontos e depois o seu
significado, ou apresentar a palavra em uma linha e então exibir seu significado
indentado em uma segunda linha. Utilize o caractere de quebra de linha (\n)
para inserir uma linha em branco entre cada par palavra-significado em sua
saída.
'''

glos = {
    'python': 'Linguagem super interessante que me abrirá portas.',
    'listas': 'Em Python listas parecem ser mais fáceis.',
    'condicional': 'Condicionais if-elif-else em Python são práticos.',
    'for': 'Percorrer uma lista com for em python é muito elegante e prático.' ,
    'dicionario': 'Conceito de dicionário em Python é total novidade para mim.'
}

print('Minha opinião sobre Python é: \n' + glos['python'])

print ('\nPude aprender mais sobre listas. \n' + glos['listas'])

print('\nAprendi a estruturar melhor o if: ' + glos['condicional'])

print('\nFor em algumas linguagens é complexo. \n' + glos['for'])

print('\n' + glos['dicionario'])

print("Adorei!")