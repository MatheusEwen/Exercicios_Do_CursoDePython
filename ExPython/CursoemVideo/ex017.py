import math

co = float(input('digite o valor do cateto oposto:'))
ca = float(input('digite o valor do cateto adjacente:'))
h = math.hypot(co, ca)
print('o valor da hipotenusa é {:.2f}:'.format(h))