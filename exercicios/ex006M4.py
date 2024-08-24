principal=[]
dados=[]
cont=maior=menor=0
while True:
    print(f"{cont+1} pessoa")
    dados.append(str(input("Digite seu nome:")))
    dados.append(int(input("Digite seu peso:")))
    if len(principal)==0:
        maior=menor=dados[1]
    else:
        if dados[1]>maior:
            maior=dados[1]
        if dados[1]<menor:
            menor=dados[1]
    r=str(input("Quer continuar?"))
    principal.append(dados[:])
    dados.clear()
    cont+=1
    if r in "Nn":
        break
print(f"Foram cadastrados {len(principal)} pessoas")
print(f"O maior peso foi de {maior}Kg",end=" ")
for p in principal:
    if p[1]==maior:
        print(f"Peso de [{p[0]}]",end=" ")
print(f"O menor peso foi de {menor}Kg",end=" ")
for p in principal:
    if p[1]==menor:
        print(f"Peso de [{p[0]}]",end=" ")
print("\nFim")