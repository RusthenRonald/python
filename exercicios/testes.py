jogador={}
principal=[]
while True:
    jogador["Nome"]=str(input("Nome do jogador:"))
    quant_partidas=int(input(f"Quantas partidas {jogador['Nome']} jogou:"))
    gols=[]
    for c in range(0,quant_partidas):
        quant_gols=int(input(f"Quantos gols na partida {c} :"))
        gols.append(quant_gols)
    jogador["Gols"]=gols
    total=sum(gols)
    jogador["Total"]=total
    principal.append(jogador.copy())
    r=str(input("Quer continuar?")).upper()
    if r in "N":
        break
print("="*15)
print(f"{"Num":^5} {"Gols":^5} {"Total":^10}")
for i,v in enumerate(principal):
    print(f"{i} {v["Nome"]} {v["Gols"]} {v["Total"]}")