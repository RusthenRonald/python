listagem=( "Arroz", 5.99,
    "Feijão", 7.49,
    "Macarrão", 3.29,
    "Leite", 4.69,
    "Açúcar", 2.99,
    "Café", 9.89)
for item in range(0,len(listagem)):
    if item%2==0:
        print(f"{listagem[item]:.<30}",end="")
    if item%2==1:
        print(f"R${listagem[item]:>5}")