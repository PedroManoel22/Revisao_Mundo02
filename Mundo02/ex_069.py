maior_idade = total_h = mulheres_menos20 = 0
while True:
    print('-' * 22)
    print('cadastre uma pessoa')
    print('-' * 22)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('-' * 22)
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if idade > 18:
        maior_idade += 1
    if sexo == 'M':
        total_h += 1
    if  sexo == 'F' and idade < 20:
        mulheres_menos20 += 1
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior_idade}')
print(f'Ao todo temos {total_h} homens cadastrados')
print(f'E temos {mulheres_menos20} mulheres com menos de 20 anos')
