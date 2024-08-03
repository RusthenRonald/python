soma=0
cont=0
for c in range(0,2):
    n=float(input(f"Digite a {c+1}° nota"))
    soma+=n
    cont+=1
    media=soma/cont
print(f"Sua média foi de {media}")
if media <5 :
    print("Você está reprovado")
elif media >=5 and media <=6.9:
    print("Você está de recuperação")
else:
    print("Aprovado")
print("Fim")