from datetime import date
dados={}
ano_atual=date.today().year
dados["Nome"]=str(input("Nome:"))
dados["Sexo"]=str(input("Sexo:")).upper().strip()
while dados["Sexo"] not in ["M","F"]:
    print("Por favor , digite apenas (M) ou (F)")
    dados["Sexo"]=str(input("Sexo:")).upper().strip()
ano_de_Nascimento=int(input("Ano de Nascimento:"))
dados["Idade"]=ano_atual-ano_de_Nascimento
if dados["Sexo"] in "Mm":
    idade_aposentadoria=65
if dados["Sexo"] in "Ff":
    idade_aposentadoria=62
dados["Carteira de Trabalho"]=int(input("Carteira de trabalho (0 não tem):"))
if dados["Carteira de Trabalho"]!= 0:
    dados["Ano de Contratação"]=int(input("Ano de Contratação:"))
    dados["Salário"]=int(input("Salário:"))
dados["aposentadoria"]=idade_aposentadoria-dados["Idade"]
print("=-"*15)
for k,v in dados.items():
    print(f" -{k} tem o valor {v}")