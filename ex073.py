valores=[]
while True:
    valor=int(input("Digite um valor:"))
    if valor not in valores:
        print("Valor adicionado!")
        valores.append(valor)
    else:
        print("Valor repetido!")
    r=str(input("Você quer continuar?"))
    if r in "Nn":
        break
    valores.sort()#modifica a original
print(f"Os valores digitados foram {sorted(valores)}")