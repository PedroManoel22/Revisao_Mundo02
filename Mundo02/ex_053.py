frase = str(input('Insira sua frase: ')).upper().strip().replace(' ', '')
frase_invertida = ''.join(reversed(frase))
print(f'O inverso de {frase} é {frase_invertida}')
if frase == frase_invertida:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo! ')
