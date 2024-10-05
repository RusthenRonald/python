from datetime import date
dados={}
ano_atual=date.today().year

dados["Nome"]=str(input("Nome:"))
dados["Ano de Nascimento"]=int(input("Ano de Nascimento:"))
dados["Carteira de Trabalho"]=int(input("Carteira de Trabalho (0 não tem):"))

for k,v in dados.items():
    print(f"- {k} {v}")