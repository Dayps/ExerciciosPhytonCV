print('=== Desafio 12 ===\n')

p = float(input('Digite o valor do produto: R$'))
desconto = (p*5)/100
valorf = p - desconto
print('- -'*15)
print(f'Parabéns, você ganhou 5% de desconto!! \nO valor do produto com 5% de desconto é R${valorf:.2f} \nAproveite!')