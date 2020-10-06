km = float(input('Qual é a distacia da viaem?:'))
if km <= 200:
    v = km*0.50
    print('A sua viagem vai custar R${:.2f}'.format(v))
else:
    v2 = km*0.45
    print('A sua viagem vai custar R${:.2f}'.format(v2))

