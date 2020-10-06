def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO, por favor, digite um numero interio valido\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[0;31mO usuario preferiu não digitar esse número \033[m')
            return 0
        else:
            return n


def lin(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(lin())
    print(txt.center(42))
    print(lin())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m-\033[34m{item}\033[m')
        c += 1
    print(lin())
    opc = leiaint('Sua opção:')
    return opc