valores=[]
maior=menor=0
for c in range(0,5):
    valores.append(int(input("Digite um número:")))
    if c == 0:
        maior=menor=valores[c]
    else:
        if valores[c]>maior :
            maior=valores[c]
        if valores[c]<menor:
            menor=valores[c]
print(valores)
for i,v in enumerate(valores):
    if v == maior:
        print(f"O maior valor foi {maior} na posição {i+1}°")
    if v == menor:
        print(f"O menor valor foi {menor} e ele apareceu na posição {i+1}")