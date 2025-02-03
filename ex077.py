dados=[]
principal=[]
maior=menor=0
while True:
    dados.append(str(input("Nome:")))
    dados.append(float(input("Peso:")))
    if len(principal)==0:
        maior=menor=dados[1]
    else:
        if dados[1]>maior:
            maior=dados[1]
        if dados[1]<menor:
            menor=dados[1]
    principal.append(dados[:])
    dados.clear()
    r=str(input("Quer continuar? (S/N):"))
    if r in "Nn":
        break
print(principal)
print(f"Foram cadastradas {len(principal)} pessoas.")
print("A listagem das pessoas com maior peso foi de :")
for p in principal:
    if p[1]==maior:
        print(f" {p[0]} ")
print("=-"*10)
print("A listagem de pessoas com menor peso foi de :")
for p in principal:
    if p[1]==menor:
        print(f"{p[0]}")