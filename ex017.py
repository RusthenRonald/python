import math
angulo=float(input("Digite o ângulo:"))
cos=math.cos(math.radians(angulo))
seno=math.sin(math.radians(angulo))
tang=math.tan(math.radians(angulo))
print(f" O ângulo {angulo} tem o cosseno igual a {cos:.2f} , seno {seno:.2f} e tangente {tang:.2f}")