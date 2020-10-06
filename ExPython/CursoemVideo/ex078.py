menor = []
maior = []
valor = []
for c in range(0, 5):
    valor.append(int(input(f'Digite um valor na posição {c}:')))
    if c == 0:
        menor = maior = valor[c]
    else:
        if valor[c] < menor:
            menor = valor[c]
        if valor[c] > maior:
            maior = valor[c]
print(f'você digitou os valores {valor}')
print(f'O maior valor digitado foi {maior} nas posiçãoes', end=' ')
for i, v in enumerate(valor):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posiçãoes', end=' ')
for p, q in enumerate(valor):
    if q == menor:
        print(f'{p}...')
