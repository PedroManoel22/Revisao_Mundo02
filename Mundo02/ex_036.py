valor_casa = float(input('Insira o valor da casa requerida: '))
salario = float(input('Insira seu salario: '))
anos = int(input('Insira em quantos anos você irá pagar por essa casa: '))
prestacao_mensal = valor_casa / (anos * 12) 
trita_porcento_salario = salario * 0.3
print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos a prestação será de R${prestacao_mensal:.2f}')
if prestacao_mensal > trita_porcento_salario:
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')
