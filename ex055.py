num=int(input("Digite um número para saber seu fatorial:"))
c=num
fat=1
while c>=1:
    print(c,end="")
    print("x" if c>1 else "=",end="")
    fat*=c
    c-=1
print(fat,end="")