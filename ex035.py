n1=float(input("Digite a primeira nota:"))
n2=float(input("Digite a segunda nota:"))
media=(n1+n2)/2
if media < 5:
    print(f"Sua média é de {media} ")
    print("Reprovado!")
elif media >=5 and media <=6.9:
    print(f"Sua média é de {media} ")
    print("Recuperação")
else:
    print(f"Sua média é de {media} ")
    print("Aprovado!")