import datetime
trabalhador={}
ano_atual=datetime.date.today().year
trabalhador["Nome"]=str(input("Nome:"))
nasc=int(input("Ano de nascimento:"))
idade=ano_atual-nasc
trabalhador["Idade"]=idade
trabalhador["Carteira de trabalho"]=int(input("Carteira de Trabalho:"))
if trabalhador["Carteira de trabalho"]!=0:
    trabalhador["Ano de Contratação"]=int(input("Ano de Contratação:"))
    trabalhador["Salário"]=float(input("Salário:"))
    aposentar=65-idade
    trabalhador["Aposentadoria"]=aposentar
else:
    print("Fim")
print("=-"*15)
for k,v in trabalhador.items():
    print(f"-{k} tem o valor {v}")