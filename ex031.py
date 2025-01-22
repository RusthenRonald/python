l1=float(input("Digite o comprimento da reta:"))
l2=float(input("Digite o comprimento da reta:"))
l3=float(input("Digite o comprimento da reta:"))
if l1<(l2+l3) and l2<(l1+l3) and l3<(l2+l1):
    print("Os segmentos PODEM formar um triângulo")
else:
    print("Os segmentos NÃO PODEM formar um triângulo")