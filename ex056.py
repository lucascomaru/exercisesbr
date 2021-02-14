"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""

soma = 0
cont = 0
media = 0
maior = 0
m21 = 0
maisvelho = 0
for c in range(1, 5):
    print(f'------{c}ª PESSOA ------')
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M]/[F]: ')).strip().upper()
    soma += idade
    cont += 1
    media = soma / cont
    if sexo == 'M':
        if c == 1:
            maior = idade
        else:
            if idade > maior:
                maior = idade
                maisvelho = nome
    elif sexo == 'F':
        if idade < 21:
            m21 += 1
print(f'A média de idade é {media} anos,\n'
      'O nome do homem mais velho é {maisvelho}\n'
      'Ao todo são {m21} mulheres com menos de 21 anos')