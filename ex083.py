import random
import time
import operator
jogo={}
for c in range(1,5):
    jogo[f"Jogador{c}"]=random.randint(1,6)
for k,v in jogo.items():
    print(f"{k} jogou o dado {v}")
    time.sleep(1)
print("=-"*15)
print("RANKING DOS JOGADORES")
ranking=[]
ranking=sorted(jogo.items(),key=operator.itemgetter(1),reverse=True)
for i,v in enumerate(ranking):
    print(f"{i+1}° {v[0]} com {v[1]}")