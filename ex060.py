"""Faça um programa que leia um número qualquer e mostre o seu fatorial."""

n1 = int(input('Digite um número inteiro qualquer: '))
acumulador = 1
for n1 in range(n1, 0, -1):
    acumulador *= n1
print(f'O produto de todos os números é {acumulador}')