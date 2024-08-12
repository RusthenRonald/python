primeiro=int(input("Digite o primeiro termo:"))
razao=int(input("Digite a razao:"))
cont=1
total=0
mais=10
while mais!=0:
    total+=mais
    while cont <=total:
        print(primeiro,end="-")
        primeiro+=razao
        cont+=1
    print("pausa")
    mais=int(input("Quantos termos você quer mostrar a mais:"))
print("Fim")