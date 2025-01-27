import random
tot=0
print("Sou seu computador vou pensar em um número entre 0 e 10")
jogador=int(input("Qual é seu palpite:"))
computador=random.randint(0,10)
while computador != jogador:
    if computador>jogador:
        print("Mais...")
    else:
        print("Menos...")
    print("Você errou. Tente novamente.",end=" ")
    tot+=1
    jogador=int(input("Qual é seu palpite:"))
print(f"Você acertou em {tot} tentativas. Você digitou o número {jogador} e o computador {computador}")
