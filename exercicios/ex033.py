a1=float(input("Digite o primeiro segmento:"))
a2=float(input("Digite o segundo segmento:"))
a3=float(input("Digite o terceiro segmento:"))
if a1<a2+a3 and a2<a1+a3 and a3<a1+a2:
    print("Os segmento acima podem formar triângulos")
else :
    print("Os segmentos acima não podem formar triângulos")