dados={}
principal=[]
media=soma_idade=tot_idade=0
while True:
    dados["Nome"]=str(input("Nome:"))
    dados["Sexo"]=str(input("Sexo:"))
    dados["Idade"]=int(input("Idade:"))
    soma_idade+=dados["Idade"]
    tot_idade+=1
    media=soma_idade/tot_idade
    principal.append(dados.copy())
    dados.clear()
    r=str(input("Quer continuar? (S/N):")).strip()
    if r in "Nn":
        break
print(principal)
print(f"Ao todo tem {len(principal)} pessoas cadastradas")
print(f"A media total foi de {media} anos")