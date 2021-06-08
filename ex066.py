"""Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas
(desconsiderando o flag)."""

c = tot = 0
while True:
    n = int(input('Digite um valor [999 para sair]: '))
    if n == 999:
        break
    c += 1
    tot += n
print(f'A soma dos valores foi {c} e o total foi {tot}')

