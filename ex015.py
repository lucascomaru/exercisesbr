"""Escreva um programa que pergunte a quantidade de km percorridos de um carro alugado e a quantidade de dias pelos
quais ele foi alugado.Calcule um preço a  pagar sabendo que o carro custa 60 reais por dia e 0.15 km por km rodado."""

km = float(input('Quantos km percorridos?: '))
d = float(input('Por quantos dias ele foi alugado?:' ))
pagar = (d * 60) + (km * 0.15)
print(f'O total a pagar é de R$ {pagar}')