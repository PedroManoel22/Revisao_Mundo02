from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA''')
jogador = int(input('Qual é sua opção? '))
print('-=' * 15)
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
print('-=' * 15)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    if jogador == 1:
        print('O jogador venceu!')
    elif jogador == 2:
        print('O computador venceu!')
    else:
        print('Jogada inválida!')
elif computador == 1:
    if jogador == 0:
        print('O computador venceu!')
    if jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('O jogador venceu!')
    else:
        print('Jogada inválida!')
elif computador == 2:
    if jogador == 0:
        print('O jogador venceu!')
    if jogador == 1:
        print('O computador venceu!')  
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida!')
