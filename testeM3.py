lanche=("Hamburguer","Suco","Pizza","Pudim","Batata frita")
for comida in lanche :#quando não precisa de posição
    print(comida)
for cont in range(len(lanche)):#quando precisa de posição
    print(f"Eu vou comer {lanche[cont]} na posição {cont+1}")
for pos,comida in enumerate(lanche) :#usando duas variaveis no for para achar posição
    print(f"Vou comer {comida} na posição {pos+1}°")