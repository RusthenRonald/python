principal=[]
tempo=[]
cont=maior=menor=0
while True:
    print(f"{cont+1}° pessoa")
    tempo.append(str(input("Digite seu nome:")))
    tempo.append(float(input("Digite seu peso:")))
    if cont==0:
        maior=menor=tempo[1]
    else:
        if tempo[1]>maior:
            maior=tempo[1]
        if tempo[1]<menor:
            menor=tempo[1]
    principal.append(tempo[:])
    tempo.clear()
    cont+=1
    r=str(input("Quer continuar? (S/N):"))
    if r in "Nn":
        break
print(principal)
print(f"Foram cadastradas {cont} pessoas:")
print(f"O maior peso foi de {maior}kg")
for p in principal:
    if p[1]==maior:
        print(f" {p[0]}")
print(f"O menor peso foi de {menor}Kg")
for p in principal:
    if p[1]==menor:
        print(f"{p[0]}")
print("Fim")