print("10 Termos de uma PA")
prim_termo=int(input("Digite o primeiro termo da pa:"))
razao=int(input("Digite a razão da pa:"))
decimo= prim_termo+(10)*razao
for c in range(prim_termo,decimo,razao):
    print(c,end="-")
print(" FIM")