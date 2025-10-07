'''
5.9 – Sem usuários: Acrescente um teste if em hello_admin.py para garantir que a
lista de usuários não esteja vazia.
• Se a lista estiver vazia, mostre a mensagem Precisamos encontrar alguns
usuários!
• Remova todos os nomes de usuário de sua lista e certifique-se de que a
mensagem correta seja exibida.
'''

'''
ESTE EXERCICIOS NAO FAZ SENTIDO E NAO TEM SOLUÇÃO CLARA NEM VINDA DO AUTOR
'''

#usernames = []

usernames = ['mega_monsterhigh', 'titan2099', '3i/atlas', 'matrix_dominator', 'lunarsense890']


for user in usernames:
    print('Este usuario ' + user + ' sera removido!')
    usernames.remove(user)
    print(usernames)