# Para adicionar um elemento a uma pasta txt você
# primeiramente vai abrir usando open(), depois vai
# adcionar algum elemento usando o write() e depois
# fechando usando close()

# Usando o método do "w" você cria ou substitui o que tem
# na pasta, usando o "a" você poderá adcionar um elemento
# sem fazer nenhuma mudança no que ja existe na pasta e
# usando o "r" você vai ler o que tem na pasta.

# usando o readline() você vai especificar que quer ler só
# uma linha e se usar somento o read() ele vai ler
# completamente a pasta

arquivo = open('pasta.txt', 'w')
arquivo.write('Deus e fiel')
arquivo.close()

arquivo = open('pasta.txt', 'a')
arquivo.write(' e generoso')
arquivo.close()

arquivo = open('pasta.txt', 'r')
quant = arquivo.readline().count('e')
arquivo.close()
print(quant)

arquivo = open('pasta.txt', 'r')
quant = arquivo.read().count('e')
arquivo.close()
print(quant)

