import random
a1=str(input("Digite o primeiro nome:"))
a2=str(input("Digite o segundo nome:"))
a3=str(input("Digite o terceiro nome:"))
a4=str(input("Digite o quarto nome:"))
list=[a1,a2,a3,a4]
random.shuffle(list)
print(f"A ordem de apresentação será {list}")