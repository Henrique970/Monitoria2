dicionario = {}

def listar_campos():
    if len(dicionario) > 0:
        print(dicionario.items())
    else:
        print('Não ah campos no dicionario')

def adicionar():
    chave = input('Informe o nome da chave: ' )
    valor = input('Inforome o valor da chave: ')
    dicionario[chave] = valor


while True:
    print(' 1 - Listar Campos')
    print(' 2 - Adicionar')
    print(' 3 - SAIR')

    opcao = int(input('Informe sua opção: '))

    if opcao == 1:
        listar_campos()
    elif opcao == 2:
        adicionar()
    elif opcao == 3:
        break
    else:
        print('Opçao invalida')
