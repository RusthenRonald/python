soma=0
for c in range(0,6):
    n=int(input("Digite um número:"))
    if n%2==0:
        soma+=n
print(f"A soma dos número pares é de {soma}")
print("Fim")