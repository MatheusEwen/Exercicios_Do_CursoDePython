v = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor?'))
    if n < 0:
        break
    while True:
        v += 1
        print(f'{n} X {v} = {n*v}')
        if v == 10:
            v = 0
            break
print('Programa encerrado')