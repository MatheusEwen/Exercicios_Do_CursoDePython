matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
colunatres = 0
linha = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]'))
        if matriz[l][c] % 2 ==0:
            soma += matriz[l][c]
for l in range(0, 3):
        colunatres += matriz[l][2]
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]

print('-='*30)
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end= '')
    print()
print(f'A soma de todos os valores pares digitados são {soma}')
print(f'A soma da terceira coluna é {colunatres}')
print(f'O maior valor da 2 linha é {mai}')