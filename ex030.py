"Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR."

n = int(input('Me diga um número qualquer: '))
resultado = n % 2
if resultado == 0:
    print(f'O número {n} é PAR')
else:
    print(f'O número {n} é ÍMPAR')