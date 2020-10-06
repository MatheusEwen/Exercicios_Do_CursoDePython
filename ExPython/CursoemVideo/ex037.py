num = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
[1]Binario
[2]octal
[3]hexadecimal''')
opção = int(input('sua opção:'))
if opção == 1:
    print('{} convertido para binario é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é {} '.format(num, hex(num)[2:]))
else:
    print('Opção invalida tente novamente')