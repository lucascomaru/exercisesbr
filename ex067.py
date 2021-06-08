"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo. """

while True:
 print('-=' * 25)
 n = int(input('Digite um número para saber a sua tabuada [0 - SAIR]: '))
 if n == 0:
  break