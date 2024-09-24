valores=[]
while True:
    valores.append(int(input("Digite um número:")))
    r=str(input("Quer continuar?")).strip().upper()
    if r in ["N","NAO","NÂO"]:
        break

print(f"Foram digitados {len(valores)} números")
if 5 not in valores:
    print("O número 5 não foi digitado!")
else:
    posicao=valores.index(5)
    print(f"O valor 5 foi digitado e está na posição {posicao+1}° ")
valores.sort(reverse=True)
print(valores)
print("Fim")