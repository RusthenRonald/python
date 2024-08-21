valores=[]
while True:
    num=int(input("Digite um número:"))
    if num not in valores:
        valores.append(num)
    else:
        print("Número ja está na lista , não vou adcionar!")
    r=str(input("Quer continuar?")).strip().upper()
    if r in ["NAO","N","NÂO"]:
        break
valores.sort()
print(valores)
print("Fim")