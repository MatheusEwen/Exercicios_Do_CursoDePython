from datetime import date
ano = int(input('Digite o ano em que você nasceu:'))
atual = date.today().year
result = atual - ano
if result == 18:
    print('Ta na hora de se alistar ')
elif result < 18:
    v1 = 18 - result
    print('falta {} anos para você se alistar'.format(v1))
else:
    v2 = result -18
    print('ja passou {} anos do prazo'.format(v2))
