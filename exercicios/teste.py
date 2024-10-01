principal=[]
dados=[]
while True:
    dados.append(str(input("Nome:")))
    dados.append(float(input("Nota 1 :")))
    dados.append(float(input("Nota 2 :")))
    media=(dados[1]+dados[2])/2
    dados.append(media)
    principal.append(dados[:])
    dados.clear()
    r=str(input("Quer continuar?")).strip().upper()
    if r in ["N","NÂO","NAO"]:
        break
print("-="*10)
print(f"{"NOTA":<5}{"Nome":^7} {"Media":>5}")
print("-="*10)
for pos,a in enumerate(principal):
    print(f"{}")