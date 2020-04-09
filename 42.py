# TODO: Dada uma string, imprima essa string inteira em maiuscula
#   exemplo: 'python' -> 'PYTHON. (1 scores)

# def maiuscula(string):
#     return string.upper()
# print(maiuscula('python'))

# TODO: Dada uma string, retorne um booleano que indique se ela é ou não um número.
#   exemplo: '1243' -> True, 'a12' -> False. (1 scores)

# def is_number(valor):
#     return valor.isnumeric()
# print(is_number('a12'))

# TODO: Dada ums string, retorne a string invertida.
#  Exemplo: 'asdf' -> 'fdsa' (3 scores)

# def inverter(string):
#     return string[::-1]
# print(inverter('asdf'))

# TODO: Dada uma string, itere cada uma das letras da string e as imprima.(2 scores)
# TODO olhar

# def cada_letra(strings):
#     for i, string in enumerate(strings):
#         return string
# print(cada_letra('henrique'))

# Google
# TODO: # A. Donuts. Dada uma contagem de inteiros de um número de donuts,
#  retornar uma string do formulário "Número de donuts: <contagem>',
#  onde <contagem> é o número passado.
#  No entanto, se a contagem for 10 ou mais, então use a palavra 'muitos'
#  ao invés da contagem real. Então donuts(5) retorna 'Número de donuts: 5'
#  e donuts(23) retorna 'Número de donuts: muitos'. (2 scores)

# def donuts(count):
#     resultado = 0
#     if count > 9:
#         resultado = 'muitos'
#     elif count < 10:
#         resultado = count
#     return 'Número de donuts:', resultado
# print(donuts(10))

# Google
# TODO: Dada uma string s, retorna uma string feita dos primeiros 2
#  e os últimos 2 caracteres da cadeia original,
#  por isso "speng" retorna "spng". No entanto, se o comprimento da string
#  é menor que 2, retorna a string vazia. (3 scores)
#ainda incompleto
# def both_ends(s):
#     resultado = ''
#     if len(s) < 2:
#         resultado = ''
#     else:
#         s[]

# TODO: Dada uma lista de nomes, retorne uma lista com todos os nomes
#   em ordem alfabetica e com a inicial maiuscula.
#   Exemplo: ['maria', 'pedro', antonio', 'josé'] ->
#   ['Antonio', 'José', 'Maria', 'Pedro'] (3 scores)

# def ordem_nomes(nomes):
#
# print(ordem_nomes(['maria', 'pedro', 'antonio', 'josé']))
