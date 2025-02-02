valores=[]
pares=[]
impares=[]
while True:
    num=int(input("Digite um valor:"))
    if num%2==0:
        pares.append(num)
        valores.append(num)
    else:
        impares.append(num)
        valores.append(num)
    r=str(input("Digite se quer continuar? (S/N):"))
    if r in "Nn":
        break
print(valores)
print(pares)
print(impares)