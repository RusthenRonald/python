import datetime
nasc=int(input("Digite seu ano de nascimento:"))
ano_atual=datetime.datetime.now().year
idade=ano_atual-nasc
if idade<18:
    print(f"Quem nasceu em {nasc} tem {idade} anos em {ano_atual}")
    print(f"Você  ainda vai se alistar.")
    falta=18-idade
    print(f"Faltam {falta} anos para você se alistar")

elif idade == 18:
    print(f"Quem nasceu em {nasc} tem {idade} anos em {ano_atual}")
    print(f"Está na hora de se alistar.")
else:
    print(f"Quem nasceu em {nasc} tem {idade} anos em {ano_atual}")
    print(f"Já passou da hora de se alistar.")
    passou=idade-18
    print(f"Você devia ter se alistado a {passou} anos atras")