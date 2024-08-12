tempo=[]
princ=[]
c=0
soma_media=0
while True:
    print("="*15)
    print(f"Cliente {c+1}°")
    tempo.append(str(input("Digite o nome do cliente:")))

    while True:#laço para validação de sexo
        sexo = str(input("Digite o sexo (M/F):")).strip().upper()
        if sexo in ["M", "F","MASCULINO","FEMININO"]:
            tempo.append(sexo)
            break
        else:
            print("Entrada inválida. Por favor, digite 'M' para Masculino ou 'F' para Feminino.")

    tempo.append(str(input("Digite a placa do carro:")))

    km=int(input("Digite a quantidade de km rodados:"))
    dias=int(input("Digite a quantidade de dias contratados:"))

    valor_total=(70*dias)+(0.10*km)#70 vezes dias e 0.10 vezes km

    #adcionando variaveis as listas temporárias
    tempo.append(km)
    tempo.append(dias)
    tempo.append(valor_total)

    #media de km
    c+=1#contador de clientes
    soma_media+=km#soma de todas as médias
    media=soma_media/c

    princ.append(tempo[:])#adciona lista temporaria na principal

    print(f"O cliente {tempo[0]} com a placa {tempo[2]} pagará um valor de {tempo[5]}R$")#exibe nome,placa e valor a ser pago

    tempo.clear()#limpa os dados para ir para próximo cliente

    r=str(input("Você quer sair?")).strip().upper()#saida do usuário
    print("="*15)
    if r in ["SIM","S"]:
        break
print(f"A media de km contratados pelos clientes foram de {media:.1f}km")#exibe media total de km
print(f"Os dados foram {princ}")
print("Fim")
