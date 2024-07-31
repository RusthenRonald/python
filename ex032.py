sal=float(input("Qual o salário do funcionário?"))
if sal >1250 :
    aumento=sal+(sal*10/100)
    print(f"Seu salário é superior a 1250R$ e passará a ter um aumento de 10%  {aumento}R$")
elif sal <=1250:
    aumento=sal+(sal*15/100)
    print(f"Seu salário é inferior a 1250R$ e passará a ter um aumento de 15%  {aumento}R$")