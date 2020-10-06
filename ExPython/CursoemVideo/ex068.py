import random
print('=-'*20)
print('Vamos jogar Par ou Impar')
print('=-'*20)
cont = 0
while True:
    c = random.randint(0, 10)
    n = int(input('Diga um valor:'))
    r =  str(input('Par ou Impar? [P/I]')).upper().strip()
    while r not in 'pPiI':
        r = str(input('Par ou Impar? [P/I]:')).upper().strip()
    s = c + n
    if s % 2 == 0:
        print(f'voce jogou {n} e computador jogou {c}. total de {s} deu Par')
        if r in 'Pp':
            cont += 1
            print('VOCÊ VENCEU!')
        elif r in 'Ii':
            print('Voce PERDEU')
            break
    elif s % 2 != 0:
        print(f'Voce jogou {n} e computador jogou {c}. total de {s} deu Impar')
        if r in 'Ii':
            cont += 1
            print('VOCE VENCEU!')
        elif r in 'pP':
            print('Voce perdeu')
            break
print(f'GAME OVER. Você venceu {cont} vezes')





