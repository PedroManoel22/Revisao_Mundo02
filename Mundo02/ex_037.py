num = int(input('Insira um número inteiro: '))
print('Escolha uma das bases para conversão:\n[1] converter para BINÁRIO\n[2] converter para OCTAL\n[3] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'O número {num} em binário é {bin(num)[2:]}')
if opcao == 2:
    print(f'O número {num} em octal é {oct(num)[2:]}')
if opcao == 3:
    print(f'O número {num} em hexadecimal é {hex(num)[2:]}')
