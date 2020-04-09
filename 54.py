
def sum_num_impares(*args):
    soma = 0
    for a in args:
        if a % 2 == 1:
            soma += a
    return soma

assert sum_num_impares(1,2,3,4,5,6,7,8,9,10) == 25
# assert sum_num_impares(200) == 40000
# assert sum_num_impares(300) == 90300