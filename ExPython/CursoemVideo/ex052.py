n = int(input('Digite um numero inteiro:'))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        tot += 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(n, tot))
if tot == 2:
    print('O número {} é PRIMO'.format(n))
else:
    print('O número {} NÃO é primo'.format(n))