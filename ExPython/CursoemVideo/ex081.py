valor = []

while True:
    valor.append(int(input('Digite um valor para adiciona-lo na lista:')))
    r = str(input('Quer Continuar?[S/N]:'))
    if r not in 'Ss':
        break

print(f'Os valores digitados foram {valor}, há {len(valor)} valores')
valor.sort(reverse=True)
print(f'Os valores em ordem decresente é {valor}')
if 5 in valor:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')