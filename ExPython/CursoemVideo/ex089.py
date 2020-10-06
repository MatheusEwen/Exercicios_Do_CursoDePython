ficha = []
while True:
    nome = str(input('Digite o nome:'))
    nota1 = float(input('nota 1:'))
    nota2 = float(input('nota 2:'))
    media = nota1 + nota2/2
    ficha.append([nome, [nota1, nota2], media])
    r = str(input('Quer continuar?[S/N]:')).strip().upper()
    if r in 'Nn':
        break
print('-'*30)
print(f'{"No.":<4}{"Nome":<10}{"media":>8}')
print('-'*25)
for i, a in enumerate(ficha):
    print(f'Aluno {i:<4}º{a[0]:<10}{a[2]:>8.1f}')
while True:
    p = int(input('Quer saber as notas de qual aluno?[999 para parar]:'))
    if p == 999:
        print('Tchau volte sempre')
        break
    else:
        print(f'As notas do aluno {ficha[p][0]} são {ficha[p][1]} ')

