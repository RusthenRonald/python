jogador={}
lista_gols=[]
tot_gols=0
jogador["Nome"]=str(input("Nome do jogador:"))
jogador["Partidas"]=int(input("Quantidade de partidas:"))
for c in range(0,jogador["Partidas"]):
    gols=int(input(f"Quantos gols na partida {c+1}:"))
    lista_gols.append(gols)
    jogador["Gols"]=lista_gols
    tot_gols+=gols
    jogador["Total de gols"]=tot_gols
print("=-"*15)
print(jogador)
print("=-"*15)
for k,v in jogador.items():
    print(f"{k} tem o valor {v}")
print("=-"*15)
print(f"O jogador {jogador['Nome']} jogou {jogador['Partidas']} partidas")
for i, v in enumerate(lista_gols):
    print(f"-Na partida {i+1}, fez {v} gols")