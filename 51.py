frase = 'Hoje o dia esta muito quente,\n' \
        'mais aqui dentro esta muito gelado \n' \
        'os computadores sao organizados para os \n' \
        'PMs w nao para os alunos. :-( '

def adcionar_arquivo():
    with open('monitoria.txt', 'r') as arquivo:
        return arquivo.read().count('d')
print(adcionar_arquivo())
