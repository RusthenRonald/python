from random import randint
print("Vou pensar em num número entre 0 e 5 . Tente advinhar!")
num=int(input("Digite em que número eu pensei:"))
computador=randint(0,5)
if computador == num :
    print(f"Você acertou !\n Eu pensei no número {computador} e você no {num}")
else:
    print(f"Você errou! \n Eu pensei no número {computador} e você no {num}")