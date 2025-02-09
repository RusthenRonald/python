aluno={}
aluno["nome"]=str(input("Nome:"))
aluno["Media"]=float(input("Média:"))
if aluno["Media"]>=7:
    aluno["Situação"]="Aprovado"
elif aluno["Media"]>=6 and aluno["Media"]<7:
    aluno["Situação"]="Recuperação"
else:
    aluno["Situação"]="Reprovado"

for k, v in aluno.items():
    print(f"{k}: {v}")