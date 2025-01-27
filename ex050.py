tot_m=0
for c in range(0,5):
    print(f"{c+1}° Pessoa")
    nome=str(input("Nome:"))
    idade=int(input("Idade:"))
    sexo=str(input("Sexo:")).strip().upper()
    if sexo in ["M","MULHER","FEMININO","F"] and idade<20:
        tot_m+=1
    print("=-"*5)