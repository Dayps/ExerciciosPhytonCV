
print('=== Desafio 15 ===')
 # Valor à pagar pelo aluguel do carro
 # Quantidade de Km percorridos e quantidade de dias que foi alugado

dias = int(input('Quantos dias o carro foi alugado? : '))
km = float(input('Quantos Km rodados?: '))
total = (dias * 60) + (km * 0.15)
print('.'*40)
print('Diaria do carro: R$60')
print('Km rodado: R$0.15')
print('.'*40)
print(f'O total a pagar é de R${total:.2f}')