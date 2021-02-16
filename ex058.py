"""Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""

tentativas = 0
from random import randint
computador = randint(0,10)
jogador = int(input("""Sou seu computador...
Acabei de pensar em um numero entre 0 e 10.
Será que você consegue adivinhar qual foi?
Qual o seu palpite?"""))
while computador != jogador:
	tentativas += 1
	if computador < jogador:
		jogador = int(input("""Menos...Tente mais uma vez.
Qual é o seu palpite? """))
	elif computador > jogador:
		jogador = int(input("""Mais...Tente mais uma vez.
Qual é o seu palpite? """))
print(computador)
print(f'Acertou com {tentativas} tentativas. Parabens!')