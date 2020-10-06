p = float(input('Digite o seu peso(kg):'))
a = float(input('digite sua altura:'))
imc = p/(a*a)
print('O imc dessa pessoa é {}'.format(imc))
if imc < 18.5:
    print('abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('obsidade')
else:
    print('obsidade morbida, cuidado.')