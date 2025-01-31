palavras=("Aprender","Programar","Linguagem","Pyhton","Curso",
          "Gratis","Estudar","Praticar","Trabalhar","Mercado",
          "Programador","Futuro")
for p in palavras:
    print(f"\nNa palavra {p.upper()} temos",end=" ")
    for l in p:
        if l in "AaEeIiOoUu":
            print(f"{l}",end=" ")
