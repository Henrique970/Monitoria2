texto = 'O python e 42'
# o "w" ele coloca e modifica
arquivo = open('text.txt', 'w')
arquivo.write(texto)
arquivo.close()

texto = 'O python e 42'
# o "a" ele da um append
arquivo = open('text.txt', 'w')
arquivo.write(texto)
arquivo.close()
