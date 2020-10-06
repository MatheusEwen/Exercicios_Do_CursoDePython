s = float(input('Digite o seu salario:'))
if s > 1250.00:
    a = s + (s * 10/100)
    print('O seu salario com 10% de aumento é {:.2f}'.format(a))
else:
    a2= s + (s * 15/100)
    print('O seu salario com 15% de aumento é {:.2f}'.format(a2))
