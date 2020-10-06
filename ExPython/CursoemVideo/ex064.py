cont = 0
total = 0
n = 0
while n != 999:
    cont += n
    total += 1
    n = int(input('Digite um numero [999 para parar]:'))
print('Você digitou {} e a soma deles é {}'.format(total - 1, cont))


