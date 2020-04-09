dicionario = {'nome': 'marciana',
              'telefone': '94211643'}

def listar_campos():
    if len(dicionario) > 0:
        print(dicionario.items())
    else:
        print('Não tem nada!')

while True:
    print('# 1 listar campos #')
    print('# 0 SAIR          #')

    opcao = int(input('Infome uma opção: '))

    if opcao == 1:
        listar_campos()
    elif opcao == 0:
        break
    else:
        print('Opção inválida')
