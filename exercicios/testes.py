dados={}
dados["Nome"]=str(input("Nome:"))
dados["Média"]=float(input("Mèdia:"))
if dados["Média"]>=7 :
    dados["situacao"]="Aprovado"
elif dados["Média"]>=5 and dados["Média"]<=7:
    dados["situacao"]="Recuperação"
else:
    dados["situacao"]="Reprovado"
for k , v in dados.items():
    print(f"{k} é igual a {v}")
