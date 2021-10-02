print('=== Desafio ===')

s = float(input('Qual o salário do funcionário: R$'))
aumento = (s*15)/100
sfinal = s + aumento
print(f'O salario de R${s:.2f} com aumento de 15% ficará atualmente R${sfinal:.2f}')