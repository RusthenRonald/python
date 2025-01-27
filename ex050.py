tot_m=0
for c in range(0,5):
    print(f"{c+1}° Pessoa")
    nome=str(input("Nome:"))
    idade=int(input("Idade:"))
    sexo=str(input("Sexo: (M/F)")).strip().upper()
    if sexo in ["FEMININO","F"] and idade<20:
        tot_m+=1
    print("=-"*5)
print(f"Tem {tot_m} mulheres com menos de 20 anos")