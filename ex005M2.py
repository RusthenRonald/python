from datetime import date
nascimento=int(input("Digite seu ano de nascimento:"))
ano_atual=date.today().year
idade=ano_atual-nascimento
if idade <=9:
    print("Classificação: Mirim")
elif idade >9 and idade <=14:
    print("Classificação: Infantil")
elif idade >14 and idade <=19:
    print("Classificação: Junior")
elif idade > 19 and idade <=25 :
    print("Classificação: Sênior")
else:
    print("Classificação: Master")