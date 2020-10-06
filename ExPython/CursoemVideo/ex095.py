time = []
dados = {}
partidas = []
while True:
    dados.clear()
    dados['nome'] = str(input('Digite o nome do jogador:'))
    tot = int(input(f'Quantas partidas o {dados["nome"]} jogou?:'))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols fez na {c +1}º partida')))
    dados['gols'] = partidas[:]
    dados['total'] = sum(partidas)
    time.append(dados.copy())
    while True:
        r = str(input('quer continuar?[S/N]')).upper()[0]
        if r in 'SN':
            break
        print("erro, digite só sim ou não[S/N]")
    if r == 'N':
        break

print('=-'*30)
print('cod', end='')
for i in dados.keys():
    print(f'{i:<15}', end= '')
print()
print('=-'*30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end= '')
    for d in v.values():
        print(f'{str(d):<15}', end= '')
    print()
print('=-'*30)
while True:
    busca = int(input('qual jogador voê quer ver os dados?[999 para parar'))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO NÃO EXISTE ESSE JOGADOR')
    else:
        print(f'---- velantamento do jogador {time[busca]["nome"]} ----')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i + 1} fez {g} gols')
    print('='*40)
print('Volte sempre')