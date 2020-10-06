import random

v = random.randint(0, 5)
print('-=-'*20)
print('vou pensar em um número...')
print('-=-'*20)

v1 = int(input('Entre 0 a 5 qual o numero que o computador pensou:'))
print('O numero que você escolheu foi {}, e o numero gerado foi {}'.format(v1, v))
if v1 == v:
    print('Você venceu!')
else:
    print('Você perdeu!')
