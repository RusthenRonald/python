sexo=str(input("Digite seu sexo:")).strip().upper()
while sexo not in ["MASCULINO","FEMININO","M","F"]:
    print("Dados inválidos")
    print("Tente novamente")
    sexo=str(input("Digite seu sexo:")).strip().upper()
print(f"Sexo {sexo.capitalize()} cadastrado com sucesso")
print("Fim")