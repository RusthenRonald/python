preco=float(input("Digite o valor da compra R$:"))
print("""
[1] á vista dinheiro/cheque
[2] á vista cartão 
[3] 2x no cartão 
[4] 3x ou mais no cartão
""")
opcao=int(input("Digite a opção:"))
if opcao==1:
    desconto=preco-(preco*10/100)
    print(f"O preço da compra era {preco} , com 10% de desconto passou a ficar {desconto:.0f}R$")
elif opcao==2:
    desconto=preco-(preco*5/100)
    print(f"O preço da compra era {preco} , com 5% de desconto passou a ficar {desconto:.0f}R$")
elif opcao==3:
    print(f"O valor a ser pago será em 2x de {preco/2:.0f}R$")
    print(f"Sua compra ao final custará {preco}")
else:
    juros=preco+(preco*20/100)
    totparc=int(input("Em quantas parcelas?"))
    parcela=preco/totparc
    print(f"Você irá pagar {totparc}x de {parcela:.1f}")
    print(f"Ao final da compra você irá pagar um total de {juros}R$")
