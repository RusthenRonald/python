dados={}
while True:
    dados["Nome"]=str(input("Nome:"))
    dados["Sexo"]=str(input("Sexo")).strip().upper()

    while dados["Sexo"] not in ["M","F"]:#validação do sexo
        print("ERRO!, Por favor , digite apenas M ou F .")
        dados["Sexo"]=str(input("Sexo")).strip().upper()

    dados["Idade"]=int(input("Idade"))

    r=str(input("Quer continuar?")).strip().upper() # parada do while
    if r in ["NÂO","N","NAO"]:
        break
    while r not in ["S","N"]: # validação de saida
        print("ERRO! , Digite apenas S ou N")
        r=str(input("Quer continuar?")).strip().upper()
print("Fim")

