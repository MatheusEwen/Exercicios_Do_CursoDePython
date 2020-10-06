casa = float(input('Qual o valor da casa? R$:'))
salario = float(input('Quanto é o seu salario? R$:'))
anos = int(input('Em quantas parcelas você vai pagar?:'))
prestação = casa/(anos*12)
minimo = salario*30/100

if prestação <= minimo:
    print('você pode finaciar essa casa')
    print('A prestação será de {:.2f}'.format(prestação, anos))
else:
    print('Você não pode financiar essa casa')
