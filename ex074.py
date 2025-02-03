valores=[]
for c in range(1,6):
    num=int(input("Digite um valor:"))
    if c ==1:
        valores.append(num)
    elif num>valores[-1]:
        valores.append(num)
    else:
        pos=0
        while pos<len(valores):
            if num<=valores[pos]:
                valores.insert(pos,num)
                break
            pos+=1
print(f"Os valores digitados em ordem foram {valores}")