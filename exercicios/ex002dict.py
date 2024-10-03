from random import randint
from time import sleep
from _operator import itemgetter
result={
    "jogador1":randint(0,6),
    "Jogador2":randint(0,6),
    "jogador3":randint(0,6),
    "jogador4":randint(0,6)
}
rank={}
for k,v in result.items():
    print(f"{k}:{v}")
    sleep(0.8)
rank=sorted(result.items(),key=itemgetter(1),reverse="True")
print("== RANKING DOS JOGADORES ==")
for i,v in enumerate(rank):
    print(f"{i+1}° lugar: {v[0]} com {v[1]} pontos")
