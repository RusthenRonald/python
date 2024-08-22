valores=[]
while True:
    valores.append(int(input("Digite um número:")))
    r=str(input("Quer continuar?(S/N)")).strip().upper()[0]
    if r in "Nn":
        break
print(f"Foram digitados {len(valores)} números")
if 5 in valores:
    print("O número 5 foi digitado")
else:
    print("O número 5 não foi digitado!")
valores.sort(reverse=True)
print(valores)