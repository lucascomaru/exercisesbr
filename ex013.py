"Faça um algoritmo que leia um salário de um funcionário e mostre seu novo salário com 15% de aumento"

salario = float(input('Digite o salário do funcionário: '))
novo = salario + (salario * 15 / 100)
print(f"Um funcionário que ganhava R${salario:.2f}, com o ajuste de 15%, passa a receber R${novo:.2f}: ")