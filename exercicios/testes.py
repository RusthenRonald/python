dados=[]
media=0
while True:
    nome=str(input("Nome:"))
    Nota_1=float(input("Nota 1:"))
    Nota_2=float(input("Nota 2:"))
    media=(Nota_1+Nota_2)/2
    dados.append([nome,[Nota_1,Nota_2],media])
    r=str(input("Quer continuar?")).strip().upper()
    if r in ["NÂO","N","NAO"]:
        break
print(f"{"NO.":^10} {"Nome":^10} {"Média":^10}")
for c,v in enumerate(dados):
    print(f"{c:^10} {v[0]:^10} {v[2]:^10}")
while True:
    notas=int(input("Mostrar notas de qual aluno:"))
    if notas==999:
        break
    if notas<= len(dados)-1:
        print(f"Notas de {dados[notas][0]} são {dados[notas][1]}")
