while True:
    n=int(input("Digite um número para saber sua tabuada:"))
    if n <0:
        break
    for c in range(1,10+1):
        print(f"{n}x{c}={n*c}")
print("Fim")