dic = {}


def listar_todos():
    if len(dic) > 0:
        print(dic.items())
    else:
        print('Não existe elementos no dicionário')


def criar_campo():
    chave = input('Informe o nome da chave: ')
    valor = input('Informe o nome do valor: ')
    dic[chave] = valor
    print('Campo adicionado com sucesso!')


def busca_informacao():
    if len(dic) > 0:
        buscar = input('Informe o indice do campo: ')
        print(dic[buscar])
    else:
        print('Não existe nenhum campo criado para buscar informações!')


def alterar_valor():
    if len(dic) > 0:
        buscar = input('Informe o nome da chave que terá o valor alterado!')
        novo_valor = input('Informe o novo valor da chave: ')
        dic[buscar] = novo_valor
        print('Valor alterado com sucesso!')
    else:
        print('Não existe um valor para ser alterado!')

def deletar_campo():
    if len(dic) > 0:
        buscar = input('Informe o nome da chave que você quer deletar o campo: ')
        del dic[buscar]
        print('Campo deletado com sucesso')
    else:
        print('Não existe campo para ser deletado!')

while True:
    print('-=' * 33)
    print('#' * 33)
    print('# 1 - Listar campo              #')
    print('# 2 - Criar um campo            #')
    print('# 3 - Buscar informação         #')
    print('# 4 - Alterar valor do campo    #')
    print('# 5 - Deletar campo             #')
    print('# 0 - SAIR                      #')
    print('#' * 33)

    opcao = int(input('Informe uma opção: '))

    if opcao == 1:
        listar_todos()
    elif opcao == 2:
        criar_campo()
    elif opcao == 3:
        busca_informacao()
    elif opcao == 4:
        alterar_valor()
    elif opcao == 5:
        deletar_campo()
    elif opcao == 0:
        print('Obrigado por usar nosso programa!')
        break
    else:
        print('Opção inválida')