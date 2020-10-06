from ex115.lib.interface import *
from ex115.lib.arquivo import *
import time

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)

    elif resposta == 2:
        cabeçalho('Novo cadastro')
        nome = str(input('Digite o nome:'))
        idade = leiaint('Digite sua idade:')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...')
        break
    else:
        print('\033[31mErro, Digite uma opção valida\033[m')
    time.sleep(1)