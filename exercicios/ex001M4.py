valores=[]
maior=menor=0
for cont in range(0,5):
    valores.append(int(input(f"Digite um número para a posição {cont+1}° :")))
    if cont ==0:
        maior=menor=valores[cont]
    else:
        if valores[cont]>maior:
            maior=valores[cont]
        if valores[cont]<menor:
            menor=valores[cont]


