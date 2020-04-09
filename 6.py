def piramide(numero):
    for contador in range(1, numero + 1):
        for repetidor in range(contador + 1):
            if repetidor == contador:
                print(f'{repetidor}  ' * contador)


piramide(9)