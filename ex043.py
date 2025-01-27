soma=tot=0
for c in range(1,501):
    if c%2==1 and c%3==0:
        tot+=1
        soma+=c
        print(c,end=" ")
print(f"\nTem um total de {tot} números impares multiplos de 3 e a soma de todos eles é de {soma}")