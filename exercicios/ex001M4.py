valores=[]
for cont in range(0,5):
    valores.append(int(input("Digite um número:")))
print("Os valores digitados foram:",end=" ")
for v in valores :
    print(v,end=" ")
print(f"\nO maior valor foi {max(valores)} e o menor valor foi {min(valores)}")