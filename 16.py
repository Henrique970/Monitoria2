lista = [2, 5, 5, 8, 2, 5, 5, 8]

# Fatiar os elementos da lista.
print(lista[2:5])
print(lista[:5])
print(lista[2:])
print(lista[2:122546])

# Inverte a ordem da lista.
print('Invertido')
print(lista[::-1])
print(lista[5:2:-1])

lista.reverse()
print(lista)

# Colocar em ordem crescente ou descrecente
lista.sort(reverse=False)
print(lista)
