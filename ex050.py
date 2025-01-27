tot_m=media=soma_idade=tot_p=maior_idade=0
for c in range(1,5):
    print(f"{c+1}° Pessoa")
    tot_p+=1
    nome=str(input("Nome:"))
    idade=int(input("Idade:"))
    soma_idade+=idade
    media=soma_idade/tot_p
    sexo=str(input("Sexo: (M/F)")).strip().upper()
    if sexo in ["FEMININO","F"] and idade<20:
        tot_m+=1
    if sexo in ["M","MASCULINO"]:
        if c ==1:
            maior_idade=idade
        else:
            if idade>maior_idade:
                maior_idade=idade
    print("=-"*5)
print(f"Tem {tot_m} mulheres com menos de 20 anos")
print(f"A media de idade do grupo é de {media} anos")
print(f"A maior idade é de {maior_idade}")