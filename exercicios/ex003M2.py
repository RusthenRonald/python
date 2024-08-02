from datetime import date
nascimento=int(input("Digite seu ano de nascimento:"))
ano_atual=date.today().year
idade=ano_atual-nascimento
print(f"Quem nasceu em {nascimento} tem {idade} em {ano_atual}.")
if idade == 18 :
    print("Está na hora do seu alistamento!")
elif idade > 18 : 
    saldo=idade-18
    print("Já passou da hora de você se alistar")
    print(f"Você deveria ter se alistado há {saldo} anos")
else:
    saldo=18-idade
    print("Você ainda irá se alistar")
    print(f"Você irá se alistar daqui há {saldo} anos")