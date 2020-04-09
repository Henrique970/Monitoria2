notas = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

cifras = notas

notas = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']

print(notas[0], cifras[0])
print(notas[1], cifras[1])
print(notas[2], cifras[2])
print(notas[3], cifras[3])
print(notas[4], cifras[4])
print(notas[5], cifras[5])
print(notas[6], cifras[6])

print('#' * 20)

for i in range(len(cifras)):
    print(cifras[i], notas[i])


