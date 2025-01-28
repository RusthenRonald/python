tot=soma=0
num=int(input("Digite um número inteiro: (999) para interromper"))
while num != 999:
    tot+=1
    soma+=num
    num=int(input("Digite um número inteiro: (999) para interromper"))
print("FIM")
print(f"Foram digitados {tot} números e a soma entre eles foi de {soma}")