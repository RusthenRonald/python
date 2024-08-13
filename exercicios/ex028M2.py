import random
print("Vamos jogar Par ou Ìmpar")
computador=random.randint(0,10)
v=0
while True:
    jogador=int(input("Digite um valor:"))
    opcao=str(input("[P/I]:")).upper().strip()
    while opcao not in ["PAR","IMPAR","P","I"]:#validação par ou impar
        opcao=str(input("[P/I]:")).upper().strip()
    total=jogador+computador
    print(f"Você jogou {jogador} e o computador {computador}. Total de {total}")
    if opcao == "PAR"or"P":
        if total%2==0:
            print("Você ganhou!")
            v+=1
        else:
            print("Você perdeu!")
            break
    elif opcao =="IMPAR"or"I":
        if total%2==1:
            print("Você ganhou!")
            v+=1
        else:
            print("Você perdeu!")
            break
    print("Vamos jogar novamente")
print("Game Over!")
print(f"Você teve um total de {v} vitorias")

