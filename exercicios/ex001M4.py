valores=[]
maio=menor=0
for cont in range(0,5):#contagem de 5 vezes e adcionamento em lista
    valores.append(int(input("digite um número:")))
    if cont==0:#verificação maior e menor valor
        maior=menor=valores[cont]
    else:
        if valores[cont]>maior:
            maior=valores[cont]
        if valores[cont]<menor:
            menor=valores[cont]
print("Os valores digitados foram:",end=" ")
print(valores)
print(f"O maior valor digitado foi {maior} ",end="")
for p,v in enumerate(valores):#encontrar a posição do maior
    if v ==maior:
        print(f" Na posição {p+1}°",end=" ")
print(f"\nE o menor foi {menor}",end=" ")
for p,v in enumerate(valores):#encontrar a posição do menor
    if v ==menor:
        print(f"Na posição {p+1}°",end=" ")



