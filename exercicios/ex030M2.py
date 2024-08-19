total=cont_mais_mil=c=menor=nome_menor=0
while True:
    nome=str(input("Digite o nome do produto:"))
    preco=float(input("Digite o preco do produto:"))
    c+=1
    if preco>1000:
        cont_mais_mil+=1
    if c ==1:
        menor=preco
        nome_menor=nome
    else:
        if preco<menor:
            menor=preco
            nome_menor=nome
    r=str(input("Quer continuar?")).strip().upper()
    total+=preco
    if r not in ["SIM","S"]:
        break
print(f"O total gasto na compra foi de {total}R$")
print(f"O nome do produto mais barato é {nome_menor} e ele custa {menor}R$")
print(f"Tem {cont_mais_mil} produtos que custam mais de 1000R$")
print("Fim")