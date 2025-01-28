while True:
    num=int(input('Digite um número para saber sua tabuada:'))
    if num<0:
        print("Só aceito números positivos.Programa encerrando...")
        break
    c=0
    while c <=10:
        print(f"{num}x{c}={num*c}")
        c+=1