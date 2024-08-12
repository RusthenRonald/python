num=int(input("Digite um número para calcular seu fatorial:"))
c=num
f=1
while c >0:
    print(c,end="")
    print("x" if c >1 else "=",end="")
    f=f*c
    c-=1
print(f,end="")


























#import math
#num=int(input("Digite um número para calcular seu fatorial:"))
#print(math.factorial(num))