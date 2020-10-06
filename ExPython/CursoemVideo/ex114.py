import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('ERRO, o site pudim não esta acessivel no momento')
else:
    print('Consigui acessar o site pudim')