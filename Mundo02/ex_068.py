from random import randint
print('-=' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
soma = 0
ganhou = 0
while True:
    print('-=' * 15)
    valor = int(input('Diga um valor: '))
    par_impar = str(input('Par ou ímpar? [P/I]: ')).upper().strip()[0]
    computador = randint(1, 11)
    soma = computador + valor
    print('-' * 30)
    if par_impar == 'P' and soma %  2 == 0:
        print(f'Você jogou {valor} e o computador {computador}. Total de {soma} DEU PAR!')
        print('Você venceu!')
        ganhou += 1
        print('Vamos jogar novamente....')
    if par_impar == 'P' and soma %  2 != 0:
        print(f'Você jogou {valor} e o computador {computador}. Total de {soma} DEU ÍMPAR!')
        print('Você perdeu!')
        break
    if par_impar == 'I' and soma %  2 == 0:
        print(f'Você jogou {valor} e o computador {computador}. Total de {soma} DEU PAR!')
        print('Você perdeu!')
        break
    if par_impar == 'I' and soma %  2 != 0:
        print(f'Você jogou {valor} e o computador {computador}. Total de {soma} DEU ÍMPAR!')
        print('Você ganhou!')
        print('Vamos jogar novamente....')
        ganhou += 1
print(f'Gamer Over! Você venceu {ganhou} vezes.')
