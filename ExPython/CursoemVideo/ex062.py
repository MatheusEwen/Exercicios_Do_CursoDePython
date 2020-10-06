t1 = int(input('Digite o primeiro termo da PA:'))
r = int(input('Digite a razão da PA:'))
termos = 0
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termos), end='')
        termos += r
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer por a mais?:'))
print('fim')
print('progressão finalizada com {} termos'.format(total))
