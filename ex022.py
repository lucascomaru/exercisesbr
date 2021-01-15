"""Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome."""

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...: ')
print(f'Seu nome em letras maiúsculas é {nome.upper()}')
print(f'Seu nome em letras minúsculas é {nome.lower()}')
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
