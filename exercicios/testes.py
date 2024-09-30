soma_pares=soma_coluna=0
matriz=[[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f"Digite um número para[{l},{c}]:"))
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]",end=" ")
        if matriz[l][c]%2==0:
            soma_pares+=matriz[l][c]
    print()
for l in range(0,3):
    soma_coluna+=matriz[l][1]
print(f"Foram digitados {soma_pares} números pares ")
print(f"A soma dos números da 1 coluna foi de {soma_coluna} ")