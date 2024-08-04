import random
while True:
      print("""
      [0] Pedra
      [1] Papel   
      [2] Tesoura """)
      jogador=int(input("Qual a sua jogada ?"))
      computador=random.randint(0,2)
      lista=("Pedra","Papel","Tesoura")
      if computador ==0:#jogou pedra
            if jogador ==0:
                  print("EMPATE")
                  print(f"Ambos colocaram {lista[computador]}")
            elif jogador ==1:
                  print("VITORIA")
                  print(f"O computador botou {lista[computador]} e você {lista[jogador]}!")
            elif jogador ==2:
                  print("DERROTA")
                  print(f"O computador botou {lista[computador]} e você {lista[jogador]}!")
            else:
                  print("Jogada inválida")
                  print("Tente novamente")  
      elif computador ==1:#jogou papel
            if jogador ==1:
                  print("EMPATE")
                  print(f"Ambos colocaram {lista[computador]}")
            elif jogador==2:
                  print("VITORIA")
                  print(f"O computador botou {lista[computador]} e você {lista[jogador]}!")
            elif jogador ==0:
                  print("DERROTA")
                  print(f"O computador botou {lista[computador]} e você {lista[jogador]}!")
            else:
                  print("Jogada inválida")
                  print("Tente novamente")    
      elif computador ==2:#jogou tesoura
            if jogador ==2:
                  print("EMPATE")
                  print(f"Ambos colocaram {lista[computador]}")
            elif jogador ==1:
                  print("DERROTA")
                  print(f"O computador botou {lista[computador]} e você {lista[jogador]}!")
            elif jogador == 0:
                  print("VITORIA")
                  print(f"O computador botou {lista[computador]} e você {lista[jogador]}!")
            else:
                  print("Jogada inválida")
                  print("Tente novamente")    
      r=str(input("Você quer continuar?")).strip().upper()
      if r != "SIM":
            break
print("Fim")