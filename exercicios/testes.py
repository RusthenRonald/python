dados=[]
principal=[]
maior=menor=cont=0
while True:
    dados.append(str(input("Digite seu nome:")))
    dados.append(float(input("Digite seu peso:")))
    if cont == 0:
        maior=menor=dados[1]
    else:
        if dados[1]>maior:
            maior=dados[1]
        if dados[1]<menor:
            menor=dados[1]
    cont+=1
    r=str(input("Quer continuar? (S/N)")).strip().upper()
    principal.append(dados[:])
    dados.clear()
    if r in ["NAO","N","NÂO"]:
        break
print(f"Foram cadastradas {len(principal)} pessoas")
print(principal)
print(f"A listagem de pessoas mais pesadas é ",end=" ")
for p in principal:
    if p[1] == maior:
        print(f"[{p[0]}]",end=" ")
print(f"\nA listagem de pessoas mais leves é ",end=" ")
for p in principal:
    if p[1] == menor:
        print(f"[{p[0]}]",end=" ")
