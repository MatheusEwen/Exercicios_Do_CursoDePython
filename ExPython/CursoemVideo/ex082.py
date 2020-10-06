valor = []
par = []
impar = []
while True:
    valor.append(int(input('Digite um numero:')))
    r = str(input('Quer Continuar?[S/N]:'))
    if r not in 'Ss':
        break
print(f'Lista {valor}')
for c in valor:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'Os numero pares são {par}')
print(f'Os numeros impares são {impar}')


