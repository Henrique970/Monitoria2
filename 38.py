# TODO: Preciso criar uma função para retornar a quantidade de cada  uma das vogais em uma palavra

# def cont_vogal(nome):
#     a = 0
#     e = 0
#     i = 0
#     o = 0
#     u = 0
#     for letra in nome:
#         if letra in 'a':
#             a += 1
#         elif letra in 'e':
#             e += 1
#         elif letra in 'i':
#             i += 1
#         elif letra in 'o':
#             o += 1
#         elif letra in 'u':
#             u += 1
#         A = 'a =',a
#         E = 'e =',e
#         I = 'i =',i
#         O = 'o =',o
#         U = 'u =',u
#     return A, E, I, O, U
# print(cont_vogal('otorrinolaringologista'))


############################# certo abaixo ########################

def quant_vogais(palavra):
  letras = 'a', 'e', 'i', 'o', 'u'
  for l in palavra:
    if l in letras:
      l*=2
  return l

print(quant_vogais("otorrinolaringologista"))
