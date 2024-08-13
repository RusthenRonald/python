import datetime 
ano_atual=datetime.date.today().year
contador_maior=0
contador_menor=0
for c in range(1,7+1):
    ano=int(input("Digite seu ano de nascimento:"))
    idade=ano_atual-ano
    if idade>= 18:
        contador_maior+=1
    else:
        contador_menor+=1
print(f"{contador_maior} pessoas já atingiram a maioridade")
print(f"{contador_menor} pessoas ainda não atingiram a maioridade")
print("Fim")