"""Faça um programa que leia a largura e a altura de uma parede em metros,calcule a sua área 
e a quantidade de tinta necessária para pinta-la sabendo que cada litro de tinta pinta uma 
área de 2 metros quadrados."""""

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2
print(f'Sua parede tem dimensão de {larg} x {alt}  e sua área é de {area}m² ')
print(f'Para pintar essa parede, você precisará de {tinta}l de tinta')