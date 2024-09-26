palavras = ("gato", "cachorro", "passaro", "leão", "elefante", "tigre")
for p in palavras:
    print(f"\n Na palavra {p.upper()} temos ",end=" ")
    for l in p :
        if l in "AaEeIiOoUu":
            print(l ,end=" ")