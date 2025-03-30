print('-=' * 30)
print('Analisador de Triângulos')
print('-=' * 30)
s1 = float(input('Primeiro segmento:'))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 == s2 == s3:
    tipo = 'equilátero'
elif s1 != s2 != s3 != s1:
    tipo = 'Escaleno'
else:
    tipo = 'Isósceles'
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s2 + s1:
    print(f'Os segmentos acima PODEM FORMAR UM TRIÂNGULO {tipo}')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO!')
