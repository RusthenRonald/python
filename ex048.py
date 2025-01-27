import datetime
tot_maior=tot_menor=0
ano_atual=datetime.datetime.today().year
for c in range(1,8):
    nasc=int(input("Digite seu ano de nascimento:"))
    idade=ano_atual-nasc
    if idade>18:
        tot_maior+=1
    else:
        tot_menor+=1
print(f"{tot_menor} pessoas ainda não atigiram a maioridade")
print(f"{tot_maior} pessoas já atigiram a maioridade")