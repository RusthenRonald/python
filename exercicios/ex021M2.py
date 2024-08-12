import random
print("Vou pensar em um número entre 0 e 5 . Tente advinhar!")
computador=random.randint(0,5)
palpites=0
while True:
    jogador=int(input("Chute um número:"))
    if computador == jogador:
        print("Você ganhou!")
        print(f"O computador escolheu {computador} e você {jogador}")
        break
    else:
        print("Você perdeu")
        palpites+=1
        print("Tente novamente")
        if jogador >computador:
            print("Chute mais baixo")
        elif jogador<computador:
            print("Chute mais alto")
print(f"Foram necessários {palpites} palpites para acertar")
print("Fim")