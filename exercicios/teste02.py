import random
lista_numeros_escolhidos=[]
while True:
    quantidade_numeros=int(input("Digite a quantidade de números que você deseja marcar:"))
    if quantidade_numeros >=15 and quantidade_numeros<=18:
        break
    else:
        print("Digite apenas números entre 15 e 18!")
    for c in range(0,quantidade_numeros):
        numeros_escolhidos=int(input("Digite o número escolhido:"))
        if numeros_escolhidos in lista_numeros_escolhidos:
            print("Esse número já está na lista!")
        else:
            lista_numeros_escolhidos.append(numeros_escolhidos)