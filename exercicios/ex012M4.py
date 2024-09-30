principal=[]
dados=[]
while True:
    dados.append(str(input("Nome:")))
    dados.append(float(input("Nota 1:")))
    dados.append(float(input("Nota 2:")))
    media=(dados[1]+dados[2])/2
    dados.append(media)
    principal.append(dados[:])
    dados.clear()
    r=str(input("Quer continuar?")).upper().strip()
    if r in ["NAO","N","NÂO"]:
        break
print(principal)
