# A lista ela indexa os elementos a partir do zero, ou seja ela aloca naquele
# indereço

idades = [3, 40, 68, 45]

print(idades[0])
print(idades[1])
print(idades[2])
print(idades[3])
print(len(idades))
print('#' * 30)
nomes = ['Henrique', 'Jéssica', 'Rulieu', 'Isáias']

print(nomes[0])
print('#' * 30)
print(len(nomes))

for i in range(len(idades)):
    print(i)
print('#' * 30)
for a in range(len(nomes)):
    print(a)
print('#' * 30)
for ii in range(len(idades)):
    print(idades[ii])
print('#' * 30)
for aa in range(len(idades)):
    print(idades[aa])