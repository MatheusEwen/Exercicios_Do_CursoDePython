print('='*10,'LOJAS EWEN','='*10)
compra = float(input('Preço das compras R$:'))
print('''Opçoes de pagamento
[1]À vista dinheiro/cheque:10% de desconto
[2]À vista no cartão:5% de desconto
[3]Em ate 2x no cartão:preço formal
[4]3x ou mais no cartão:20% de juros ''')
o = int(input('Digite a opção:'))

if o == 1:
    v1 = compra - (compra*10/100)
    print('Sua compra de R${} vai custar no final R${}'.format(compra, v1))
elif o == 2:
    v2 = compra - (compra*5/100)
    print('Sua compra de R${} vai custar no final R${}'.format(compra, v2))
elif o == 3:
    v3 = compra / 2
    print('Sua compra será parcelada em 2x de R${:.2f}\nSua compra de R${} vai custar no final R${:.2f} no final.'.format(v3, compra, compra))
elif o == 4:
    v4 = compra + (compra*20/100)
    parcela = int(input('quantas parcelas?'))
    v5 = v4 / parcela
    print('Sua compra será parcelada em {}x de R${:.2f} Com juros de 20% \nSua compra de R${} vai custar R${:.2f} no final.'.format(parcela, v5, compra, v4))
else:
    print('ERRO Tente novamente')

