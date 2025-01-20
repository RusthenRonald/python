nome=str(input("Digite seu nome completo:")).strip().upper()
separar=nome.split()
print(f"Seu primeiro nome é {separar[0]}")
print(f"Seu ultimo nome é {separar[-1]}")