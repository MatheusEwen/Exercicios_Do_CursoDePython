def fatorial(n, show=False):
    """
    --> calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: (opicional) mostrar ou não a conta
    :return: O valor fatorial de um numero n
    """
    f = 1
    if show == False:
        for c in range (n, 0, -1):
            f *= c
        return f
    if show == True:
        for c in range (n, 0, -1):
            print(c, end='')
            if c > 1:
                print(f' X ', end= '')
            else:
                print('=', end=' ')
            f *= c
        return f
        print()


print(fatorial(5, False))
help(fatorial)




