"Faça um programa que leia um ano qualquer e mostre se ele é bissexto."

from datetime import date
a = int(input('Digite o ano que quer analisar?Coloque 0 pra analisar o ano atual: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'O ano {a} é BISEXTO')
else:
    print(f'O ano {a} não é BISEXTO')
