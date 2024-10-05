dados={}
dados["Nome"]=str(input("Nome:"))
dados["Média"]=float(input("Mèdia:"))
if dados["situaçao"]>=7 :
    dados["situaçao"]="Aprovado"
for k,v in dados.items():
    print(f"{k} :{v} ")

