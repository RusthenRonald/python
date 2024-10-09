from datetime import date
ano_atual=date.today().year
dados={}
dados["Nome"]=str(input("Nome:"))
Ano_de_Nascimento=int(input("Ano de Nascimento:"))
idade=ano_atual-Ano_de_Nascimento
dados["Idade"]=idade
dados["Carteira de trabalho"]=int(input("Carteira de trabalho (0 não tem):"))
if dados["Carteira de trabalho"]!=0:
    dados["Ano de contratação"]=int(input("Ano de contratação:"))
    dados["Salário"]=float(input("Salário:"))
for k,v in dados.items():
    print(f"{k} tem o valor {v}")
print("Fim")