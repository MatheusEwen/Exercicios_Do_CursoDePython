from random import randint
numeros = []
def sorteia(lista):
    print('Sorteando valores:', end= '')
    n = 1
    while True:
        if n <= 5:
            lista.append(randint(1,10))
            n += 1
        else:
            print(f'{lista}', end='')
            print()
            break


def somap(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteia(numeros)
somap(numeros)





