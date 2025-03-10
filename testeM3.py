emprestimo=float(input("Qual o valor do emprestimo:"))
parcelas=int(input("Qual a quantidade de parcelas:"))
emprestimo_juros=emprestimo+(emprestimo*20/100)
quantidade_parcelas=emprestimo_juros/parcelas
print(f"O valor do emprestimo atual é {emprestimo} , com os 20% de juros passara a ter {emprestimo_juros} ")
print(f"A quantidade de parcelas será de {quantidade_parcelas}")