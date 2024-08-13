prin=[]
soma_media=cont=0
while True:
    num=float(input("Digite um número inteiro:"))
    if num not in prin:
        prin.append(num)
        soma_media+=num
        cont+=1
        media=soma_media/cont
    else:
        print("Número repetido, não vou colocar!")
    r=str(input("Quer continuar?(Sim/Não)")).strip().upper()
    if r in ["NÂO","N","NAO"]:
        break
print(prin)
print(f"A média foi de {media:.2f}")
print(f"O maior número foi {max(prin)} e o menor foi {min(prin)}")