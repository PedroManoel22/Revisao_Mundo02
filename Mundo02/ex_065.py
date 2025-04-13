total = 0
soma = 0
while True:
    num = int(input('Dgite um número: '))
    opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    soma += num
    total += 1
    if total == 1:
        menor = num
        maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    if opcao == 'N':
        break
media = soma / total
print(f'Você digitou {total} números e a média foi {media:.2f}')
print(f'O maior número foi {maior} e o menor foi {menor}')
