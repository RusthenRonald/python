import random
while True:
    num=int(input("Digite um valor:"))
    opc=str(input("Digite par ou impar (P/I):"))
    computador=random.randint(0,10)
    total=num+computador
    print(f"Você jogou {num} e o computador {computador}.")