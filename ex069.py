valores=(
    int(input("Digite um valor:")),
    int(input("Digite um valor:")),
    int(input("Digite um valor:")),
    int(input("Digite um valor:"))
)
print(valores)
print(f"O valor 9 apareceu {valores.count(9)} vezes")
print(f"O primeiro valor 3 foi digitado na posição {valores.index(3)+1}°")
print("Os valores pares são:",end=" ")
for v in valores:
    if v%2==0:
        print(v,end="")