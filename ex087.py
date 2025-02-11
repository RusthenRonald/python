jogador={}
gols=[]
jogador["Nome do jogador"]=str(input("Digite o nome do jogador:"))
partidas=int(input(f"Digite a quantidade de partidas que {jogador['Nome do jogador']} jogou:"))
for c in range(0,partidas):
    gols_partidas=int(input(f"Quantos gols na partida {c+1}: "))
    gols.append(gols_partidas)
    jogador["Gols"]=gols
    jogador["Total de gols"]=sum(gols)
print("=-"*15)
