jogador={}
jogador["Nome"]=str(input("Nome do jogador:"))
jogador["Partidas"]=int(input("Quantidade de partidas:"))
for c in range(0,jogador["Partidas"]):
    jogador["Gols"]=int(input(f"Quantos gols na partida {c+1}:"))