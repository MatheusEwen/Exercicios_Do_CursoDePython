from datetime import date
ano = int(input('Digite o ano de seu nascimento:'))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('MIRIM')
elif 10 <= idade <= 14:
    print('INFANTIL')
elif idade >= 15 and idade <= 19:
    print('JUNIOR')
elif idade > 19 and idade < 25:
    print('SENIOR')
else:
    print('MASTER')