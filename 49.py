"""Cifra de Cesar"""
# O chr ele procura vai buscar um elemento a partir de um número
# O ord ele vai buscar o número a partir do elemento


def cifrando(palavra, deslocamento):
    lista = []
    for letra in palavra:
        lista.append(chr(ord(letra) + deslocamento))
    palavra_cifrada = "".join(lista)
    return palavra_cifrada
palavra_input = input('Informe a palavra ou frase que deseja cifrar: ')
deslocamento_input = int(input('Informe o deslocamento da cifra: '))


def decifrando(palavra, deslocamento):
    lista = []
    for letra in palavra:
        lista.append(chr(ord(letra) - deslocamento))
    palavra_cifrada = "".join(lista)
    return palavra_cifrada

def run():
    cifra = cifrando(palavra_input, deslocamento_input)
    decifra = decifrando(cifra, deslocamento_input)

    print('Palavra cifrada:')
    print(cifra)
    print('Palavra decifrada:')
    print(decifra)
run()