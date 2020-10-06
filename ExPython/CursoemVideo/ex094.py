galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome da pessoa:'))
    while True:
        pessoa['sexo'] = str(input('Digite o sexo:[M/F]')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO, somente [M/F]')
    pessoa['idade'] = int(input('idade:'))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        r = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
        if r in 'NS':
            break
        print('Erro digite só [S/N]')
    if r == 'N':
        break
print(f'A) {len(galera)} pessoas foram cadstradas')
media = soma/len(galera)
print(f'B) A media do grupo é {media}')
print('As mulheres cadastradas foram,', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end=' ')
print()
print('Pessoas acima da media', end= ' ')
for p in galera:
    if p['idade'] >= media:
        print(f'   ')
        for k, v in p.items()
            print(f'{p["nome"]} com idade de {p["idade"]}')
print()
print('-='*30)







