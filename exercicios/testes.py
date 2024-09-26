valores=[[],[]]
for c in range(0,7):
    valor=int(input("Digite um valor:"))
    if valor%2==0:
        valores[0].append(valor)
    elif valor%2==1:
        valores[1].append(valor)
print(f"Os valores são {valores}")
valores[0].sort()
valores[1].sort()
print(valores[0])
print(valores[1])