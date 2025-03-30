from datetime import date
nascimento = int(input('Qual o ano de nascimento do atleta: '))
ano_atual = date.today().year
idade = ano_atual - nascimento
if idade <= 9:
    classificacao = 'MIRIM'
elif idade <= 14:
    classificacao = 'INFANTIL'
elif idade <= 19:
    classificacao = 'JUNIOR'
elif idade <= 25:
    classificacao = 'SÊNIOR'
else:
    classificacao = 'MASTER'
print(f'O atleta tem {idade} anos\nClassificação: {classificacao}')
