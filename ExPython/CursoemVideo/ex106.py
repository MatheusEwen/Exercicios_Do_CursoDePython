from time import sleep
c = ('\033[m',          #0- nada
     '\033[0;30;41m',#1 - vermelho
     '\033[0;30;42m',#2 - verde
     '\033[0;30;43m',#3 - amarelo
     '\033[0;30;44m',#4 - azul
     '\033[0;30;45m',#5 - roxo
     '\033[7;30m'#6 - branco
     );

def ajuda(con):
    titulo(f'acessando o manual do comando {con}', 4)
    print(c[6])
    help(con)
    print(c[0])
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


while True:
    titulo('sistema de ajuda PyHelp', 2)
    comando = str(input('função ou biblioteca:'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Ate logo!!!', 1)









'''def sistema():
    while True:
        print('\033[30;42m='* 20)
        print('    Ajuda python')
        print('='* 20)
        p = str(input('\033[mFunção ou Biblioteca>')).strip().lower()
        print('\033[30;44m~~'*15)
        print(f'  Acessando manual do {p}')
        print('~~'*15)
        print('\033[7;37;40m')
        help(p)
        print('\033[m')
        r = str(input('quer continuar?[S/N]')).strip().upper()
        if r not in 'sS':
            break'''



