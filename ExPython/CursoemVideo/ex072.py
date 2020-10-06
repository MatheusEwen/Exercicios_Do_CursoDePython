r = int(input('Digite um número de 0 a 20:'))
while r > 20 or r < 0:
    r = int(input('Tente novamente.Digite um número de 0 a 20:'))

n = 'zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'
print(f'você digitou o numero {n[r]}')