from random import randint
resultados={}
for c in range(0,4):
    resultados[f"Jogador_{c+1}"]=randint(0,6)
for k,v in resultados.items():
    print(f"{k} tirou {v} no dado.")