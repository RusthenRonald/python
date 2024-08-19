from random import randint
numeros=(randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5))
print("Os valores sorteados foram:",end=" ")
for n in numeros:
    print(n,end=" ")
print(f"\nO maior valor é {max(numeros)} e o menor é {min(numeros)}")