from time import sleep
def contador(inicio, fim, passo):
    
    for n in range(inicio, fim, passo):
        print(n, end= ' ')
        sleep(0.5)


print('=='*10)
for n in range(0, 10):
    print(n, end= ' ')
    sleep(0.5)
print()
print('=='*10)
for n in range(10, 0, -2):
    print(n, end= ' ')
    sleep(0.5)
print()
print('==' * 10)
print('Agora é sua vez de personalizar sua contagem')
inicio = int(input('Inicio'))
fim = int(input('Fim'))
passo = int(input('Passo'))
contador(inicio, fim, passo)