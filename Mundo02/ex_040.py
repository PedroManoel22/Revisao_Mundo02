n1 = float(input('Insira a primeira nota: '))
n2 = float(input('insira a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('O aluno foi REPROVADO!')
elif media >=5 and media <= 6.9:
    print('O aluno está em RECUPERAÇÃO!')
elif media >= 7:
    print('O aluno está APROVADO!')
