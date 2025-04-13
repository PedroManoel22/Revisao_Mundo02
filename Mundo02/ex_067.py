while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 15)
    if tabuada <= 0:
        break
    for i in range(1, 11):
        print(f'{tabuada} x {i} = {tabuada * i}')
    print('-' * 15)
print('Programa encerrado com sucesso. Volte Sempre!')
