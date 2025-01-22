l1=float(input("Digite o segmento do triãngulo:"))
l2=float(input("Digite o segmento do triãngulo:"))
l3=float(input("Digite o segmento do triãngulo:"))
if l1<(l2+l3) and l2<(l1+l3) and l3<(l1+l2):
    print("Os segmentos PODEM formar um triângulo")
    if l1==l2 and l2==l3:
        print("Equilátero")
    elif l1!=l2 and l1!=l3 :
        print("Escaleno")
    else:
        print("Isósceles")
else:
    print("Os segmentos NÃO PODEM formar um triângulo")