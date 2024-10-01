aluno={}
aluno["nome"]=str(input("Nome:"))
aluno["Media"]=float(input(f"Média de {aluno['nome']}"))
if aluno["Media"]>=7:
    aluno["Situação"]="Aprovado"
elif aluno["Media"]>=5 and aluno["Media"]<7:
    aluno["Situação"]="recuperação"
else:
    aluno["Situação"]="Reprovado"
for k , v in aluno.items():
    print(f"{k}: {v}")