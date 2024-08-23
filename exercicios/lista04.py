a=[2,3,4,7]# a partir do momento que eu igualo uma lista , o pyhton cria uma ligação entre elas
b=a[:]#esse sinal indica cópia , ou seja , b vai receber todos os itens de a
b[2]=8
print(f"Lista A: {a}")
print(f"Lista B: {b}")