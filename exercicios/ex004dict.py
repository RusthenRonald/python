jogador={}
partidas=[]
jogador["Nome"]=str(input("Nome do jogador:"))
tot=int(input(f"Quantas partidas {jogador['Nome']} jogou ?"))
for c in range(0,tot):
    partidas.append(int(input(f"Quantos gols na partida {c}?")))
jogador["Gols"]=partidas[:]
jogador["Total"]=sum(partidas)#soma elementos em lista ou tupla
print(jogador)
print("=-"*15)
for k,v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print("=-"*15)
print(f"O jogador {jogador['Nome']} jogou {len(partidas)} partidas")
for i,v in enumerate(jogador["Gols"]):
    print(f"Na partida {i} fez {v} gols")

