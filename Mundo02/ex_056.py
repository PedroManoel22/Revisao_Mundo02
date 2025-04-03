soma_idades = 0      
soma_mulheres_20 = 0
for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    soma_idades += idade
    if i == 1 and sexo in 'mM':
        maior = idade
        maior_homem = nome
    if sexo in 'mM' and idade > maior:
        maior = idade
        maior_homem = nome
    if sexo in 'Ff' and idade < 20:
        soma_mulheres_20 += 1
media_idades = soma_idades / 4
print(f'A média de idade do grupo foi é de {media_idades:.1f}')
print(f'o homem mais velho tem {maior} anos e se chama {maior_homem}.')
print(f'Ao todo são {soma_mulheres_20} mulheres com menos de 20 anos!')
