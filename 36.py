import random
produtos = []

###################################################
#1
def listar_produtos():
    if len(produtos) > 0:
        for i, lista in enumerate(produtos):
            print(lista)
    else:
        print('Não existe produtos para serem listados!')

#############################################################
#2
def cadastrar_produtos():
    codigo = random.randint(1000,9999)
    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do protudo: '))
    desconto = float(input('Informe o deconto do produto: '))
    produtos.append({'Código':codigo,'Nome':nome,
                     'Preço': preco, 'Desconto':desconto})
    print('Produto cadastrado com sucesso!')

#############################################################
#3
def pesquisar_codigo():
    if len(produtos) > 0:
        busca = int(input('Informe o código para realizar a busca: '))
        for p in produtos:
            if p['Código'] == busca:
                print(p)
            if busca is p['Código']:
                print('Não existe produtos com esse código!')
    else:
        print('Não existe produtos para serem pesquisados!')

#############################################################
#4
def excluir_produtos():
    if len(produtos) > 0:
        busca = int(input('Informe o código do produto para ser excluído: '))
        for p in produtos:
            if p['Código'] == busca:
                del p
                print('Produto excluido com sucesso!')
            else:
                print('Não existe produto para ser excluído!')
    else:
        print('Não existe produtos para serem excluídos!')

##############################################################
#5
def alterar_produto():
    if len(produtos) > 0:
        busca = int(input('Informe o código do produto para alterar: '))
        print('O código do produto não pode ser alterado!')
        for p in produtos:
            if p['Código'] == busca:
                novo_nome = input('Informe o novo nome do produto: ')
                novo_preco = float(input('Informe o novo preço do protudo: '))
                novo_desconto = float(input('Informe o novo deconto do produto: '))
                p['Nome'] = novo_nome
                p['Preço'] = novo_preco
                p['Desconto'] = novo_desconto
                print('Produto alterado com sucesso!')
            else:
                print('Não existe produto com esse código!')
    else:
        print('Não existem produtos para serem alterados!')

##############################################################
#6
def valor_total():
    if len(produtos) > 0:
        for p in produtos:
            soma = p['Preço'] * (p['Desconto'] / 100)
            print(p['Nome'],soma)
    else:
        print('Não existem produtos para mostrar o valor total!')

###############################################################
#7
def quantidade_produtos():
    if len(produtos) > 0:
        print('A quantidade de produtos contidos na lista é',len(produtos))
    else:
        print('Não existem produtos para mostrar a quantidade total!')

while True:
    print('###############################################')
    print('# 1 - Listar Produtos                         #')
    print('# 2 - Cadastra Produtos                       #')
    print('# 3 - Pesquisar pelo código                   #')
    print('# 4 - Excluir Produto                         #')
    print('# 5 - Alterar Produto                         #')
    print('# 6 - Valor Total dos Produtos                #')
    print('# 7 - Quantidade de Produtos na Lista         #')
    print('# 8 - SAIR do sistema                         #')
    print('###############################################')
    op = int(input('Informe uma opção: '))

    if op == 1:
        listar_produtos()
    elif op == 2:
        cadastrar_produtos()
    elif op == 3:
        pesquisar_codigo()
    elif op == 4:
        excluir_produtos()
    elif op == 5:
        alterar_produto()
    elif op == 6:
        valor_total()
    elif op == 7:
        quantidade_produtos()
    elif op == 8:
        break
    else:
        print('Opção Inválida!')

# fracielsousarego@gmail.com