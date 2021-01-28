"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER"""

from datetime import date
n = int(input('Ano de nascimento: '))
a = date.today().year
i = a - n
print(f'O atleta tem {i} anos')
if i <= 9:
    print('Você é da categoria MIRIM! ')
elif i >= 9 and i <= 14:
    print('Você é da categoria INFANTIL! ')
elif i >= 14 and i <=19:
    print('Vocé é da categoria JUNIOR! ')
elif i >= 19 and i <= 25:
    print('Você é da categoria SENIOR! ')
else:
    print('Você é da categoria MASTER! ')

