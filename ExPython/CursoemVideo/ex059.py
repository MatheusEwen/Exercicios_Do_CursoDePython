r = 0
while r != 5:
    n1 = float(input('Digite o primeiro número:'))
    n2 = float(input('Digite o segundo número:'))
    print('''O que você quer saber?
     [1] \033[1;32mSomar \033[m
     [2] \033[1;33mMultiplicar \033[m
     [3] \033[1;34mMaior \033[m
     [4] \033[1;35mNovos números \033[m
     [5] \033[1;31mSair do programa \033[m
     ''')
    r = int(input('Sua opção:'))

    if r == 1:
            print('A soma dos números {} + {} é {}'.format(n1, n2, n1 + n2))
    if r == 2:
            print('A multiplicação dos números {} X {} é {}'.format(n1, n2, n1 * n2))
    if r == 3:
        if n1 > n2:
            print('O maior numero entre {} e {} é {}'.format(n1, n2, n1))
        elif n1 == n2:
            print('os números são iguais')
        else:
            print('O maior numero entre {} e {} é {}'.format(n1, n2, n2))
    if r == 4:
            print('Digite novamente')
    if r == 5:
            print('Fim volte sempre')
    print('-='*20)
