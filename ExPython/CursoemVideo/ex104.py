def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;32m Erro, Digite um número. \033[m')
        if ok:
            return valor
            break



n = leiaint(input('Digite um número:'))
print(f'você acabou de digitar {n}')
