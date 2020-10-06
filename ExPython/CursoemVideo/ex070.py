soma = 0
barato = 0
cont = 0
produtobarato = ''
quant = 0
while True:
    print('=-'*20)
    print('Lojas super baratão')
    print('=-'*20)
    p = str(input('Qual o nome do produto?')).strip()
    v = float(input('Qual o valor do produto?:R$'))
    quant += 1
    if quant == 1:
        produtobarato = p
        barato = v
    if v > 1000:
        cont += 1
    elif v < barato:
        barato = v
        produtobarato = p
    soma += v
    r = str(input('Quer continuar?[S/N]:'))
    if r in 'nN':
        break
print('='*20)
print('Fim do Programa')
print('='*20)
print(f'O total da compra foi R${soma}')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produtobarato} custando R${barato}')
