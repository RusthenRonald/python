dados={}
principal=[]
media=soma_idade=0
while True:
    dados["Nome"]=str(input("Nome:"))
    dados["Sexo"]=str(input("Sexo:"))
    dados["Idade"]=int(input("Idade:"))
    principal.append(dados.copy())
    dados.clear()
    r=str(input("Quer continuar? (S/N):")).strip()
    if r in "Nn":
        break
print(principal)
print(f"Ao todo tem {len(principal)} pessoas cadastradas")