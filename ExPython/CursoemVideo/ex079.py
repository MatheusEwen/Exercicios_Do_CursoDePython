valor = []
r = ''
while r in 'sS':
    v = int(input('Digite uma valor:'))
    if v not in valor:
        valor.append(v)
        print('valor adicionado com sucesso')
    else:
        print('Valor duplicado!Não vou adicionar...')
    r = str(input('Quer continuar [S/N]:')).upper().strip()
valor.sort()
print(f'Você digitou os valore {valor}')