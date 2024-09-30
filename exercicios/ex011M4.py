from random import sample
from time import sleep
cont=0
print("-="*10)
print("JOGA NA MEGASENA")
print("-="*10)
sorteio=[]
quant_jogos=int(input("Digite a qauntidade de jogos :"))
for c in range(0,quant_jogos):
    computador=sample(range(1, 61), 6)
    sorteio.append(computador)
for s in sorteio:
    sleep(0.5)
    print(f" Jogo {cont+1}° {sorted(s)}")
    cont+=1
