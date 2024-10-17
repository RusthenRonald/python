dados={}
while True:
    dados["Nome"]=str(input("Nome:"))
    dados["Sexo"]=str(input("Sexo:"))
    dados["Idade"]=int(input("Idade:"))
    r=str(input("Quer continuar?")).upper().strip()
    while r not in ["S","N"]:
        r=str(input("Quer continuar?")).upper().strip()
    if r in "N":
        break
print("fim")