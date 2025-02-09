import datetime
trabalhador={}
ano_atual=datetime.date.today().year
trabalhador["Nome"]=str(input("Nome:"))
trabalhador["Ano de nascimento"]=int(input("Ano de nascimento:"))
idade=ano_atual-trabalhador["Ano de nascimento"]
trabalhador["Carteira de trabalho"]=int(input("Carteira de Trabalho:"))
print(idade)