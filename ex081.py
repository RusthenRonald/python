temp=[]
principal=[]
while True:
    temp.append(str(input("Digite seu nome:")))
    temp.append(int(input("Digite a primeira nota:")))
    temp.append(int(input("Digite a segunda nota:")))
    principal.append(temp[:])
    temp.clear()
    r=str(input("Quer continuar? (S/N):"))
    if r in "Nn":
        break
print(principal)