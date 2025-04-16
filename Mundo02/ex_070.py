total = mais = menor = 0
nome = str
print('-=' * 10)
print('LOJA DO PEDRÃO')
print('-=' * 10)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    total += preco
    menor = preco
    if preco < menor:
        menor = preco
        nome = produto
    if preco > 1000:
        mais += 1
    if continuar == 'N':
        break
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {mais} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome} que custa R${menor:.2f}')
