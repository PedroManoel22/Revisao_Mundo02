print('=' * 20)
print(f'{"":^3}', end="")
print('BANCO ROUBA TU')
print('=' * 20)
valor = int(input('Qual valor deseja sacar ? '))
total = valor 
ced = 50
total_ced = 0
while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break
print('=' * 20)
print('Volte sempre ao BANCO ROUBA TU!, tenha um bom dia!')
