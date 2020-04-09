# TODO: Preciso criar uma string em canel case apartir de uma outra string.

def camel_case(texto):
    camel = []
    texto_camel = ""
    for i, l in enumerate(texto):
        if i % 2 != 0:
            camel.append(texto[i].upper())
        else:
            camel.append(texto[i])
            # join transformou a lista em uma string como o format.
    texto_camel = ",".join(camel)
    return texto_camel


print(camel_case('otorrinolaringologista'))