dist=float(input("Digite a distância da viagem:"))
if dist <=200 :
    preco=0.50*dist
    print(f"O total a ser pago para uma viagem de {dist} km é de {preco} R$")
else:
    preco=0.45*dist
    print(f"O total a ser pago para uma viagem de {dist} km é de {preco}R$")