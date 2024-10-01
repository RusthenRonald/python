estado={}
brasil=[]
for c in range(0,3):
    estado["Uf"]=str(input("Unidade federativa:"))
    estado["Sigla"]=str(input("Sigla:"))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(f"{v}")