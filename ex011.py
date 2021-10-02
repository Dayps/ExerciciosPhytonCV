print('=== Desafio 11 ===\n')

# Medir quanta tinta será usada
print('*** Quanto de tinta você irá precisar para pintar sua parede ***')
print('-'*65)

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
parede = altura * largura
tinta = parede/2

print('** Cada litro de tinta pode pintar 2 m² **')
print('-'*40)
print(f'Sua parede possui {parede} m²')
print(f'Você vai precisa {tinta:.2f} litros de tinta para pintar sua parede.')
