"""Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while."""


pa = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razaão da PA: '))
cont = 0

print()
while cont < 10:
    print(pa, end=' - ')
    pa += razao
    cont += 1

print('Fim!')