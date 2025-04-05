primeiro_termo = int(input('Primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))
print(f'{primeiro_termo} ->', end='')
cont = 0
pa = primeiro_termo
cont2 = 0
while cont < 9:
    pa += razao 
    cont += 1
    print(f' {pa} ->', end='')
print(' Pausa', end='')
print()
a_mais = int(input('Quantos termos você quer mostrar a mais ? '))
soma = 10 + a_mais
pa2 = pa
soma2 = 0
while a_mais != 0:
    while cont2 < a_mais:
        pa2 += razao
        cont2 += 1
        print(f'{pa2} -> ', end='')
    print(' Pausa', end='')
    print()
    cont2 = 0
    a_mais = int(input('Quantos termos você quer mostrar a mais ? '))
    soma2 += a_mais
print(f'Progressão finalizada com {soma + soma2} termos mostrados.')
