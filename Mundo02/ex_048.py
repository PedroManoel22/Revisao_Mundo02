quantidade = 0
soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        quantidade += 1
        soma += i
print(f'A soma dos {quantidade} números é {soma}')
