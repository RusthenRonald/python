l1=int(input("Primeiro segmento:"))
l2=int(input("Segundo segmento:"))
l3=int(input("Terceiro segmento:"))
if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print("Os segmentos podem formar um triângulo")
    if l1==l2 and l2==l3:
        print("O triãngulo é Equilatero")
    elif l1!= l2 and l2!=l3 and l3!=l1:
        print("O triângulo é Escaleno")
    else:
        print("O triângulo é isosceles")
else: 
    print("Os segmentos não podem formar um triângulo")