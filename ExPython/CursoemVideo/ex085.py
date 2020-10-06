num = [[], []]
for c in range(1,8):
    n = int(input(f'Digite o {c}º numero:'))
    if n % 2 == 0:
        num[1].append(n)
    else:
        num[0].append(n)
num[1].sort()
num[0].sort()
print(f'Os valores pares digitados são {num[1]}')
print(f'Os valores impares digitados são {num[0]}')


