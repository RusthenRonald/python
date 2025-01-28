import random
v=0
while True:
    num=int(input("Digite um valor:"))
    opc=str(input("Digite par ou impar (P/I):"))
    while opc not in "PpIi":
        opc=str(input("Digite par ou impar (P/I):"))
    computador=random.randint(0,10)
    total=num+computador
    print(f"Você jogou {num} e o computador {computador}. Total de {total}")
    if opc in "Pp":
        if total%2==0:
            print("Você vençeu!")
            v+=1
        else:
            print("Você perdeu!")
            break
    elif opc in "Ii":
        if total%2==1:
            print("Você vençeu!")
            v+=1
        else:
            print("Você perdeu!")
            break
print(f"Fim. Você venceu {v} vezes")