import random
import time
itens = ('pedra', 'papel', 'tesoura')
print('''Qual a sua jogada?
[0] PERDRA
[1] PAPEL
[2] TESOURA''')
print('=-='*10)
ia = random.randint(0, 2)
j = int(input('Qual a sua jogada?:'))
print('=-='*10)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
time.sleep(1)
print('=-='*11)
print('O computador jogou {}'.format(itens[ia]))
print('O jogador jogou {}'.format(itens[j]))
print('=-='*11)
if ia == 0:
    if j == 0:
        print('Empate')
    elif j == 1:
        print('Jogador venceu')
    elif j == 2:
        print('Computador venceu')
    else:
        print('JOGADA INVALIDA')
if ia == 1:
    if j == 0:
        print('Computador venceu ')
    elif j == 1:
        print('Empate')
    elif j == 2:
        print('Jogador venceu')
    else:
        print('JOGADA INVALIDA')
if ia == 2:
    if j == 0:
        print('Jogador venceu')
    elif j == 1:
        print('Computador venceu')
    elif j == 2:
        print('Empate')
    else:
        print('JOGADA INVALIDA')












