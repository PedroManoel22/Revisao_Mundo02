from random import randint
tentativas = 1
print('Olá, sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
palpite = int(input('Qual é o seu palpite? '))
jogada_computador = randint(0, 10)
while palpite != jogada_computador:
    tentativas += 1
    if palpite < jogada_computador:
        print('Mais... Tente mais uma vez.')
        palpite = int(input('Qual é o seu palpite? '))
    elif palpite > jogada_computador:
        print('Menos... Tente mais uma vez.')
        palpite = int(input('Qual é o seu palpite? '))
print(f'Acertou com {tentativas} tentativas. Parabéns!')
