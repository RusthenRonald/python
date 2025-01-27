
termo=int(input("Digite o termo da pa:"))
razao=int(input("Digite a razão da pa:"))
mais_termos=10
while mais_termos != 0:
    c=1
    while c <=mais_termos:
        print(termo,end=" ")
        termo+=razao
        c+=1
    mais_termos=int(input("\nQuantos termos você quer mostrar a mais:"))
print("FIM")

