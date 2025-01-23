print("Calculando IMC")
peso=float(input("Digite o seu peso:"))
alt=float(input("Digite sua altura:"))
imc=peso/(alt**2)
if imc<18.5:
    print(f"Seu imc é de {imc:.2f} \n Categoria: Abaixo do peso")
elif imc>=18.5 and imc <25:
     print(f"Seu imc é de {imc:.2f} \n Categoria: Peso ideal")
elif imc>=25 and imc <30:
      print(f"Seu imc é de {imc:.2f} \n Categoria: Sobre peso")
elif imc>=30 and imc<40:
      print(f"Seu imc é de {imc:.2f} \n Categoria: Obesidade")
else:
      print(f"Seu imc é de {imc:.2f} \n Categoria: Obesidade mórbida")