valor=float(input("Qual será o valor a ser sacado:"))
totced=0
ced=50
while True:
    if valor>=ced:
        valor-=ced
        totced+=1
    else:
        print(f"Total de {totced} cédulas de R${ced}")
        if ced ==50:
            ced=20
        elif ced ==20:
            ced=10
        elif ced==10:
            ced=1
        if valor==0:
            break