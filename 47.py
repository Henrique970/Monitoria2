# TODO: Dada uma lista de IPs v4, salve todos os ipsválidos em um arquivo chamado ips_validos.txt
#  se for inválido escreva em ips_invalidos.txt.


ips = [
    '192.168.2.342',
    '10.11.12.1',
    '10.11.12.45',
    '100.110.12.134',
    '99.11.12.1344',
    '100.121.112.134',
    '254.200.12.134',
    '220.0.12.134',
    '120.11.12.134',
    '145.11.12.134',
    '145.11.12.134',
    '100.255.45.1',
    '10.1167.12.134',
]

# Ips válidos vão de 1 a 254
#split separa pelo elemento indicado


for ip in ips:
    for str_ip in ip.split('.'):
        if int(str_ip) in range(1):
            print('Válido!')
        else:
            print('Iválido!')

# with open('validos.txt', 'w') as ips_validos:
#     ips_validos.write('10.11.12.1')
