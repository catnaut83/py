# Escrevendo prompts claros

#name = input("Please enter upi name: ")
#print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt +="\nWhats is yout first name? "


name = input(prompt)

print ("\Hello, " + name + "!")

# input() é para aceitar entradas em forma de string
# int() é para aceitar entradas numericas

age = input("How old are you?")
print(age)

#Aqui demonstra-se o erro de trackback
#age >=18

#Vamos tratar para que convertendo para a função int()

age = int(age)

age >= 18