principal = []

while True:
    opcao = str(input("Você quer criar uma tarefa? (S/N) ")).strip().upper()
    if opcao in ["N", "NAO", "NÃO"]:
        break
    
    while True:
        print("""\nMenu de opções
[1] Criar tarefa
[2] Excluir tarefa
[3] Ver tarefas
[4] Encerrar
""")
        
        selecionar_opcoes = int(input("Digite a opção: "))
        
        if selecionar_opcoes == 1:
            nome = str(input("Digite o nome da tarefa: "))
            descricao = str(input("Digite a descrição da tarefa: "))
            principal.append({'nome': nome, 'descricao': descricao})
            print("Tarefa adicionada com sucesso!")
        
        elif selecionar_opcoes == 2:
            if not principal:
                print("Nenhuma tarefa disponível para excluir.")
            else:
                print("Tarefas disponíveis:")
                for i, tarefa in enumerate(principal):
                    print(f"[{i}] {tarefa['nome']} - {tarefa['descricao']}")
                
                opcao_deletada = int(input("Qual tarefa você quer deletar (digite o índice): "))
                if 0 <= opcao_deletada < len(principal):
                    del principal[opcao_deletada]
                    print("Tarefa excluída com sucesso!")
                else:
                    print("Índice inválido.")
        
        elif selecionar_opcoes == 3:
            if not principal:
                print("Nenhuma tarefa criada até o momento.")
            else:
                print("Tarefas criadas:")
                for tarefa in principal:
                    print(f"{tarefa['nome']} - {tarefa['descricao']}")
        
        elif selecionar_opcoes == 4:
            print("Programa encerrado.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

print("Fim")
