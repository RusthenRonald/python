jogador={}
gols=[]
principal=[]
while True:
    gols=[]
    jogador["Nome do jogador"]=str(input("Digite o nome do jogador:"))
    partidas=int(input(f"Digite a quantidade de partidas que {jogador['Nome do jogador']} jogou:"))
    for c in range(0,partidas):
        gols_partidas=int(input(f"Quantos gols na partida {c+1}: "))
        gols.append(gols_partidas)
        jogador["Gols"]=gols
        jogador["Total de gols"]=sum(gols)
    principal.append(jogador.copy())
    jogador.clear()
    r=str(input("Digite se quer continuar (S/N):"))
    if r in "Nn":
        break
print("=-"*15)
for p in principal:
    print(p)