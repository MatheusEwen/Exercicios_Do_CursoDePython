palavras = ('aprender','programar','python',
            'linguagem','curso','gratis','estudar',
            'praticar','mercado','programador')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos:', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')