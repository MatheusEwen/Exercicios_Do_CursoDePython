expre = str(input('Digite uma expressão:'))
pilha = []
for sim in expre:
    if sim == '(':
        pilha.append('(')
    elif sim == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão é valida')
else:
    print('A expressão é invalida')
