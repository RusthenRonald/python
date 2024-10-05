from random import randint
from operator import itemgetter
resultados={}
for c in range(0,4):
    resultados[f"Jogador_{c+1}"]=randint(0,6)
for k,v in resultados.items():
    print(f"{k} tirou {v} no dado.")
rank=[]
print("RANKING DOS JOGADORES")
rank=sorted(resultados.items(),key=itemgetter(1),reverse=True)
for i,v in enumerate(rank):
    print(f"{i+1}° lugar o {v[0]} com {v[1]}.")
