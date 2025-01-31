produtos=("Lapis","1.75",
          "Borracha","2.00",
          "Caderno","15.90",
          "Estojo","25.00",
          "Compasso","9.99",
          "Mochila","120.32",
          "Canetas","22.30",
          "Livro","34.90",
          "Trasnferidor","4.20")
for p in range(0,len(produtos)):
    if p%2==0:
        print(f"{produtos[p]:.<30}R$",end="")
    else:
        print(f"{produtos[p]:>6}")
