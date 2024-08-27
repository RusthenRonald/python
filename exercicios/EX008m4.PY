matriz=[[0,0,0],[0,0,0],[0,0,0]]
soma=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f"Digite um valor para a posição {l},{c}:"))
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]}]",end=" ")
        if matriz[l][c]%2==0:
            soma+=matriz[l][c]
    print()
print(f"A soma dos pares é de {soma}")