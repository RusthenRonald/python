numeros=("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","catorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte")
num=int(input("Digite um número entre 0 e 20:"))
while num <0 or num>20:
    num=int(input("Digite um número entre 1 e 20:"))
print(f"Você digitou o número {numeros[num]}")
print("Fim")