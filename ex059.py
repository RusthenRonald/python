r=''
media=tot=soma=maior=menor=0
while r not in ["N"]:
    num=float(input("Digite um número:"))
    tot+=1
    soma+=num
    media=soma/tot
    if tot ==1:
        maior=num
        menor=num
    else:
        if num>maior:
            maior=num
        if num<menor:
            menor=num
    r=str(input("Você quer continuar? (S/N):")).strip().upper()
print('FIM')
print(f"A média dos {tot} valores digitados foram de {media}")
print(f"O maior valor digitdo foi {maior} e o menor foi {menor}")
