opc=maior=menor=0
n1=int(input("Digite um número:"))
n2=int(input("Digite um número:"))
while opc !=5:
    print("""
    [1] somar
    [2] multiplicar
    [3] maior 
    [4] novos números
    [5] sair do programa""")
    opc=int(input("Selecione a opção:"))
    if opc ==1:
        soma=n1+n2
        print(f"A soma de {n1} e {n2} foi de {soma}")
    elif opc ==2:
        mult=n1*n2
        print(f"A multiplicação de {n1} e {n2} foi de {mult}")
    elif opc ==3:
        if n1>n2:
            maior=n1
            print(f"O maior número entre {n1} e {n2} é {maior}")
        elif n1==n2:
            print("Os valores são iguais")
        else:
            menor=n2
            print(f"O menor número entre {n1} e {n2} é {menor}")
    elif opc ==4:
        n1=int(input("Digite um novo número:"))
        n2=int(input("Digite um novo número:"))
print("Fim")