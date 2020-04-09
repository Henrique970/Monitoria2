def duplicar_volgais(*args):
    lista = []
    for nome in args:
        for letra in nome:
            if letra in 'aeiouAEIOU':
                lista.append(letra * 2)
            else:
                lista.append(letra)
    return "".join(lista)


assert duplicar_volgais('Anjo') == 'AAnjoo'