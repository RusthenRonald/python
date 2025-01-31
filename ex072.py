lista=[]
maior=menor=0
for c in range(0,5):
    lista.append(int(input("Digite um valor:")))
    if c ==0:
        maior=lista[c]
        menor=lista[c]
    else:
        if lista[c]>maior:
            maior=lista[c]
        if lista[c]<menor:
            menor=lista[c]
print(lista)
print(maior)
print(menor)