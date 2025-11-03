'''
7.4 - Ingredientes para uma pizza: Escreva um laço que peça ao usuario para fornecer uma serie de ingredientes para uma pizza até o que o valor 'quit'
seja fornecido. À medida que cada ingrediente é especificado, apresente uma mensagem informando que você acrescentarpa esse ingrediente à pizza.
'''

prompt = "\nO que gostaria na sua pizza?"
prompt += "\n(Quando quiser finalizar digite quit)"

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print("Adicionado " + topping.title() + " à sua pizza!")
        