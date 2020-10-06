n = str(input('digite seu nome:')).strip()
nome = n.split()
print('o seu primeiro nome è:', nome[0])
print('seu ultimos nome é {}'.format(nome[len(nome)-1]))
