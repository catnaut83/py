'''
6.12 – Extensões: Estamos trabalhando agora com exemplos complexos o
bastante para poderem ser estendidos de várias maneiras. Use um dos programas
de exemplo deste capítulo e estenda-o acrescentando novas chaves e valores,
alterando o contexto do programa ou melhorando a formatação da saída.
'''

# Vou falar sobre os meus gatos, criar um dicionario de gatos

gatos = {
    'sirius' : {
        'cor': 'preto',
        'idade': 7,
        'caracteristica': 'tranquilo, doce, carinhoso, gordo',
        'apelidos': 'bruxão, pêto, petão, doção, pitico, pantera, exuzão',
    },
      'thoth' : {
        'cor': 'tigrado',
        'idade': 7,
        'caracteristica': 'agitado, nervosinho, carinhoso, grude',
        'apelidos': 'tigrão, tigrones, thotão'
    },
      'juno' : {
        'cor': 'frajola',
        'idade': 6,
        'caracteristica': 'tranquila, desconfiada, vaidosa, carinhosa',
        'apelidos': 'jujuno, pêta, macia'
    },
      'fujiko' : {
        'cor': 'tricolor',
        'idade': 6,
        'caracteristica': 'tranquila, doce, carinhosa, fofa',
        'apelidos': 'fufuji, fuji, japonesa, florzinha, menininha'
    },
      'cibele' : {
        'cor': 'tigrada com branco',
        'idade': 6,
        'caracteristica': 'energetica, brincalhona, carinhosa, comilona',
        'apelidos': 'cibelinha, mamaezinha, godinha'
    },
      'orion' : {
        'cor': 'cinza e branco',
        'idade': 6,
        'caracteristica': 'tranquila, carinhosa, ciumenta, falante',
        'apelidos': 'constelação, lobinha, menininha'
    },
      'athena' : {
        'cor': 'cinza (blue)',
        'idade': 5,
        'caracteristica': 'tranquila, desconfiada, carinhosa, misteriosa',
        'apelidos': 'de mentira, morceguinha, gotosa, menininha'
    },
      'lyon' : {
        'cor': 'amarelo',
        'idade': 6,
        'caracteristica': 'tranquilo, doce, carinhoso, gordo',
        'apelidos': 'leãozinho, menininho, gordinho'
    },
      'luan' : {
        'cor': 'siamês',
        'idade': 2,
        'caracteristica': 'peralta, doce, carinhoso, brincalhão',
        'apelidos': 'capuccino, chocolate, menininho'
    },
      'joaquim' : {
        'cor': 'tigrado',
        'idade': 2,
        'caracteristica': 'tranquilo, doce, carinhoso, desconfiado',
        'apelidos': 'neném, meninino, gotoso'
    },
}

print("Meus gatos são os mais lindos e perfeitos!")
print("\nAqui estão algumas característica sobre eles:\n")

for gato, gato_info in gatos.items():
    print("Nome da fofura: " + gato.title() )
    print("Características da fofura: ")
    print("\tCor: " + gato_info['cor'].title())
    print("\tIdade: " + str(gato_info['idade']))
    print("\tCaracterística: " + gato_info['caracteristica'].title())
    print("\tApelidos: " + gato_info['apelidos'].title())
