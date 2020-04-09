# Argumentos ou parâmetros

def calcula_area_quadrado(lado):
    return lado ** 2

def calcula_area_retangulo(base,altura):
    return base * altura

def calcula_distancia(velocidade, tempo):
    return velocidade * tempo

def is_par(numero):
    resultado = False
    if numero % 2 == 0:
        resultado = True
    else:
        resultado = False
    return resultado

def is_impar(numero):
    resultado = False
    if numero % 2 == 0:
        resultado = False
    else:
        resultado = True
    return resultado

print(calcula_area_quadrado(12))
print('-=' * 10)

print(calcula_area_retangulo(10, 10))
print('-=' * 10)

print(calcula_distancia(100, 6))
print('-=' * 10)

print(is_par(8))
print('-=' * 10)

print(is_impar(8))
