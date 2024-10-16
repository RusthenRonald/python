dados={}
dados["Nome"]=str(input("Nome:"))
dados["Média"]=float(input("Média:"))
if dados["Média"]>=7:
    dados["Situação"]="Aprovado"
elif dados["Média"]>=5 and dados["Média"]<7:
    dados["Situação"]="Recuperação"
else:
    dados["Situação"]="Reprovado"
for k , v in dados.items():
    print(f"{k } é igual á {v}")