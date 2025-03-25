def contador (*num):
    tam=len(num)
    print(f'Recebi os valores {num} e são ao todo {tam}')

contador(2,3)
contador(1,5,2,8)
contador(2)
#Cada vez que você chama a função, os números passados são agrupados em uma tupla.

def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos]*=2
        pos+=1

valores=[2,5,7,1,8]
print(valores)
dobra(valores)
print(valores)

def soma(*valores):
    s=0
    for n in valores:
        s+=n

soma(2,2,3)