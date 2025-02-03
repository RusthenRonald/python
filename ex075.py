valores=[]
while True:
    num=int(input("Digite um valor:"))
    valores.append(num)
    r=str(input("Quer continuar? (S/N):"))
    if r in "Nn":
        break
print(valores)
print(f"Foram digitados {len(valores)} números")
print(f"A lista ordenada de forma decrescente é {sorted(valores,reverse=True)}")
if 5 in valores:
    print(f"O valor 5 foi digitado e está na lista na posição {valores.index(5)}!")
else:
    print("O valor 5 não foi digitado!")