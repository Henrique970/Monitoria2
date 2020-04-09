# TODO: Criar uma função para excluir um elemento da lista.
# TODO: Criar uma função para buscar contato por índice.
# TODO: E também buscar pelo nome do contato.
# TODO: Criar uma função para alterar o contato.
# TODO: Modificar para mostrar o indice quando for listar os contatos.

contatos = []

def lista_contato():
    if len(contatos) > 0:
        for i, contato in enumerate(contatos):
            print(i,contato)
    else:
        print('Não existe contatos na cadastrados!')

def criar_contatos():
    nome = input('Informe o nome do contato: ')
    telefone = input('Informe o número do contato: ')
    contatos.append([nome, telefone])
    print('Contato cadastrado com sucesso!')

def buscar_por_indice():
    if len(contatos) > 0:
        buscar = int(input('Informe o indíce do contato: '))
        if buscar >= len(contatos):
            print('Contato não existente!')
        else:
            print(contatos[buscar])
    else:
        print('Não existe nenhum contato cadastrado para realizar a busca!')

def buscar_por_nome():
    if len(contatos) > 0:
        buscar = input('Informe o nome do contato: ')
        if buscar in contatos:
            print('Contato não existente!')
        else:
            nome = buscar
            for i, contato in enumerate(contatos):
                if contato[0] == nome:
                    print(i, contato)
    else:
        print('Não existe contatos para serem pesquisados!')

def alterar_contato():
    if len(contatos) > 0:
        buscar = int(input('Informe um indíce do contato para ser alterado: '))
        if buscar >= len(contatos):
            print('Contato não existente!')
        else:
            alterar_nome = input('Informe o novo nome do contato: ')
            alterar_telefone = input('Informe o novo número do contato: ')
            contatos[buscar] = [alterar_nome, alterar_telefone]
            print('Contato alterado com sucesso!')
    else:
        print('Não existe contato para ser alterado!')

def deletar_contato():
    if len(contatos) > 0:
        buscar = int(input('Informe um indíce do contato para ser deletado: '))
        if buscar >= len(contatos):
            print('Contato não existente!')
        else:
            del contatos[buscar]
            print('Contato deletado com sucesso!')
    else:
        print('Não existe contato para ser deletado!')


while True:
    print('-=' * 33)
    print('#' * 33)
    print('# 1 - Listar contatos           #')
    print('# 2 - Criar contato             #')
    print('# 3 - Buscar contato por indíce #')
    print('# 4 - Buscar contato por nome   #')
    print('# 5 - Alterar contato           #')
    print('# 6 - Deletar contato           #')
    print('# 0 - SAIR                      #')
    print('#' * 33)

    opcao = int(input('Informe uma opção: '))

    if opcao == 1:
        lista_contato()
    elif opcao == 2:
        criar_contatos()
    elif opcao == 3:
        buscar_por_indice()
    elif opcao == 4:
        buscar_por_nome()
    elif opcao == 5:
        alterar_contato()
    elif opcao == 6:
        deletar_contato()
    elif opcao == 0:
        print('Obrigado por usar nosso programa!')
        break
    else:
        print('Opção inválida')
