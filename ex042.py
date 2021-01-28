"""Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
"""

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 == s2 == s3:
    print('O triângulo é EQUILÁTERO! ')
elif s1 != s2 != s3 != s1:
    print('O triângulo é ESCALENO! ')
else:
    print('O triângulo é ISOSCELES! ')


