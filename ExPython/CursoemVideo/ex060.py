n = int(input('Digite um numero para saber o seu fatorial:'))
c = n
f = 1
print('calculando {}! ='.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))


'''from math import factorial
n = int(input('Digite um numero para saber o seu fatorial:'))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''