'''
7.10 – Férias dos sonhos: Escreva um programa que faça uma enquete sobre as
férias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se pudesse
visitar um lugar do mundo, para onde você iria? Inclua um bloco de código que
apresente os resultados da enquete.
'''

# Este exercicio é semelhante ao mountain_poll

# vamos usar o conceito de dicionário

# Inicia-se o dicionário vazio
responses = {}

# Define uma regra para indicar que a enquete está ativa:

dream_vacations_active = True

# Abertura do laço

while dream_vacations_active:
    # Pede o nome da pessoa e a resposta:
    name = input("Whats is you name? ")
    place = input("Where the place for a dream vacation? ")

    # Armazena resposta no dicionário:
    # Lembrando é chave (name) e valor (place)
    responses[name] = place

    # Aqui finaliza a enquete ou continua:
    repeat = input("Someone else need answer? (yes/no)")
    
    if repeat == 'no':
        dream_vacations_active = False

    # Listando as respostas

print("Aqui estão as respostas!: \n")

for name, place in responses.items():
    print(name.title() + " want to visit " + place.title())

