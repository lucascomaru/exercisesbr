"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores."""

q=0
media=0
n2=str
p=0
j=0
i=0
lista = []
while n2!='n':
    n1=int(input('Digite um numero  '))
    n2=str(input('Deseja continuar [n/s]?   ')).lower()
    media +=n1
    q +=1
    lista += [n1]
    if n2 =='n':
        p = media /q
        j = max (lista)
        i= min(lista)
print('ACABOU:')
print('Vc digitou {} e a media foi de {}'.format(q,p))
print(' a maior numero foi {} e o menor foi {}'.format(j,i))