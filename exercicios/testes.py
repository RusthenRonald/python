dados=[]
principal=[]
maior=menor=0
while True:
    dados.append(str(input("Digite seu nome:")))
    dados.append(float(input("Digite seu peso:")))
    r=str(input("Quer continuar? (S/N)")).strip().upper()
    principal.append(dados[:])
    dados.clear()
    if r in ["NAO","N","NÂO"]:
        break
print(f"Foram cadastradas {len(principal)} pessoas")