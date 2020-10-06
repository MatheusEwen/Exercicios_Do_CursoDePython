print('digite o valor das retas do triangulo')
r1 = float(input(('digite a reta 1:')))
r2 = float(input(('digite a reta 2:')))
r3 = float(input(('digite a reta 3:')))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Da para se formar um triangulo.', end='')
    if r1 == r2 == r3:
        print(' E será equilatero')
    elif r1 != r2 != r3 != r1:
        print(' E será escaleno')
    else:
        print(' E será isosceles')

else:
    print('Não da para se formar um triangulo')
