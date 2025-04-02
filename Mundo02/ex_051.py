print('=' * 30)
print('     10 termos de uma PA')
print('=' * 30)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_termo + (10 - 1) * razao
for i in range(primeiro_termo, decimo + razao, razao):
    print(f'{i} ->', end= ' ')
print('Acabou')
