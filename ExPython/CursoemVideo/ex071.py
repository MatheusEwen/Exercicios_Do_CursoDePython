print('='*20)
print('    BANCO CEV')
print('='*20)
valor = int(input('Qual o valor que você que sacar?:R$'))
total = valor
ce = 50
totaldece = 0
while True:
    if total >= ce:
        total -= ce
        totaldece += 1
    else:
        if totaldece > 0:
            print(f'total de {totaldece} cedulas de R$ {ce}')
        if ce == 50:
            ce = 20
        elif ce == 20:
            ce = 10
        elif ce == 10:
            ce = 1
        totaldece = 0
        if total == 0:
            break
print('Volte sempre')

