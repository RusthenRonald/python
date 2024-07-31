velo=int(input("Digite a velocidade do carro:"))
if velo>80:
    print(f"Você foi multado , sua velocidade foi de {velo}km/h")
    multa=(velo-80)*7
    print(f"Você irá receber uma multa de {multa}R$")
else:
    print("Tenha um bom dia , diriga com segurânça")