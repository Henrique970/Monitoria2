# Strings é dado em aspas ''

# A string não pega por quantidade de elementos e sim
# os caracteres do nome do elemento

# upper deixa as strings maiúsculas

# lower deixa as strings menúsculas

strings = 'henrique'

def is_vogal(nome):
    lista = []
    for letra in nome:
        if letra not in 'aeiou':
            lista.append(letra)
    return lista

print(is_vogal(strings))