dados = {}
partidas = []
dados['nome'] = str(input('Digite o nome do jogador:'))
tot = int(input(f'Quantas partidas o {dados["nome"]} jogou?:'))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols fez na {c}º partida')))
dados['gols'] = partidas
dados['total'] = sum(partidas)
print('=-'*30)
print(dados)
print('=-'*30)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('=-'*30)
print(f'O {dados["nome"]} jogou {len(dados["gols"])} partidas')
for i, v in enumerate(dados['gols']):
    print(f'Na partida {i} fez {v} gols')
print(f'O total de gols foi {dados["total"]}')






