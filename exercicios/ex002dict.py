from random import randint
from time import sleep
result={}
rank={}
for c in range(0,5):
    result["jogador"]=randint(0,10)
    print(f"jogador{c} tirou {result['jogador']} no dado")
    sleep(0.8)
rank=sorted(result.items())
print("== RANKING DOS JOGADORES ==")
