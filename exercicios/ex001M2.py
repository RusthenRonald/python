valor=float(input("Qual o valor da casa?"))
salario=float(input("Qual o salário do comprador?"))
anos=int(input("Em quantos anos pretende pagar?"))
pretacao=valor/(anos*12)
porcentagem=salario*30/100
if pretacao > porcentagem:
    print("Seu salário é inferior a 30 do empréstimo")
    print("Empréstimo negado")
else:
    print("Empréstimo concedido")
print(f"Para pagar uma casa de {valor:.2f}R$  em {anos}anos a prestação será de {pretacao:.2f}R$")
