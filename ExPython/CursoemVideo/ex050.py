s = 0
cont =0
for c in range(6):
    n = int(input('Digite o numero:'))
    if n % 2 == 0:
        cont += 1
        s += n

print('Voce informou {} numeros pares e o valor da soma de todos os numeros pares é {}'.format(cont, s))

