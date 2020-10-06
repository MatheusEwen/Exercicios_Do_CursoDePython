pessoas = []
dados = []
mai = men = 0
while True:
    dados.append(str(input('Qual o Nome:')))
    dados.append(float(input('Peso:')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        elif dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    r = str(input('Quer continuar? [S/N]:')).strip().upper()
    if r in 'Ss':
        print('Cadastre outra pessoa')
    else:
        print('-='*30)
        break

print(f'Total de pessoas cadstradas {len(pessoas)}')
print(f'O maior peso foi {mai}. peso de ', end= '')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]} ',end='')
print()
print(f'O menor peso foi {men}.peso de ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]}')
print()
