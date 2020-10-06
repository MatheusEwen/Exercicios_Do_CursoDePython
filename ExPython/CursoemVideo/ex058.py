import random
v = 0
v1= 2
toterros = 0
v = random.randint(0, 10)
print('-=-'*20)
print('\033[1;31mvou pensar em um número...\033[m')
print('-=-'*20)
acertou = False
while not acertou:
    v1 = int(input('Entre 0 a 10 qual o numero que o computador pensou?:'))
    toterros += 1
    if v1 == v:
        acertou = True
        print('\033[1;32;44mVocê venceu!\033[m')
    else:
        if v1 < v:
            print('tente mais alto')
        elif v1 > v:
            print('tente mais baixo')
print('Finalmente você vonceu, foi preciso {} chutes.'.format(toterros))




'''import random
v = 0
v1= 2
toterros = 0

while v != v1:
    v = random.randint(0, 10)
    print('-=-'*20)
    print('\033[1;31mvou pensar em um número...\033[m')
    print('-=-'*20)

    v1 = int(input('Entre 0 a 10 qual o numero que o computador pensou?:'))
    print('O numero que você escolheu foi {}, e o numero gerado foi {}'.format(v1, v))
    if v1 == v:
        print('\033[1;32;44mVocê venceu!\033[m')
    else:
        toterros += 1
        print('Você perdeu!')
print('Finalmente você vonceu, foi preciso {} chutes.'.format(toterros))'''
