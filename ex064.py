"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre
 eles """

n = c = soma = 0
while n != 999:
    n = int(input('Digite o número inteiro: '))
    if n != 999:
        c += 1
        soma = soma + n
print(f'Foram digitados {c} valores e a soma deles eh: {soma}.')

