valor=float(input("Digite o preço das compras:"))
print('''
a vista dinheiro/cheque[1]
a vista no cartão [2]
em até 2x no cartão [3]
3x ou mais no cartão [4]
''')
opc=int(input("Digite a opção de pagamento:"))
if opc == 1 :
    desconto= valor-(valor*10/100)
    print(f"O valor normal é de {valor}R$ , pagando a vista com 10% de desconto fica {desconto}R$")
elif opc == 2:
    desconto=valor-(valor*5/100)
    print(f"O valor normal é de {valor}R$ , pagando no cartão com 5% de desconto fica {desconto}R$")
elif opc == 3:
    parcelas=valor/2
    print(f"O valor da compra é de {valor}R$ , parcelando em 2x você ira pagar 2 parcelas de {parcelas}R$")
elif opc ==4:
    parc=int(input("Em quantas parcelas você quer pagar:"))
    total=valor+(valor*20/100)
    parcelas=total/parc
    print(f"O valor da compra é {valor}R$ , você irá pagar {parc}x de {parcelas}R% adicionando um juros de 20% o total da compra será de {total}R$")