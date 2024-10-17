dados={}
principal=[]
while True:
    dados["Nome"]=str(input("Nome:"))

    dados["Sexo"]=str(input("Sexo:")).upper().strip()
    while dados["Sexo"] not in ["M","F"]:
            dados["Sexo"]=str(input("Sexo:")).upper().strip()
    dados["Idade"]=int(input("Idade:"))

    r=str(input("Quer continuar?")).upper().strip()
    while r not in ["S","N"]:
        print("Digite apenas (S) ou (N)")
        r=str(input("Quer continuar?")).upper().strip()
    principal.append(dados.copy())
    dados.clear()
    if r in "N":
        break

print(f"Foram cadastradas {len(principal)} pessoas")