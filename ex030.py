sal=float(input("Digite o salário do funcionário:"))
if sal>1250 :
    aumento=sal+(sal*10/100)
    print(f"O funcionário que ganhava {sal}R$ passará a ganhar {aumento}R$")
elif sal<=1250:
    aumento=sal+(sal*15/100)
    print(f"O funcionário que ganhava {sal}R$ passará a ganhar {aumento}R$")
