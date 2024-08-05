maior=0
menor=0
for c in range(1,5+1):
    peso=float(input(f"Peso da {c}° pessoa"))
    if c ==1:
        maior=peso
        menor=peso
    else:
        if peso > maior:
            maior=peso
        if peso<menor:
            menor=peso
print(f"O maior peso lido foi {maior:.0f}")
print(f"O menor peso foi {menor:.0f}")