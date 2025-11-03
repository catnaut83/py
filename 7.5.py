'''
7.5. - Ingressos para o cinema: Um cinema cobra preços diferentes para os ingressos de acordo com a idade de uma pessoa. Se a pessoa tiver menos de 3 anos,
nem deveria esta la, portanto nao pode entrar. Se tiver entre 3 e 12, o ingresso custará 50 dolares, se tiver mais de 12 anos custará 15 dolares. Se tiver mais de 
18 anos, custará 10 dolares.
Escreva um laço em que você pergunte a idade aos usuários e, então, informe-lhes o preço do ingresso do cinema.
'''


prompt = "Qual a sua idade para assistir ao filme?"
prompt += "(Digite 'quit' quando finalizar!)"

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age <= 3:
        print('Voce nao pode entrar, vai atrapalhar a sessao chorando e gritando! heheheh')
    elif age <= 12:
        print('Voce criança chata se quiser ver o filme vai pagar caro! E comporte-se! Pague 50 dolares')
    else:
        print("Seu ingresso custará 10 dolares")