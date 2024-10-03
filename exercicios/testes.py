from random import randint
from time import sleep
from operator import itemgetter
dados={
    "jogador_1":randint(1,6),
    "jogador_2":randint(1,6),
    "jogador_3":randint(1,6),
    "jogador_4":randint(1,6)
}
rank=[]
for k , v in dados.items():
    print(f"{k} tirou {v} no dado")
    sleep(0.8)
print("RAKING DOS JOGADORES")
rank=sorted(dados.items(),key=itemgetter(1),reverse=True)
for i,v in enumerate(rank):
    print(f"{i}° lugar {v}")