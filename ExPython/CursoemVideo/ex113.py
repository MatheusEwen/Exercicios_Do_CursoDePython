def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO, por favor, digite um numero interio valido\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[0;31mO usuario preferiu não digitar esse número \033[m')
            return 0
        else:
            return n



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


n1 = leiaint('digite um valor inteiro:')
n2 = leiafloat('digite um valor real:')
print(f'O valor digitado foi {n1} e o valor real foi {n2}')

