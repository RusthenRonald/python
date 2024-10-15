matriz=[[0,0,0],[0,0,0],[0,0,0]]
pares=soma_coluna=maior=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f"Digite um número para linha [{l} {c}]:"))
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^10}]",end=" ")
        if matriz[l][c]%2==0:
            pares+=matriz[l][c]
    print()
for l in range(0,3):
    soma_coluna+=matriz[l][2]
for c in range(0,3):
    if c ==0:
        maior=matriz[1][c]
    else:
        if matriz[1][c]>maior:
            maior=matriz[1][c]
print(f"A soma de todos os valores pares é de {pares}")
print(f"O maior valor da 2° linha é {maior}")
print(f"A soma de todos os valores da coluna 3° é {soma_coluna}")