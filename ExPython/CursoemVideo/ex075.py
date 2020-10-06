totalpares = 0
posição = 0
numeros = (int(input('Digite um valor:')),
           int(input('Digite um valor:')),
           int(input('Digite um valor:')),
           int(input('Digite um valor:')))
print(numeros)
print(f'o valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado')
print(f'Os valores pares digitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
