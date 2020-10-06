n1 = int(input('Digite um numero inteiro:'))
n2 = int(input('Digite outro numero:'))
if n1 > n2:
    print('O numero {} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('O numero {} é maior que {}'.format(n2, n1))
else:
    print('Os dois valores são iguais')
