"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número
já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
crescente"""

lista = []
while True:
    n = int(input('Digite um número inteiro: '))
    if n in lista:
        print('ESSE NÚMERO JÁ CONSTA NA LISTA.')
        lista.remove(n)

    lista += [n]

    flag = str(input('Continuar? (S/N): ')).strip().lower()[0]
    if flag == 'n':
        print(f'\nOs números digitados foram {sorted(lista)}')
        break
