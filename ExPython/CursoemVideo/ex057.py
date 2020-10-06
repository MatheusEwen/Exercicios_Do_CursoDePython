sexo = str(input('digite o seu sexo [M/F]:')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos.informe o seu sexo [M/F]'))
print('Sexo {} registrado com sucesso'.format(sexo))




'''r = 'p'
while r != 'M' and r != 'F':
    r = str(input('digite o seu sexo [m ou f]:')).upper().strip()
    if r != 'M' and r != 'F':
        print('invalido')
print('acabou')'''
