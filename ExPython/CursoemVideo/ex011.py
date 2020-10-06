largura=float(input('digite qual a largura da sua parede:'))
comprimento=float(input('digite qual o comprimento da sua parede:'))
quantidade=((largura*comprimento)/2)
print('A area da sua parede é de',(largura*comprimento),'para pintar sua parede será necessario {} litros de tinta'.format(quantidade))