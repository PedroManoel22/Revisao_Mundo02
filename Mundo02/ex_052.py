num = int(input('Insira um número inteiro: '))
soma = 0
for i in range(1, num + 1):
    if num % i == 0:
        print(f'\033[32m{i}\033[m', end= ' ')
        soma += 1
    else:
        print(f'\033[31m{i}\033[m', end= ' ')
print()
print(f'O número {num} foi divisivel {soma} vezes')
if soma > 2:
    print('E por isso ele NÃO É PRIMO')
elif soma == 2:
    print('E por isso ele É PRIMO')
    