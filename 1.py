def calcula_idade():
    ano_nascimento = int(input('Informe a data de nascimento: '))
    ano_atual = 2019
    return ano_atual - ano_nascimento
idade = calcula_idade()

print(idade,'anos')

