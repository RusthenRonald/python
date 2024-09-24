valores=[]
while True:
    num=int(input("Digite um número:"))
    if num not in valores:
        valores.append(num)
    else:
        print("Número repetido! \nnão vou adcionar")
    r=str(input("Quer continuar?")).strip().upper()
    if r in ["N","NÂO","NAO"]:
        break
print("Você digitou os números:",end=" ")
valores.sort()
print(valores)
print("Fim")