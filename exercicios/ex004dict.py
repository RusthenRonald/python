jogador={}
jogador["Nome"]=str(input("Nome do jogador:"))
partidas=int(input(f"Quantas partidas {jogador['Nome']} jogou "))
c=total=0
part_gol=[]
while c != partidas:
    jogador["Gols"]=int(input(f"Quantos gols na partida {c+1}?"))
    total=total+jogador["Gols"]
    part_gol.append(jogador)
    c+=1
jogador["Total"]=total

print(jogador)

print("=-"*15)
for k , v in jogador.items():
    print(f"O campo {k} tem o valor {v}")

print("=-"*10)
print(f"O jogador {jogador['Nome']} jogou {partidas} partidas")
print(part_gol)

