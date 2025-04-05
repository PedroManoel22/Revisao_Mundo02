soma = 0
soma_todos = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        soma +=1
        soma_todos += num
    elif num == 999:
        break
print(f'Você digitou {soma} números e a soma entre eles foi {soma_todos}.')
