from time import sleep
primeiro_valor = int(input('Primeiro valor: '))
segundo_valor = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print(f'A soma entre {primeiro_valor} e {segundo_valor} é {primeiro_valor + segundo_valor}')
        print('=-==' * 10)
    elif opcao == 2:
        print(f'A multiplicação entre {primeiro_valor} e {segundo_valor} é {primeiro_valor * segundo_valor}')
        print('=-==' * 10)
    elif opcao == 3:
        if primeiro_valor > segundo_valor:
            print(f'O maior valor é {primeiro_valor}')
        else:
            print(f'O maior valor é {segundo_valor}')
        print('=-==' * 10)
    elif opcao == 4:
        primeiro_valor = int(input('Primeiro valor: '))
        segundo_valor = int(input('Segundo valor: '))
        print('=-==' * 10)
    sleep(1)
print('Obrigado. Volte sempre!')
