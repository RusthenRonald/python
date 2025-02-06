soma=somaterce=0
matriz=[[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f"Digite um valor para [{l}]:[{c}]"))
for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c]%2==0:
            soma+=matriz[l][c]
        print(f"[{matriz[l][c]:^10}]",end=" ")
    print()
for l in range(0,3):
    somaterce+=matriz[l][2]
print(f"A soma de todos os valores pares é de {soma}")
print(f"A soma dos valores da terceira coluna é de {somaterce}")