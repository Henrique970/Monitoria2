# TODO: Problema 1
import random

produtos = [{}]

codigo = random.randint(1000,9998)
#1
def listar_produtos():
    if len(produtos) > 0:
        for i, produto in enumerate(produtos):
            print(produto)
    else:
        print('Não existe contatos na cadastrados!')

#2
def inserir_produtos():
    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto: '))
    preco_desconto = float(input('Informe o desconto do produto: '))
    produtos.append({'Código':codigo, 'Nome':nome, 'Preço':preco, 'Desconto': preco_desconto})
    print('Produto Cadastrado com sucesso!')

#3
def buscar_por_codigo():
    if len(produtos) > 0:
        busca = int(input('Informe o código do produto: '))
        for p in produtos:
            if p['Código'] == busca:
                print(p)
            else:
                print('Não existe produto com esse código!')
    else:
        print('Não existe produtos para ser pesquisados!')

#4
def excluir_produto():
    pass


#5
def alterar_produto():
    if len(produtos) > 0:
        pass
    else:
        print('Não há produtos inseridos para alterar')

#6
def valor_total_produtos():
    if len(produtos) > 0:
        pass
    else:
        print('Não há produtos inseridos para dar o valor total!')

#7
def quantidade_produtos():
    if len(produtos) > 0:
        pass
    else:
        print('Não há produtos inseridos para dar a valor total!')


#######################################################
while True:
    print('-=' * 33)
    print('#' * 33)
    print('# 1 - Listar Produtos           #')
    print('# 2 - Inserir Produtos          #')
    print('# 3 - Pesquisar por Código      #')
    print('# 4 - Excluir Produto           #')
    print('# 5 - Alterar Produto           #')
    print('# 6 - Valor Total dos Produtos  #')
    print('# 7 - Quantidade de Produtos    #')
    print('# 0 - SAIR                      #')
    print('#' * 33)

    opcao = int(input('Informe uma opção: '))

    if opcao == 1:
        listar_produtos()
    elif opcao == 2:
        inserir_produtos()
    elif opcao == 3:
        buscar_por_codigo()
    elif opcao == 4:
        excluir_produto()
    elif opcao == 5:
        alterar_produto()
    elif opcao == 6:
        valor_total_produtos()
    elif opcao == 7:
        quantidade_produtos()
    elif opcao == 0:
        print('Obrigado por usar nosso programa!')
        break
    else:
        print('Opção Ínvalida!')








# TODO: Problema 2








# TODO: Problema 3