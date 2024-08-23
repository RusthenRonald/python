galera=[]
dado=[]
for cont in range(0,3):
    dado.append(str(input("Digite seu nome:")))
    dado.append(int(input("Digite sua idade:")))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1]>=21:
        print(f"{p[0]} é maior de idade!")
    else:
        print(f"{p[0]} é menor de idade")