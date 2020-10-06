r = 'S'
soma = quant = media = 0
while r in 'sS':
    n = int(input('Digite um número:'))
    soma += n
    quant += 1
    if quant == 1:
        menor = maior = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    r = str(input('Quer continuar?[S/N]')).strip().upper()
media = soma/quant
    
print('Você digitou {} numeros e a media entre eles é {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))



