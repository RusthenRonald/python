valores=[[],[]]
cont=0
for c in range(0,7):
    cont+=1
    num=int(input(f"Digite o {cont}° valor:"))
    if num%2==0:
        valores[0].append(num)
    elif num%2==1:
        valores[1].append(num)
valores[0].sort()
valores[1].sort()
print(f"Todos os valores {valores}")
print(f"Valores pares {valores[0]}")
print(f"Valores Impares {valores[1]}")