# Deixando o usuario decidir quando quer sair

# vamos definir um valor de saida. 
# O programa so ira terminar quando o usuario digitar quit

prompt = "\Tell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program.\n"

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
        print("\n\n")