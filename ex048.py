"""Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo
de 1 até 500."""

soma = 0
for num in range(1, 501, 2):
    if num % 3 ==0:
        soma = soma + num
print(f'A soma de todos os valores é {soma}')
