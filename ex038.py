"""Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
 conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O primeiro valor é maior! ')
elif n2 > n1:
    print('O segundo valor é maior! ')
else:
    print('Os valores são iguais! ')
