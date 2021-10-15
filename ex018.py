import math
print('=== Desafio 18 ===')

ângulo = float(input('Digite o ângulo que você deseja: '))
# Converter graus para radianos
# Depois que for convertido para radianos, será calculado o seno dele.
sin = math.sin(math.radians(ângulo))
cos = math.cos(math.radians(ângulo))
tan = math.tan(math.radians(ângulo))
print(f'O ângulo de {ângulo} tem o SENO de {sin:.2f}')
print(f'O ângulo de {ângulo} tem o COSSENO de {cos:.2f}')
print(f'O ângulo de {ângulo} tem TANGENTE de {tan:.2f}')
