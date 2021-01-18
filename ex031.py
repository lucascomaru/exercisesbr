""""Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando 
R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas."""""

d = float(input('Qual é a distância da sua viagem?: '))
print(f'Você está prestes a começar uma viagem de {d} Km')
if d <= 200:
    p = d * 0.50
else:
    p = d * 0.45
print(F'E o preço da sua viagem será de R$ {p}')