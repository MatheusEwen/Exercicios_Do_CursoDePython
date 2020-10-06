n = int(input('digite um numero para saber quanto ele é em centimetros e milimetros:'))
km = (n/1000)
hm = (n/100)
dam = (n/10)
dc = (n*10)
cm = (n*100)
mm = (n*1000)


print('O numero em km é {}\nhm é {}\ndam é {}\ndc é {}\ncm é {}\nmm é {}'.format(km, hm, dam, dc, cm, mm))