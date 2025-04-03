for i in range(1, 6):
    peso = float(input(f'Insira o peso da {i}ª pessoa: '))
    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        elif peso > maior:
            maior = peso
print(f'O menor peso foi {menor}')
print(f'O maior peso foi {maior}')
