import random
lista_numeros_escolhidos=[]
while True:
    quantidade_numeros=int(input("Digite a quantidade de números que você deseja marcar:"))
    if quantidade_numeros in [15,16,17,18]:
        break
    else:
        print("Digite apenas números entre 15 e 18")

while len(lista_numeros_escolhidos) <quantidade_numeros:#verificação de números dentro da lista
    numeros_escolhidos=int(input("Digite os números escolhidos:"))
    if numeros_escolhidos <1 or numeros_escolhidos>25:#validação de número de 1 até 25
        print("Digite apenas números entre 1 e 25")
    elif numeros_escolhidos not in lista_numeros_escolhidos:#verificação de números repetidos
        lista_numeros_escolhidos.append(numeros_escolhidos)
    else:
        print("Esse número já está na lista , não vou adcionar!")
print(f"O usuário escolheu esses números:{lista_numeros_escolhidos}")
print("Fim")