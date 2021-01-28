"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre
seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida"""

p = float(input('Qual é o seu peso? '))
a = float(input('Qual é a sua altura? '))
imc = p / (a ** 2)
print(f'O IMC dessa pessoa é igual a {imc:.1f}')
if imc <= 18.5 :
    print('Você está abaixo do PESO IDEAL! ')
elif imc <= imc < 25:
    print('Parabéns, você está no PESO IDEAL! ')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO! ')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE! ')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA! ')

