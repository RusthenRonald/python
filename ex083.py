import random
jogo={}
for c in range(1,5):
    jogo[f"Jogador{c}"]=random.randint(1,6)
print(jogo)