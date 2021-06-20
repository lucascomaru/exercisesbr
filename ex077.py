"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
 para cada palavra, quais são as suas vogais."""

palavras = ('AVIÃO', 'CARRO' , 'FUTEBOL', 'SKATE','PYTHON','JAVA','CHUVA','ARVORE','NATUREZA')
count = 0
for x in range(0,len(palavras)):
    print(f"\nNa palavra {palavras[x]} temos as vogais:", end=' ')
    for i in palavras[x]:
        if i in 'AEIOUÃ':
            print(i,end=' ' )
print('\n')