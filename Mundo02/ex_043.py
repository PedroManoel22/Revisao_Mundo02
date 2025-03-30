peso = float(input('Insira seu peso (Kg): '))
altura = float(input('Insira sua altura (M): '))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f'Seu IMC é igual a {imc:.2F}, e sua classificação é ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é igual a {imc:.2F}, e sua classificação é PESO IDEAL!')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é igual a {imc:.2F}, e sua classificação é SOBREPESO!')
elif imc >= 30 and imc <= 40:
    print(f'Seu IMC é igual a {imc:.2F}, e sua classificação é OBESIDADE!')
else:
    print(f'Seu IMC é igual a {imc:.2F}, e sua classificação é OBESIDADE MÓRBIDA!')
