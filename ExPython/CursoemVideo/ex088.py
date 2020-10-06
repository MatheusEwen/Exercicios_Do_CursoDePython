from random import randint
import time
lista = []
jogos = []
tot = 1
print('-'* 30)
print('     Jogo da mega sena     ')
print('-'* 30)
q = int(input('Quantos jogos voce quer que eu sorteie?:'))
while tot <= q:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'='*30)
for i, l in enumerate(jogos):
    print(f'O jogo {i + 1}º:{l}')
    time.sleep(1)
print('BOA SORTE')




