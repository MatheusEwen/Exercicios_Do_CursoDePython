from math import sin, cos, tan, radians
an = int(input('digite um angulo:'))

sen = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('O seno de {} é {:.2f}'.format(an, sen))
print('O coseno de {} é {:.2f}'.format(an, cos))
print('A tangente de {} é {:.2f}'.format(an, tan))