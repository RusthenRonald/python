tot=0
num=int(input("Digite um número:"))
for c in range(1,num+1): 
    if num%c ==0:
        tot+=1
        print(f"\033[31m{c}\033[0m",end=" ")
    else:
        print(f"\033[33m{c}\033[0m",end=" ")
if tot>2 :
    print(f"\nO número {num} foi divisivel {tot}\n E por isso ele NÃO é PRIMO")
else:
    print(f"\nO número {num} foi divisivel {tot}\n E por isso ele É PRIMO")