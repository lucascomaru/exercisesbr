"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
listas geradas.
"""

lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    c = str(input('Deseja continuar? [S/N] '))
    while c not in 'NnSs':
        c = str(input('Resposta inválida! Deseja continuar? [S/N] '))
    if c in 'Nn':
        break
print('-='*40)
print(f'A lista completa é {lista}')
for n in range(0, len(lista)):
    if lista[n] % 2 == 0:
        pares.append(lista[n])
    else:
        impares.append(lista[n])
print(f'A lista de pares é {pares}')
print(f'A lista de impares  é {impares}')


