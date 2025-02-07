temp=[]
principal=[]
media=soma=0
while True:
    temp.append(str(input("Digite seu nome:")))
    temp.append(int(input("Digite a primeira nota:")))
    temp.append(int(input("Digite a segunda nota:")))
    media=(temp[1]+temp[2])/2
    temp.append(media)
    principal.append(temp[:])
    temp.clear()
    r=str(input("Quer continuar? (S/N):"))
    if r in "Nn":
        break
print("Boletim")
print("=-"*15)
print(f"{"Pos"} {"Nome"} {"Média"}")
for i,v in enumerate(principal):
    print(f"{i} {v[0]} {v[3]}")
print("=-"*15)