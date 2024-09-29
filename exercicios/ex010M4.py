matriz=[[0,0,0],[0,0,0],[0,0,0]]
soma_pares=maior=soma_coluna=0
pares=[]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input("Digite um valor:"))
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]",end=" ")
        if matriz[l][c]%2==0:
            pares.append(matriz[l][c])
            soma_pares+=matriz[l][c]
    print()
print(f"A soma dos valores pares é {soma_pares}")