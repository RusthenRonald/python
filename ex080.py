import random
import time
print("MEGA SENA")
valores=[]
jogos=int(input("Quantos jogos serão gerados?"))
for c in range(0,jogos):
    computador=random.sample(range(1,60),6)
    valores.sort()
    valores.append(computador)
print(f"Sorteando {jogos} jogos")
for i,v in enumerate(valores):
    time.sleep(0.8)
    print(f"Jogo {i+1}:{v}")