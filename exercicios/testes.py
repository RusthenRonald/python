jogador={}
jogador["Nome"]=str(input("Nome do jogador:"))
partidas=int(input(f"Quantas partidas {jogador['Nome']} jogou "))
c=total=0
gols=[]
while c != partidas:
    jogador["Gols"]=int(input(f"Quantos gols na partida {c+1}?"))
    total=total+jogador["Gols"]
    gols.append(jogador["Gols"])
    c+=1
jogador["Total"]=total
print("=-"*15)
print(jogador)
print("=-"*15)

del(jogador["Gols"])

for k,v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print(f"O campo gols tem o valor {gols}")
print("=-"*15)

print(f"O jogador {jogador['Nome']} jogou {partidas} partidas.")
for c , v in enumerate(gols):
    print(f"Na partida {c}, fez {v} gols")




