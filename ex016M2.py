num=int(input("Digite um número:"))
cont=0
for c in range(1,num+1):
    if num%c==0:
        print("\033[31m",end="")#divisivel#vermelho
        cont+=1
    else:
        print("\033[33m",end="")#naodivisivel#amarelo
    print(c,end="-")
if cont <=2:
    print(f"\nO número {num} é primo")
    print(f"Ele foi divisivel apenas {cont} vezes")
    print("Por isso ele é primo!")
else :
    print(f"\nO número {num} não é primo ")
    print(f"Ele foi divisivel {cont} vezes")
