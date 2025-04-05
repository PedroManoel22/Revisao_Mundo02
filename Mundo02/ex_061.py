primeiro_termo = int(input('Primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))
print(f'{primeiro_termo} ->', end='')
cont = 0
pa = primeiro_termo
while cont < 9:
    pa += razao 
    cont += 1
    print(f' {pa} ->', end='')
print(' Acabou', end='')
