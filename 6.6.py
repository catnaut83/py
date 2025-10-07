'''
6.6 – Enquete: Utilize o código em favorite_languages.py (página 150).
• Crie uma lista de pessoas que devam participar da enquete sobre linguagem
favorita. Inclua alguns nomes que já estejam no dicionário e outros que não
estão.
• Percorra a lista de pessoas que devem participar da enquete. Se elas já tiverem
respondido à enquete, mostre uma mensagem agradecendo-lhes por responder.
Se ainda não participaram da enquete, apresente uma mensagem convidando-as
a responder.
'''


guests = ['jen', 'sarah', 'edward', 'billie', 'tod', 'june', 'sakura']

favorite_language= {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in guests:
    if name not in favorite_language.keys():
        print(name.title() + ', please take our poll!')
    else:
        print(name.title() + ', Thanks to join our poll!')


