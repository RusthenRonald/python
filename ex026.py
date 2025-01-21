velo=float(input("Digite a velociade do carro:"))
multa=(velo-80)*7
if velo>80:
    print("Você foi multada!")
    print(f"Você devera pagar uma multa de {multa}R$")
else:
    print("Bom dia ! Diriga com segurânça.")