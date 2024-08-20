valores=[]
for cont in range(0,5):
    valores.append(int(input("Digite um número:")))#laço que ja pergunta e joga na lista
for p,v in enumerate(valores) :
    print(f"Na posição {p+1}° encontrei o valor {v}")