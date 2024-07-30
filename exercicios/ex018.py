import math
ang=float(input("Digite um valor:"))
seno=math.sin(math.radians(ang))
coss=math.cos(math.radians(ang))
tan=math.tan(math.radians(ang))
print(f"O seno de {ang} é {seno:.2f}")
print(f"O cosseno de {ang} é {coss:.2f}")
print(f"A tangente de {ang} é {tan:.2f}")