jogador={}
partidas=[]
jogador["Nome"]=str(input("Nome do jogador:"))
tot=int(input(f"Quantas partidas {jogador['Nome']} jogou ?"))
for c in range(0,tot):
    partidas.append(int(input(f"Quantos gols na partida {c}?")))
jogador["Gols"]=partidas[:]
jogador["Total"]=sum(partidas)#soma elementos em lista ou tupla
print(jogador)
print(partidas)
