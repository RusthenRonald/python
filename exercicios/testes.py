dados={}
dados["Nome"]=str(input("Nome:"))
dados["Média"]=float(input("Mèdia:"))
if dados["Média"]>=7 :
    dados["Média"]="Aprovado"
elif dados["Média"]>=5 and dados["Média"]<=7:
    dados["Média"]="Recuperação"
else:
    dados["situacao"]="Reprovado"
print(dados)
