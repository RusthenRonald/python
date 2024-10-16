from random import randint
from operator import itemgetter
jogo={"Jogador_1":randint(0,6),
"Jogador_2":randint(0,6),
"Jogador_3":randint(0,6),
"Jogador_4":randint(0,6)}
rank=[]
for k , v in jogo.items():
    print(f"{k} tirou {v} no dado")
print("RANKING DOS JOGADORES")
rank=sorted(jogo.items(),key=itemgetter(1),reverse=True)
for i,v in enumerate(rank):
    print(f"{i+1} lugar: {v[0]} {v[1]}")