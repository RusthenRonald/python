import time
import random
computador=random.randint(0,2)
print('''
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador=int(input("Qual a sua jogada:"))
print("JO")
time.sleep(1.4)
print("KEN")
time.sleep(1.4)
print("PO")
#pedra
if jogador == 0 and computador == 0:
    print("EMPATE")
    print("Ambos escolheram PEDRA")
if jogador == 0 and computador == 1:
    print("DEORROTA")
    print("O jogador escolheu PEDRA e o computador PAPEL")
if jogador == 0 and computador ==2:
    print("VITORIA")
    print("O jogador escolheu PEDRA e o computador TESOURA")
#papel
if jogador == 1 and computador ==1:
    print("EMPATE")
    print("Ambos escolheram PAPEL")
if jogador == 1 and computador == 0:
    print("VITORIA")
    print("O jogador escolheu PAPEL e o computador PEDRA")
if jogador == 1 and computador == 2:
    print("DEORROTA")
    print("O jogador escolheu PAPEL e o computador TESOURA")
#tesoura
if jogador == 2 and computador == 2:
    print("EMPATE")
    print("Ambos escolheram TESOURA")