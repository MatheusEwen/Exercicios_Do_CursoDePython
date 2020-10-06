import datetime
a = 0
b = 0
for c in range(1, 8):
    ano = int(input('DiGITE O ANO DE NASCIMENTO da {}ºpesso:'.format(c)))
    atual = datetime.date.today().year
    idade = atual - ano
    if idade >= 21:
        a = a + 1
    elif idade < 21:
        b = b + 1
print('Há {} de maior idade e {} de menor idade'.format(a, b))
