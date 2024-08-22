valores=[]
valores_pares=[]
valores_impares=[]
while True:
    num=int(input("Digite um número:"))
    r=str(input("Quer continuar?")).strip()
    if r in "Nn":
        break
    valores.append(num)
    if num%2==0:
        valores_pares.append(num)
    elif num%2==1:
        valores_impares.append(num)
print(f"Os valores são {valores}")
print(f"Os valores impares são {valores_impares}")
print(f"Os valores pares são {valores_pares}")
