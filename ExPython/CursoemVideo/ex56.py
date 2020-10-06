somaidade = 0
mediaidade = 0
maioridadehomem = 0
totmulher20 = 0
for p in range(1,5):
    print('------pessoa{}º------'.format(p))
    nome = str(input('Digite o nome:')).strip()
    idade = int(input('Digite a idade:'))
    sexo = str(input('Digite o sexo [M]Masculino e [F]Feminino:')).strip()
    somaidade += idade
    if p == 1 and sexo == 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade/4
print('A media de idade do grupo é {} anos'.format(mediaidade))
print('O nome do homem mais velho tem {} anos e o nome dele é {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))

