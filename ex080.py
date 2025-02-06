import random
import time
print("MEGA SENA")
cont=0
valores=[]
jogos=int(input("Quantos jogos serão gerados?"))
for c in range(0,jogos):
    computador=random.sample(range(1,60),6)
    valores.append(computador)
print(f"Sorteando {jogos} jogos")
for v in valores:
    cont+=1
    time.sleep(0.8)
    print(f"Jogo {cont}:{v}")