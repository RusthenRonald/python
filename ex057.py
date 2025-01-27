num=int(input("Digite um número inteiro:"))
c=3
t1=0
t2=1
print(f"{t1}-{t2}",end="-")
while c <=num:
    c+=1
    t3=t1+t2
    t1=t2
    t2=t3
    print(f"{t3}",end="-")
print("FIM")
