# Aqui vamos verificar se um item nao esta na lista

banned_users = ['andrew', 'carolina', 'david']

user = 'marie'
#Booleano
user_active = True

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

