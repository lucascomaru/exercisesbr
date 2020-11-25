"Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros."

medida = float(input('Digite uma medida: '))
cm = medida * 100
mm = medida * 1000
print(f'A medida de {medida} corresponde a {cm}cm {mm}mm ')