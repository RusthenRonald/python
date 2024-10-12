dados={}
principal=[]
soma_idade=0
while True:
    dados["Nome"]=str(input("Nome:"))
    dados["Sexo"]=str(input("Sexo:")).strip().upper()

    while dados["Sexo"] not in ["M","F"]:#validação do sexo
        print("ERRO!, Por favor , digite apenas M ou F .")
        dados["Sexo"]=str(input("Sexo")).strip().upper()

    dados["Idade"]=int(input("Idade:"))
    principal.append(dados.copy())
    soma_idade+=dados["Idade"]
    r=str(input("Quer continuar?")).strip().upper() # parada do while
    if r in ["NÂO","N","NAO"]:
        break
    while r not in ["S","N"]: # validação de saida
        print("ERRO! , Digite apenas S ou N")
        r=str(input("Quer continuar?")).strip().upper()
media=soma_idade/len(principal)
print("Fim")
print(f"Foram cadastradas {len(principal)} pessoas.")
print(f"A média de idade é de {media} anos.")
print("As mulheres cadastradas foram: ",end=" ")
for p in principal:
    if p["Sexo"] == "F":
        print(f"{p['Nome']}",end=" ")
print()
print("Lista com pessoas acima da média:",end=" ")
for p in principal:
    if p["Idade"]>media:
        print(f"{p["Nome"]}",end=" ")

