dados={}
principal=[]
lista_mulheres=[]
media=soma_idade=tot_idade=0
while True:
    dados["Nome"]=str(input("Nome:"))
    dados["Sexo"]=str(input("Sexo:"))
    if dados["Sexo"] in "Ff":
        lista_mulheres.append(dados["Nome"])
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
print(f"A media total foi de {media:.1f} anos")
print(f"As mulheres cadastradas foram ",end=" ")
for m in lista_mulheres:
    print(m,end=" ")