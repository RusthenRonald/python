matriz=[[0,0,0],[0,0,0],[0,0,0]]
soma_pares=maior=soma_coluna=0
pares=[]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f"Digite um valor para [{l},{c}]:"))
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]",end=" ")
        if matriz[l][c]%2==0:#soma dos valores pares
            pares.append(matriz[l][c])
            soma_pares+=matriz[l][c]
    print()
#soma de elementos na terceira coluna
for l in range(0,3):
    soma_coluna+=matriz[l][2]
print(f"A soma dos valores pares é {soma_pares}")
print(f"A soma dos valores da terceira coluna é {soma_coluna}")