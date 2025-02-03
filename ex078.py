valores=[[],[]]
for c in range(0,7):
    num=int(input(f"Digite o {c+1}° valor:"))
    if num%2==0:
        valores[0].append(num)
    elif num%2==1:
        valores[1].append(num)
print(f"Todos os valores foram {valores}")
print(f"Os valores pares digitados foram {sorted(valores[0])}")
print(f"Os valores impares digitados foram {sorted(valores[1])}")