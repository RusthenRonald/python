from random import randint
result={}
for c in range(0,5):
    result["jogador"]=randint(0,10)
    print(f"jogador{c} tirou {result['jogador']}")
print("== RANKING DOS JOGADORES ==")
