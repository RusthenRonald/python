tot=soma=0
while True:
    num=int(input("Digite um número:"))
    if num ==999:
        break
    tot+=1
    soma+=num
print("FIM")
print(f"Você digitou {tot} números e a soma entre eles foi de {soma}")
