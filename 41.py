# TODO: Faça uma funçao que retorne todas as vogais
#  duplicadas.

def duplicar_vogais(palavra):
    lista = []
    texto_lista = ''
    for letra in palavra:
        if letra in 'aeiou':
            lista.append(letra*2)
        else:
            lista.append(letra)
        texto_lista = ''.join(lista)
    return texto_lista
print(duplicar_vogais('eu sou programador'))


# TODO: Faça uma funçao que retorne todas as vogais
#  maiusculas.

def vogais_maiusculas(palavra):
    lista = []
    texto_lista = ''
    for letra in palavra:
        if letra in 'aeiou':
            lista.append(letra.upper())
        else:
            lista.append(letra)
        texto_lista = ''.join(lista)
    return texto_lista
print(vogais_maiusculas('eu sou programador'))