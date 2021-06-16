"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Flamengo."""

times = ('Fortaleza', 'Athlético-PR', 'Flamengo', 'Atlético-GO',
         'Atlético-MG', 'Bragantino', 'Fluminense', 'Bahia',
         'Palmeiras', 'Corinthians', 'Ceará', 'Santos','Internacional',
         'Juventude', 'Cuiabá', 'Sport', 'São Paulo', 'Chapecoense',
         'Grêmio', 'América-MG')
print(f'Tabela da terceira rodada do Brasileirão 2021{times}')
print(f'Os 4 primeiros colocados são {times[0:4]}')
print(f'Os times em ordem alfábetica são {sorted(times)}')
print(f'Os quatro últimos colocados são{times[-4:]}')
print(f'O Flamengo está na {times.index("Flamengo")+1} posição')

