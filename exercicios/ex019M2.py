cont_menos_20=0
soma_idade=0
cont=0
velho=0
nome_velho=" "
for c in range(1,4+1):
    print("="*15)
    print(f"{c}° pessoa")
    nome=str(input("Nome:"))
    idade=int(input("Idade:"))
    sexo=str(input("Sexo:")).strip().upper()
    if c ==1 and sexo in ["MASCULINO","M"]:
        velho=idade
        nome_velho=nome
    else:
        if idade> velho and sexo in ["MASCULINO","M"]:
            velho=idade
            nome_velho=nome
    soma_idade+=idade
    cont+=1
    print("="*15)
    if sexo not in ["MASCULINO" , "FEMININO","M","F"]:#validação de sexo
        print("Sexo inválido, Encerrando.....")
        break
    if sexo in ["FEMININO","F"] and idade <20:#mulheres com menos de 20 anos
        cont_menos_20+=1
media=soma_idade/cont
print(f"O nome da pessoa mais velha é {nome_velho} e ela tem {velho} anos")
print(f"A média de idade do grupo é de {media}")
print(f"Tem {cont_menos_20} mulheres com menos de 20 anos")