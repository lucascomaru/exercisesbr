"""Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print("""
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa""")
    op = int(input('Digite a opção desejada: '))
    if 1 <= op <= 5:
        if op == 1:
            print(v1+v2)
        elif op == 2:
            print(v1 * v2)
        elif op == 3:
            maior = v1
            if v2 > maior:
                maior = v2
            print(maior)
        elif op == 4:
            v1 = int(input('Primeiro valor: '))
            v2 = int(input('Segundo valor: '))
    else:
        print('Opção invalida! Tente outra vêz!')

