import random
print('=== Desafio 20 ===')
# Um programa que escolhe a ordem de apresentação de um trabalho
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
# Fazer que o programa embaralhe (shuffle) a ordem dos alunos digitados
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)