total=mil=barato=nome_barato=c=0
while True:
    nome=str(input("Digite o nome do produto:"))
    preco=float(input("Digite o preço do produto R$:"))
    c+=1
    total+=preco
    if preco>1000:
        mil+=1
    if c ==1:
        barato=preco
        nome_barato=nome
    else:
        if preco < barato:
            barato=preco
            nome_barato=nome
    r=str(input("Digite se quer continuar (S/N):"))
    if r in "Nn":
        break
print(f"Tem um total de {c} produtos")
print(f"O total gasto na compra foi de {total}")
print(f"{mil} produtos custam mais de 1000 R$")
print(f"O produto mais barato é {nome_barato} e ele custa {barato}R$")
