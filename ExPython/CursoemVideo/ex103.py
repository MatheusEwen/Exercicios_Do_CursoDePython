def ficha(n='<desconhecido>', g= 0):
    print(f'Jogador {n} fez {g} no campeonato')

nome = str(input('Jogador:'))
gols = str(input('gols feitos:'))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g = gols)
else:
    ficha(nome, gols)
