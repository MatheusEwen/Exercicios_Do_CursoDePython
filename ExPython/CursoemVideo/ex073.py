times = ('atletico.p','internacional','atletico.m','gremio','atletico.g','vasco da gama','Bahia',
         'São Paulo','Sport','Bragantino','Botafogo','Palmeiras','Ceara','Fluminense','Santos',
         'Corintians','Goias','Coritiba','Fortaleza','Flamengo')
print(f'lista de times{times}')
print(f'Primeiros cinco colocados {times[0:5]}')
print(f'Utimos 4 colocados {times[-4:]}')
print('Em ordem alfabetica',sorted(times))
time = times.index('São Paulo')
print(f'O São Paulo esta na {time + 1}º posição')
