valores=[]
pares=[]
impares=[]
while True:
    num=int(input("Digite um número:"))
    if num%2==0:
        pares.append(num)
        valores.append(num)
    elif num%2==1:
        impares.append(num)
        valores.append(num)
    r=str(input("Quer continuar?")).strip().upper()
    if r in ["N","NÂO","NAO"]:
        break
print(valores)
print(pares)
print(impares)