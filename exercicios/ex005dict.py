dados={}
while True:
    dados["Nome"]=str(input("Nome:"))
    dados["Sexo"]=str(input("Sexo"))
    dados["Idade"]=int(input("Idade"))
    r=str(input("Quer continuar?")).strip().upper()
    if r in ["NÂO","N","NAO"]:
        break
    
