print('=== Treinando comandos ===')

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale {}'.format(n1+n2))

# Não precisa usar mais uma variável soma, pois nesse caso vai vai ser usada depois.
# Caso precise desse valor posteriormente, criar uma variável para guardar.

print('-'*50)
name = str(input('Seu nome: '))
print(f'Ola {name:*^20}'.upper())

print('-'*50)
print('=== Desafio 05 ===')

num = int(input('Digite um número: '))
print(f'O antecessor de {num} é {num-1} e o sucessor é {num+1}')