n1=int(input("Digite um número:"))
n2=int(input("Digite outro número:"))
while True:
    print("""
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    """) 
    opcao=int(input("Escolha a opção:"))
    if opcao == 1:
        soma=n1+n2
        print(f"A soma de {n1} e {n2} é {soma}")
    elif opcao ==2 :
        mult=n1*n2
        print(f"A multiplicação de {n1} e {n2} é {mult}")
    elif opcao ==3:
        if n1>n2:
            print(f"O maior número é {n1}")
        elif n1==n2:
            print("Ambos tem o msm valor")
        else:
            print(f"O maior número é {n2}")
    elif opcao ==4:
        n1=int(input("Digite um número:"))
        n2=int(input("Digite outro número:"))
    elif opcao==5:
        print("Fim do programa")
        break
    else:
        print("Dados inválidos")
        print("Digite apenas números entre 1 e 5")
