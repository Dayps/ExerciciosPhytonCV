import math
print('=== Desafio 17 ===')
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(co, ca)
print(f'O valor da hipotenusa é {hipotenusa:.2f}')