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

print(jogador)

print("=-"*15)
print(f"O campo gols tem o valor {gols} ")

