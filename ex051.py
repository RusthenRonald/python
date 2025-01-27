sexo=str(input("Digite o seu sexo:[M/F]")).upper().strip()
while sexo not in ["M","F","MASCULINO","FEMININO"]:
    print("Dados inválidos. Por Favor ,",end=" ")
    sexo=str(input("digite o seu sexo:[M/F]")).upper().strip()
print(f"Sexo {sexo} cadastrado")
print("Fim")