n1 = float(input('Digite a nota 1 do aluno:'))
n2 = float(input('Digite a nota 2 do aluno:'))
media = (n1 + n2)/2
if media < 5:
    print('reprovado, a media do aluno foi {:.1f}'.format(media))
elif media > 5 and media < 6.9:
    print('ALUNO DE RECUPERAÇÃO,a media do aluno foi {:.1f}'.format(media))
else:
    print('Aluno foi APROVADO, a media do aluno foi {:.1f}'.format(media))
