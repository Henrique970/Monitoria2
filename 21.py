contatos = {'nome': 'juju', 'telefone': '99252348'}
contatos2 = {'nome': 'didi', 'telefone': '99455460'}


print(contatos.keys())
print(contatos.values())

for c in contatos.items():
    print(c)

# nunca passe  indíce e sim passe a chave ou seja o nome da chave.
print(contatos['nome'])
print(contatos['telefone'])

# adicionar valores
contatos['email'] =  'jujugatinhos.net'

print(contatos)

contatos['tipo_saguinio'] = 'o'

contatos['RG'] = '-'
print(contatos)

agenda = []

agenda.append(contatos)
agenda.append(contatos2)
print(agenda)

for contato in agenda:
    print(contato)


