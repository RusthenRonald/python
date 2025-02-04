soma=somaterc=0
matriz=[[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f"Digite um valor para [{l}],[{c}]:"))
for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c]%2==0:
            soma+=matriz[l][c]
        print(f"[{matriz[l][c]}]",end=" ")
    print()
for l in range(0,3):
    somaterc+=matriz[l][2]
for c in range(0,3):
    
print(f"A soma de todos os valores pares foram {soma}")
print(f"A soma dos valores da terceira coluna {somaterc}")