import datetime
nasc=int(input("Digite seu ano de nascimento:"))
ano_atual=datetime.datetime.now().year
idade=ano_atual-nasc
if idade<=9:
    print(f"O atleta tem {idade} anos")
    print("Classificação : Mirim")
elif idade>9 and idade <=14:
    print(f"O atleta tem {idade} anos")
    print("Classificação : Infantil")
elif idade>14 and idade<=19:
    print(f"O atleta tem {idade} anos")
    print("Classificação : Junior")
elif idade>19 and idade<=25:
    print(f"O atleta tem {idade} anos")
    print("Classificação : Sênior")
else:
    print(f"O    atleta tem {idade} anos")
    print("Classificação : Master")