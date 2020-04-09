dic = {}

#1
def listar_campo():
    if len(dic) > 0:
        print(dic)
    else:
        print('Não existe campos no dicionário!')
#2
def criar_campo():
    chave = input('Informe o nome da chave: ')
    valor = input('Informe o valor da chave: ')
    dic[chave] = valor
    print('Campo adcionado com sucesso!')

#3
def buscar_informação():
    if len(dic) > 0:
        chave = input('Informe o nome da chave para mostrar o valor: ')
        print(dic[chave])
    else:
        print('Não existe campos para se buscar!')

#4
def alterar_valor():
    if len(dic) > 0:
        chave = input('Informe o nome da chave para ser alterada: ')
        novo_valor = input('Informe o novo valor da chave: ')
        dic[chave] = novo_valor
        print('Valor da chave alterado com sucesso!')
    else:
        print('Não existe campos para alterar!')

#5
def deletar_campo():
    if len(dic) > 0:
        chave = input('Informe o nome da chave para ser deletada: ')
        del dic[chave]
        print('Chave deletada com sucesso!')
    else:
        print('Não existe campos para deletado!')
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
        listar_campo()
    elif opcao == 2:
        criar_campo()
    elif opcao == 3:
        buscar_informação()
    elif opcao == 4:
        alterar_valor()
    elif opcao == 5:
        deletar_campo()
    elif opcao == 0:
        print('Obrigado por usar nosso programa!')
        break
    else:
        print('Opção inválida')