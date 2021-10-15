import random
print('=== Desafio 19 ===')

# Colocar nome de 4 alunos e sortear o nome de 1
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(f'O escolhido foi {escolhido}')