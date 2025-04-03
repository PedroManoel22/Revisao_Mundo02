from datetime import date
ano_atual_maquina = date.today().year
soma_menor = 0
soma_maior = 0
for i in range(1, 8):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {i}° pessoa: '))
    idade = ano_atual_maquina - ano_nascimento
    if idade < 18:
        soma_menor += 1 
    else:
        soma_maior += 1
print(f'Ao todo teve {soma_maior} maiores de idade!')
print(f'E também tivemos {soma_menor} menores de idade!') 
