'''
6.4 – Glossário 2: Agora que você já sabe como percorrer um dicionário com um
laço, limpe o código do Exercício 6.3 (página 148), substituindo sua sequência de
instruções print por um laço que percorra as chaves e os valores do dicionário.
Quando tiver certeza de que seu laço funciona, acrescente mais cinco termos de
Python ao seu glossário. Ao executar seu programa novamente, essas palavras e
significados novos deverão ser automaticamente incluídos na saída.
'''

glos = {
    'python': 'Linguagem super interessante que me abrirá portas.',
    'listas': 'Em Python listas parecem ser mais fáceis.',
    'condicional': 'Condicionais if-elif-else em Python são práticos.',
    'for': 'Percorrer uma lista com for em python é muito elegante e prático.' ,
    'dicionario': 'Conceito de dicionário em Python é total novidade para mim.'
}

#agora vamos adicionar pares chave-valor

glos['while'] = 'Ainda há muito o que descobrir para usar.'
glos['classes'] = 'Descobrir orientação a objeto em Python.'
glos['ponteiros'] = 'Existe algo semelhante?'
glos['DataScience'] = 'Descobrir como usar.'
glos['IA'] = 'Esse é o objetivo!'

#alien_0['color'] = 'green'
#alien_0['points'] = 5

for word, sign in glos.items():
    print(word.title() + ": " + sign)

