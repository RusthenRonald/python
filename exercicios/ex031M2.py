valor=int(input("Digite o valor a ser sacado:"))
total=valor
ced=50
totced=0
while True:
    if total>=ced:#quantas vezes eu consigo tirar 50 do total
        total-=ced
        totced+=1
    else:#se n der pra tirar
        print(f"Total de {totced} de cédulas de R${ced}")
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=1
        totced=0
        if total==0:
            break