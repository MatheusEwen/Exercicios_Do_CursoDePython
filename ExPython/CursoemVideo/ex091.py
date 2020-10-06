import random
import time
from operator import itemgetter
competidores = {'jogador1': random.randint(1, 6),
                'jogador2': random.randint(1, 6),
                'jogador3': random.randint(1, 6),
                'jogador4': random.randint(1, 6)
                }
print('valores sorteados')
for c, i in competidores.items():
    print(f'O {c} tirou {i} nos dados')
    time.sleep(1)
posição = []
posição = sorted(competidores.items(), key= itemgetter(1), reverse=True)
print('=== Ranking ===')
for a, p in enumerate(posição):
    print(f'{a + 1}ºlugar = {p[0]} com {p[1]}')
    time.sleep(1)




