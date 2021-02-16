"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digi
tação novamente até ter um valor correto."""


sexo = " "
while sexo != 'M' and sexo != 'F':
	sexo = str(input("Qual seu sexo?[M/F] ")).upper().replace (' ', '')
	if sexo != 'M' and sexo != 'F':
		print("Digite uma opcao valida")
if sexo == 'M':
		print("O Sexo masculino foi registrado com sucesso...")
if sexo == 'F':
		print("O sexo Feminimo foi registrado com sucesso....")