"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
triângulo."""

t1 = float(input('Primeiro segmento: '))
t2 = float(input('Segundo segmento: '))
t3 = float(input('Terceiro segmento: '))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Os segmantos acima PODEM FOMRAR UM TRIÂNGULO: ')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO: ')
