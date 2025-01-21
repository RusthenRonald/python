dist=float(input("Digite a distância da viagem:"))
if dist <=200:
    preco=0.50*dist
    print(f"Com uma distância de {dist} você pagará um valor de {preco}R$")
else:
    preco=0.45*dist
    print(f"Com uma distância de {dist} você pagará um valor de {preco}R$")