c=0
cont_maior_idade=0
homens_cadas=0
cont_mulher_menos=0
while True:
    print(f"{c+1}° pessoa")
    idade=int(input("Digite a sua idade:"))
    sexo=str(input("Digite seu sexo:")).strip().upper()
    while sexo not in ["MASCULINO","FEMININO","F","M"]:
        sexo=str(input("Digite seu sexo:")).strip().upper()#validação de sexo

    if sexo in ["MASCULINO","M"]:#contador de homens cadastrados
        homens_cadas+=1
    if sexo in ["FEMININO","F"] and idade<20:
        cont_mulher_menos+=1
    c+=1
    if idade >18:
        cont_maior_idade+=1
    print("Cadastro concluido")
    r=str(input("Quer continuar?")).strip().upper()
    if r not in ["SIM","S"]:
        break
print(f"Tem {cont_maior_idade} pessoas com mais de 18 anos")
print(f"Foram cadastrados {homens_cadas} homens")
print(f"Tem {cont_mulher_menos} mulheres com menos de 20 anos")
print("Fim")