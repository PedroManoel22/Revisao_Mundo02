print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
termos = int(input('Informe quantos termos da sequencia você quer que eu lhe mostre: '))
p0 = 0
p1 = 1
cont = 3
print('~' * 30)
print(f'{p0} -> {p1}', end='')
while cont <= termos:
    p2 = p0 + p1
    print(f' -> {p2}', end='')
    p0 = p1
    p1 = p2
    cont += 1
print(' -> Acabou')
