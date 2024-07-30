import random
print("Vou pensar em um número entre 0 e 5 . Tente advinhar!")
num=int(input("Digite um número entre 0 e 5:"))
computador=random.randint(0,5)
if num == computador:
    print(f"Parabéns , você acertou! , o número escolhido foi {computador})")
else: 
    print("Lamento, Você errou!" )
    print(f"Eu escolhi o número {computador} e você digitou o {num}")
