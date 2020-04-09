#TODO: 1 Crie uma função que recebe um argumento como um número e se for maior 0 é
# True se não é False.

def maior_que_0(numero):
    resultado = False
    if numero > 0:
        resultado = True
    else:
        resultado = False
    return resultado

print('1°)')
print('')
print(maior_que_0(-1))
print('-=' * 10)

#TODO: 2 Crie um função que receba um número como argumento e imprima todos
# impares os antecessores dele.

def antecessor_impar(numero):
    while numero >= 0:
        if numero % 2 == 1:
            print(numero)
        numero -= 1

print('2°)')
print('')
antecessor_impar(10)
print('-=' * 10)

#TODO: 3 Crie uma função que recebe um argumento como um número e se ele
# for primo é true se não é false.

def is_primo(numero):
    n = numero
    quatodade_divisores = 0
    resolucao = False
    while n >= 1:
        if numero % n == 0:
            quatodade_divisores += 1
        n -= 1
    return quatodade_divisores <= 2

print('3°)')
print('')
print(is_primo(7))
print('-=' * 10)

# TODO: 4 Crie uma função que recebe um valor e um percentual de desconto
#  e retorne o valor final menos esse desconto.

def desconto(valor, desconto):
    desconto = valor - (valor*desconto/100)
    return desconto

print('4°)')
print('')
print(desconto(100, 5))