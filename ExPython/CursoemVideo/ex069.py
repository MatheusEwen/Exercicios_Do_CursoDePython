contmaior = 0
conthomem = 0
contmulher = 0
while True:
    print('=-'*15)
    print('Cadastre uma pessoa')
    print('=-'*15)
    idade = int(input('Idade:'))
    if idade >= 18:
        contmaior += 1
    sexo = str(input('[M/F]')).strip().upper()
    while sexo not in 'MmFf':
        sexo = str(input('[M/F]')).strip().upper()
    if sexo in 'Mm':
        conthomem += 1
    elif sexo in 'Ff':
        if idade < 20:
            contmulher += 1
    r = str(input('Quer continuar?[S/N]:'))
    if r in 'Nn':
        break
print(f'Total de pessoas com mais de 18 anos {contmaior}')
print(f'Ao todo temos {conthomem} homens cadastrados')
print(f'O número de mulheres com menos de 20 anos é {contmulher}')
print('fim do programa.')




