def nao_tem_nada_a_ver_com_piramide(numero):
    for i in range(1, numero+1):
        if numero == i:
            print(f'{numero} ' * i, end="")

nao_tem_nada_a_ver_com_piramide(3)
