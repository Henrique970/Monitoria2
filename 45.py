# Emulando a cifra de cezar

# TODO: Criar uma função para descirptografar um texto do arquivo criptografado.txt para outro arquivo

def ler_arquivo(arquivo):
    #se pronuncia uaf
    with open(arquivo, 'r') as arg:
        #readline vai ler a linha
        return arg.readline()



def escreve_arquivo(texto, arquivo):
    with open(arquivo, 'w') as arg:
        arg.write(texto)


def encripta(palavra, deslocamento):
    lista = []
    for l in palavra:
        lista.append(chr(ord(l) + deslocamento))
    texto_criptografado = "".join(lista)
    escreve_arquivo(texto_criptografado, 'criptografado.txt')
    return texto_criptografado


def decripta(palavra, deslocamento):
    lista = []
    for l in palavra:
        lista.append(chr(ord(l) - deslocamento))
    texto_decriptografado = "".join(lista)
    escreve_arquivo(texto_decriptografado, 'decriptografado.txt')
    return texto_decriptografado


def run():
    nome = input('Informe o nome que você deseja cifrar: ')
    deslocamento = int(input('Informe o deslocamento da cifra: '))
    cifrana = encripta(nome, deslocamento)
    descifra = decripta(cifrana, deslocamento)
    print(f'O nome que você escolheu "{descifra}"')
    print(f'E ele foi criptografado parar "{cifrana}"')
    linha = ler_arquivo('criptografado.txt')
    linha_decifrada = descifra(linha, deslocamento)
    escreve_arquivo(linha_decifrada, 'decriptografado.txt')



run()
