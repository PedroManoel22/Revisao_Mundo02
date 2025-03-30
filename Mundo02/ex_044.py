print('========== LOJAS DO PEDRÃO ==========')
valor = float(input('Insira o valor total da sua compra: R$'))
print('=====================================')
print('Qual será sua forma de pagamento:\n[1] Á vista dinheiro/cheque\n[2] Á vista no cartão\n[3] Em até 2x no cartão\n[4] 3x ou mais no cartão')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'Você selecionou a forma de pagamento: Á vista dinheiro/cheque e o valor final de sua compra ficou = R${valor - (valor * 0.1)}')
elif opcao == 2:
    print(f'Você selecionou a forma de pagamento: Á vista no cartão e o valor final de sua compra ficou = R${valor - (valor * 0.05)}')
elif opcao == 3:
    print(f'Você selecionou a forma de pagamento: 2x no cartão e o valor final de sua compra ficou = {valor}  em 2x de {valor/2}')
else:
    parcelas = int(input('Quantas parcelas? '))
    valor_parcelas = (valor + (valor * 0.2)) / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R${valor_parcelas:.2f} com juros')
    print(f'Sua compra de R${valor} vai custar R${valor + (valor * 0.2)} no final')
