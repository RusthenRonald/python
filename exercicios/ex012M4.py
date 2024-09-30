principal=[]
dados=[]
while True:
    dados.append(str(input("Nome:")))
    dados.append(float(input("Nota 1:")))
    dados.append(float(input("Nota 2:")))
    media=(dados[1]+dados[2])/2
    dados.append(media)
    principal.append(dados[:])
    dados.clear()
    r=str(input("Quer continuar?")).upper().strip()
    if r in ["NAO","N","NÂO"]:
        break
print(principal)
print(f"{"No.":<5}{"NOME":^5}{"MEDIA":>7}")
for pos,a in enumerate(principal):
    print(f"{pos:<5}{a[0]:^5}{a[3]:>7}")
while exibir_notas!=999:
    exibir_notas=int(input("Mostrar as notas de qual aluno? (999 interrompe)"))

