while True:
    opcao = input('Você quer criar uma tarefa: [S]im / [N]ão \n').upper()
    tarefa = {}
    lista_tarefas = []
    while opcao == 'S':

        print(
            'O que você deseja?: \n 1: Criar uma tarefa \n 2: Excluir uma tarefa \n 3: Ver suas tarefas \n 4: Encerrar'
        )
        selecionar_opcao = input('Selecione uma opção: \n')
        
        if selecionar_opcao == '1':
            nome_tarefa = input('Digite o nome da tarefa: \n')
            descricao_tarefa = input('Digite a descrição da tarefa: \n')
            tarefa[nome_tarefa] = descricao_tarefa
            lista_tarefas.append(tarefa)
        
        elif selecionar_opcao == '2':
            if len(lista_tarefas) >= 1:
                for tarefas, descricao_tarefas in tarefa.items():
                    print('='*40)
                    print(tarefas, descricao_tarefas)
                opcao_excluir = input('Você realmente deseja excluir uma tarefa? \n [S]im / [N]ão: \n').upper()
                if opcao_excluir == 'S':
                    try:
                        del_tarefa = (input('Qual tarefa você deseja excluir?: \n'))
                        del tarefa[del_tarefa]
                    except KeyError:
                        print('Valor inválido.')
                elif opcao_excluir == 'N':
                    continue
                
            else:
                print("Você não tem tarefas.")
                
        elif selecionar_opcao == '3':
            for tarefas, descricao_tarefas in tarefa.items():
                print(f'{tarefas}: {descricao_tarefas}')
        
        elif selecionar_opcao == '4':
            for tarefas, descricao_tarefas in tarefa.items():
                print('='*40)
                print(f'{tarefas}: {descricao_tarefas}')
                print('='*40)
            print('Até logo')
            break
        
        else:
            print('Valor inválido.')

    if opcao == 'N':
        break
        

    elif opcao != 'S' and 'N':
        print('Valor inválido.')
