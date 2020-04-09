# TODO: Criar uma função que receba como argumento um número e retorne uma lista com todos os pares até o 0

# TODO: Criar uma função que receba como argumento um número e retorne uma lista com todos os impares até o 0

def is_par(numero):
    return list(range(0, numero, 2))


def is_impar(numero):
    if numero % 2 == 0:
        impar = list(range(numero, 0-1, -1))

print(is_par(5))