"""Crie um programa que faça o computador jogar Jokenpô com você."""

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print(f'Computador jogou {itens[comp]}' )
print(f'Jogador jogou {itens[comp]}')
if comp == jogador:
    print('Empate')
elif jogador == 1:
    print('JOGADOR VENCEU! ')
elif jogador == 2:
    print('COMPUTADOR VENCEU! ')
else:
    print('JOGADA INVÁLIDA')



