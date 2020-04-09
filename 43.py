# Todas as questões devem ser com funções

# TODO: Dada a string, imprima essa string inteira em maiúscuça
#  exemplo: 'python'-> PYTHON.(1 scores)

# def maiuscula(string):
#     return string.upper()
# print(maiuscula('python'))

# TODO: Dada uma string, retorne um booleano que indique se
#  ela é ou não um número
#  exemplo '1234' -> True, 'a12' -> False.(1 scores)

# def is_number(string):
#     return string.isnumeric()
# print(is_number('a12'))

# TODO: Dada uma string, retorne a string invertida.
#  exemplo: 'asdf' -> 'fdsa'. (3 scores)

# def inverter_string(string):
#     return string[::-1]
# print(inverter_string('asdf'))

# TODO: Dada string, itere cada uma das letras
#   da string e as imprima.(2 scores)

# def letras_da_palavra(string):
#     for i, letra in enumerate(string):
#         print(letra)
# letras_da_palavra('Henrique')

# TODO: A Donuts. Dada uma contagem de inteiros de um
#   números de donuts, retornar uma string do
#   formulário "Número de dunots: <contagem>"
#   onde <contagem> é o número passado.
#   no entanto, se a contagem for 10 ou mais, então
#   use a palavra 'muitos' ao invés da contagem real.
#   então dunots(5) retorna "Números de donats: 5"
#   e dunots(23) retorna "Número de donats: Muitos".
#   (2 scores)

# def quant_donats(numero):
#     if numero < 10:
#         return f"Números de donats: {numero}"
#     else:
#         return "Número de donats: Muitos"
# print(quant_donats(5))

# TODO: Dada uma string s, retorna uma string feita dos
#   primeiros 2 ne os ultimós 2 caracteres da cadeia original,
#   é maior que 2, retorna a string vazia. (3 scores)

# def retornar_caracteres(s):
#     if len(s) <= 2:
#         return ""
#     else:
#         return s[:2:] + s[-2::]
# print(retornar_caracteres('flamengo'))

# TODO: Dada uma lista de nomes, retorne uma lista com todos
#   nomes em ordem alfabética com a inicial maúiscula.

# def ordem_nomes(pessoas):
#     nova_lista = []
#     for pessoa in pessoas:
#         nova_lista.append(pessoa.capitalize())
#     nova_lista.sort()
#     return nova_lista
# print(ordem_nomes(['maria', 'josé', 'antônio', 'pedro']))

# TODO: Dada a lista do problema anterior, insira o nome
#   na lista e a imprima.(1 score)

# pessoas = ['maria', 'josé', 'antônio', 'pedro']
#
# def adicionar_pessoas(nome):
#     pessoas.append(nome)
#     return pessoas
# print(adicionar_pessoas('raquel'))

# TODO: Dada uma string, retorne em um dicionario a
#   quantidade de cada uma das vogais contidas na string
#   Exemplo: 'adalamia' -> {'a': 4, 'e': 0, 'i': 1, 'o': 0
#   'u': 0}.(4 scores)

# def quantidade_letras(string):
#     dic = {}
#     for s in string:
#         if s in 'aeiou':
#             dic[s] = string.count(s)
#     return f'{string} -> {dic}'
# print(quantidade_letras('onintorrinco'))

# Google
# TODO: C.fix_start
#   Dada uma string s, retornar uma string onde todas as
#   ocorrências do seu primeiro caractere seja
#   alterado para "*", não alterar o primeiro char em si
#   por exemplos, "babble" rende ba**le",
#   "google" rende "goo*le". Supanha que a corda é de compo