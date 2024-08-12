print("Prova de 5 questões")
print("Deixe sua resposta")
#cadastro de questões 
questoes=[["a"],["a"],["c"],["b"],["c"]]
perguntas=[
    ("Qual é a capital da França?", "a) Paris\nb) Londres\nc) Roma"),
    ("Qual é a capital da Inglaterra?", "a) Madrid\nb) Londres\nc) Berlim"),
    ("Qual é a capital da Itália?", "a) Milão\nb) Veneza\nc) Roma"),
    ("Qual é a capital da Alemanha?", "a) Viena\nb) Berlim\nc) Amsterdã"),
    ("Qual é a capital de Portugal?", "a) Lisboa\nb) Porto\nc) Roma")
]

while True:#este laço é para saida do usuário
    c=0
    total_acertos=0
    total_erro=0

    while c<len(questoes):#enquanto c for menor que todos os itens da lista questoes, ou seja , 5 , o programa continua
        print(f"Questão {c+1}°")
        print(perguntas[c][0])#printei enunciado
        print(perguntas[c][1])#printei enunciado
        usuario=str(input("Digite a alternativa correta:")).strip().lower()
        if usuario == questoes[c][0]:#se usuário for igual a lista de questoes na posicao de c e posicao 0
            print("Você acertou!")
            c+=1
            total_acertos+=1#contador de acerto
        else:
            print("Você errou!")
            print("Tente novamente!")
            total_erro+=1#contador de erro
    saida=str(input("Você quer sair? (Sim/Não)")).upper().strip()
    if saida in ["SIM","S"]:
        break
print(f"Você teve um total de {total_acertos} acertos")
print(f"Você teve um total de {total_erro} erros")
print("Fim")