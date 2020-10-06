

def voto(ano):
    import datetime
    atual = datetime.date.today().year
    idade = atual - ano
    if 18 <= idade <= 64:
        return 'Voto Obrigatorio'
    elif idade < 16:
        return 'Negado'
    elif 16 <= idade < 18 or idade > 65:
        return 'Voto Opcional'



anon = int(input("digite o ano em que você nasceu:"))
print(voto(anon))