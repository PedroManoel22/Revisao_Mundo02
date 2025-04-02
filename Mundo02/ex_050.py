soma = 0
for i in range(1, 7):
    numero = int(input(f'insira o {i}° número:'))
    if numero % 2 == 0:
        soma += numero
print(f'A soma dos números pares é {soma}')
