v = float(input('Qual foi a velocidade do carro KM:'))
if v > 80:
    m = (v-80)*7
    print('Você foi multado por dirigir a cima da velocidade \nSua velocidade foi de:{}Km. \nA multa a pagar será de R${:.2f}'.format(v, m))
else:
    print('tudo ok')
