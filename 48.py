# TODO: Dado o texto.txt. Crie uma função que retorne a quantidade de ocorrências da palavra "and"

def contagem_de_palavra(arquivo, palavra):
    with open(arquivo) as quant:
        return quant.read().count(palavra)
    #     ocorrencias = quant.read().count(palavra)
    # return ocorrencias


print(contagem_de_palavra('texto.txt', 'and '))
