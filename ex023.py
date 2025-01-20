frase=str(input("Digite uma frase:")).strip().upper()
print(f"A letra A apareceu {frase.count('A')} vezes")
print(f"A letra A apareceu pela primeira vez na posição {frase.find('A')}")
print(f"A letra A apareceu pela ultima vez na posição {frase.rfind('A')}")