nome=str(input("Digite seu nome completo :"))
print(f"Seu nome em maiúsculas fica {nome.upper()}")
print(f"Seu nome em minúsculas fica {nome.lower()}")
print(f"Seu nome ao todo tem {len(nome)-nome.count(" ")} letras")
lista=nome.split()
print(f"O primeiro nome tem {len(lista[0])} letras")
