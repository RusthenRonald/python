num=(int(input("Digite um número:")),int(input("Digite um número:")),int(input("Digite um número:")),int(input("Digite um número:")))
print(f"Você digitou os valores {num}")
print(f"O número 9 apareceu {num.count(9)} vezes")
if 3 not in num:
    print("O número 3 não foi digitado nenhuma vez")
else:
    print(f"O primeiro valor 3 foi digitado na posição {num.index(3)+1}°")
print("Os valores pares mostrados foram:",end=" ")
for n in num:
    if n%2==0:
        print(n,end=" ")