from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('Qual é o seu ano de nascimento? '))
idade = ano_atual - ano_nascimento
print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}')
if idade < 18:
    print(f'Você ainda tem {18 - idade} ano/s para se alistar!')
    print(f'Seu alistamento será em {ano_atual + (18 - idade)}.')
elif idade == 18:
    print('Você deverá se alistar IMEDIATAMENTE!')
else:
    print(f'Você passou {idade - 18} ano/s para o alistamento!')
    print(f'Seu alistamento deveria ter sido em {ano_atual - (idade - 18)}')
