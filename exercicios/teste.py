valores=(int(input("digite um número")),int(input("digite um número")),int(input("digite um número")),int(input("digite um número")))
print("Os valores foram:",end=" ")
for v in valores :
    print(v,end=" ")
if 9 in valores:
    print()
    print(f"O número 9 apareceu {valores.count(9)} vezes")
else:
    print()
    print("O número 9 não estava na tupla!")
if 3 in valores:
    print(f"O primeiro valor 3 foi digitado na posição {valores.index(3)+1}° posição")
else:
    print("O número 3 não estava na tupla!")
for v in valores :
    if v%2==0:
        print("Os números pares foram :",end=" ")
        print(f"{v}",end="")
    else:
        print("Só tem números impares")