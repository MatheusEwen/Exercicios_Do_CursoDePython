import datetime
ano = datetime.date.today().year
dados = {}
dados['nome'] = str(input('digite seu nome:'))
dados['an'] = int(input('Digite em que ano você nasceu:'))
dados['ctps'] = int(input('numero da carteirad de trabalho(0 para não tem):'))
dados['idade'] = ano - dados['an']
if dados['ctps'] != 0:
    dados['ac'] = int(input('Ano de contratação:'))
    dados['Salario'] = float(input('Salario:R$'))
    dados['a'] = dados['idade'] + ((dados['ac'] + 35) - datetime.date.today().year)
    print('=-'*30)
for a, v in dados.items():
    print(f'{a} tem valor de {v}')

