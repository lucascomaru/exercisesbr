"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

lista = []
for c in range (1,6):
    lista.append(int(input (f'Qual o peso da {c}ª pessoa? ')))
print ('O maior peso é', max(lista))
print ('O menor peso é', min(lista))