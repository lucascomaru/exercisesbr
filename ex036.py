"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
 do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo
 será negado."""

casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o salário? '))
anos = int(input('Em quantos anos vai pagar? '))
p = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R$ {casa:.2f} em {anos:.2f} anos a prestação será de {p:.2f}: ')
if p <= minimo:
    print('Empréstimo pode ser CONCEDIDO! ')
else:
    print('Empréstimo NEGADO! ')

