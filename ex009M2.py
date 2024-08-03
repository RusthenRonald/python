import random
import time
itens=("Pedra", "Papel","Tesoura")
print("""Suas opções :
      [0] Pedra
      [1] Papel
      [2] Tesoura
      """)
computador=random.randint(0,2)
print(f"O computador escolheu {itens[computador]}")



