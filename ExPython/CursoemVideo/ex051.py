t1 = int(input('Digite o primeiro termo da PA:'))
r = int(input('Digite a razão da PA:'))
t2 = 0
print(t1)
for c in range(1, 10):
    t1 += r
    #t1 = t1
    print('{}'.format(t1))

''' 
Primeiro termo = int(input('primeiro termo'))
razão = int(input('razão'))
decimo = primeiro + (10 - 1) * razão
for c in range(primeiro, decimo + razão, razão):
    print('{}'.format(c), end= '->')
print('acabou')
'''