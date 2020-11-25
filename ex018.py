"Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e a tangente desse ângulo."

from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem o seno de {seno:.2f}')
print(f'O ângulo de {angulo} tem o cosseno de {cosseno:.2f}')
print(f'O ângulo de {angulo} tem a tangente de {tangente:.2f} ')

