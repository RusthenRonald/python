jogador={}
gols=[]
jogador["Nome"]=str(input("Nome do jogador:"))
quant_partidas=int(input(f"Quantas partidas {jogador['Nome']} jogou:"))
for c in range(0,quant_partidas):
    quant_gols=int(input(f"Quantos gols na partida {c}° :"))
    gols.append(quant_gols)
jogador["Gols"]=gols
jogador["Total"]=sum(gols)
print(jogador)
print("=-"*15)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print("=-"*15)
print(f"O jogador {jogador['Nome']} jogou {quant_partidas}")
for c, v in enumerate(gols):
    print(f"Na partida {c}, fez {v} ")
