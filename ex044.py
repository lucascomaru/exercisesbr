"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros"""

p = float(input('Preço de compras: '))
print('''Formas de Pagamento
[ 1 ] a vista dinheiro/cheque:
[ 2 ] a vista cartão:
[ 3 ] 2x no cartão:
[ 4 ] 3x ou mais no cartão:''')

op = int(input('Qual é a sua opção? '))
if op == 1:
    total = p - (p * 10 / 100)
elif op == 2:
    total = p - (p * 5 / 100)
elif op ==3:
    total = p
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de {parcela:.2f}SEM JUROS ')
elif op == 4:
    total = p + (p * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print(F'Sua compra será parcelada em {totalparc:.2f}x de R${parcela:.2f} ')
else:
    total = p
    print('Opção inválida de pagamento. Tente novamente! ')
print(f'Sua compra de {p:.2f} vai custar {total:.2f} no final. ')
