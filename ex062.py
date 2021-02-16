"""Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará
quando ele disser que quer mostrar 0 termos."""

termo1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
condicao = 1
termon = termo1
print(f'10 Primeiros termos da PA de razão = {razao} e 1º termo = {termo1}:')
while condicao < 11:
    if condicao < 10:
        print(f'{termon}, ', end='')
        termon += razao
    else:
        print(f'{termon}.')
    condicao += 1
maistermos = int(input('Deseja ver vais termos? Digite a quantidade ou 0 para encerrar: '))
while maistermos > 0:
    novolimite = condicao + maistermos
    while condicao < novolimite:
        termon += razao
        if (condicao + 1) == novolimite:
            print(f'{termon}.')
        else:
            print(f'{termon}, ', end='')
        condicao += 1
    maistermos = int(input('Deseja ver vais termos? Digite a quantidade ou 0 para encerrar: '))
print('PROGRAMA ENCERRADO.')