from datetime import date
dados={}
ano_atual=date.today().year
aposentadoria=70
dados["Nome"]=str(input("Nome:"))
ano_nasc=int(input("Ano de Nascimento:"))
dados["Idade"]=ano_atual-ano_nasc
dados["Carteira de Trabalho"]=int(input("Carteira de Trabalho (0 não tem):"))
if dados["Carteira de Trabalho"]!=0:
    dados["Ano de contratação"]=int(input("Ano de contratação:"))
    dados["Salário"]=float(input("Salário:"))
    dados["Aposentadoria"]=aposentadoria-dados["Idade"]

for k,v in dados.items():
    print(f"- {k} {v}")