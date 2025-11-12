'''
# Preenchendo um dicionário com dados de entrada do usuário

Podemos perdir a quantidade de entrada que for necessária a cada passagem do laço while. Vamos criar um programa 
de enquente em que cada passagem pelo laço while solicita o nome do participante e uma resposta.

Armazenaremos os dados coletados em um dicionário, pois queremos associar cada resposta a um usuário em particular.
'''

# Inicia o dicionário vazio

responses = {}


# Define uma flag para indicar que a enquete está ativa

polling_active = True

# Abertuda do laço

while polling_active:
    # Pede o nome da pessoa e a resposta
    name = input("\nWhats your name: ")
    response = input("Which montain would you like to climb someday? ")

    # Armazena a resposta no dicionario
    responses[name] = response

    # Descobre se outra pessoa vai responder à enquete.
    # Aqui irá finalizar a enquete
    repeat = input("Would you like to let another person responde? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# A enquete foi concluida. Mostra os resultados.
print("\n--- Poll Results ---")

for name, response in responses.items():
    print(name.title() + " would like to climb " + response.title() + ".")