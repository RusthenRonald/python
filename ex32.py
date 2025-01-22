valor_casa=float(input("Digite o valor da casa:"))
salario=float(input("Digite seu salário:"))
anos=int(input("Informe em quantos anos você irá pagar:"))
prestacao=valor_casa/(anos*12)
if prestacao>(salario*30/100):
    print(f"Para pagar uma casa de {valor_casa}R$ em {anos} anos a prestação será de R${prestacao:.2f}")
    print("Empréstimo NEGADO!")
else:
    print(f"Para pagar uma casa de {valor_casa}R$ em {anos} anos a prestação será de {prestacao:.2f}R$")
    print("Empréstimo Concedido")