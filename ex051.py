"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão."""

pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
d = pri + (10 - 1) * raz
for n in range(pri, d + raz, raz):
    print(f'{n}')
print('Fim')