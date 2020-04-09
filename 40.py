print('vogais duplicadas')
def vogais_duplicadas(nome):
    lista = []
    texto_lista = ''
    for letra in nome:
        if letra in 'aeiou':
            lista.append(letra*2)
        else:
            lista.append(letra)
        texto_lista = ''.join(lista)
    return texto_lista
print(vogais_duplicadas('henrique:'))
print('')
###########################################################
print('vogais maiuscolas:')
def vogais_maiuscolas(nome):
    lista = []
    texto_lista = ''
    for letra in nome:
        if letra in 'aeiou':
            lista.append(letra.upper())
        else:
            lista.append(letra)
        texto_lista = ''.join(lista)
    return texto_lista
print(vogais_maiuscolas('henrique'))
print('')
##############################################################
