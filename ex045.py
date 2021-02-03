"""Crie um programa que faça o computador jogar Jokenpô com você."""

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print(f'Computador jogou {itens[jogador]}')
print(f'Jogador jogou {itens[jogador]}')
if comp == 0:
    if jogador == 0:
        print('EMPATE')
elif jogador == 1:
    print('JOGADOR VENCEU')
elif jogador == 2:
    print('COMPUTADOR VENCEU')
else:
    print('Jogada inválida')
if comp == 1:
   if jogador == 0:
       print('COMPUTADOR VENCEU')
elif jogador == 1:
    print('EMPATE')
elif jogador == 2:
    print('JOGADOR VENCEU')
else:
    print('JOGADA INVÁLIDA')
if comp == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
elif jogador == 1:
    print('COMPUTADOR VENCE')
elif jogador == 2:
    print('EMPATE')
else:
    print('JOGADA INVÁLIDA')


