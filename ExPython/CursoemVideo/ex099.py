from time import sleep
from random import randint
def lin():
    print('-=' * 20)

def maior(*num):
    lin()
    m = cont = 0
    print(f'\nAnalisando os valores passados....')
    for valor in (num):
        print(f'{valor}', end= ' ', flush=True)
        sleep(0.5)
        if cont == 0:
            m = valor
        elif valor > m:
            m = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {m}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)

