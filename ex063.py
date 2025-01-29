c=1
maior_18=homem=menos_20=0
while True:
    print(f"Pessoa {c}°")
    idade=int(input("Digite sua idade:"))
    if idade>18:
        maior_18+=1
    sexo=str(input("Digite seu sexo (M/F):")).strip().upper()
    if sexo in ["MASCULINO","M"]:
        homem+=1
    if sexo in ["FEMININO","F"] and idade<20:
        menos_20+=1
    r=str(input("Você quer continuar? (S/N):")).strip().upper()
    if r in ["NAO","NÂO","N"]:
        break
    print("=-"*5)
    c+=1
print(f"Tem {maior_18} pessoas maiores de 18 anos.")
print(f"Tem {homem} homens cadastrados.")
print(f"Tem {menos_20} mulheres com menos de 20 anos cadastradas.")