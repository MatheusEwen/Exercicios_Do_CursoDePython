a = float(input('Digite um numero:'))
b = float(input('Digite um numero:'))
c = float(input('Digite um numero:'))
menor = a
if b<c and b<a:
   menor=b
if c<a and c<b:
   menor=c
maior = a
if b>a and b>c:
   maior = b
if c>a and c>b:
   maior = c
print('O menor numero é {}, e o maior é {}'.format(menor, maior))