# TODO: Preciso inserir em uma lista todas as vogais presentes em nome.

# mostra vogal
def is_vogal(nome):
    lista = []
    for letra in nome:
        if letra in 'aeiou':
            lista.append(letra)
    return lista
print(is_vogal('strings'))
# só consoante
def is_consoante(nome):
    lista = []
    for letra in nome:
        if letra not in 'aeiou':
            lista.append(letra)
    return lista
print(is_consoante('otorrinolaringologista'))