dados={}
dados["Nome"]=str(input("Digite seu nome:"))
dados["Media"]=float(input(f"Média do aluno {dados['Nome']}"))
if dados["Media"]>=7:
    dados["Situação"]="Aprovado"
elif dados["Media"]>=5 and dados["Situação"]<7:
    dados["Situação"]="Recuperação"
else:
    dados["Situação"]="Reprovado otário!"
for k , v in dados.items():
    print(f"{k}:{v}")