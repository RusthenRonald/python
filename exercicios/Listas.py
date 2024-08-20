lanche=["hamburguer","Suco","Pizza","Pudim"]#listas são mutáveis
lanche[3]="Picolé"
lanche.append("Sorvete")#adciona itens na lista
lanche.insert(0,"Batata-Frita")#adiona em posição especifica
del lanche[1]#remove lista ou item especifico 
lanche.pop#remove ultimo elemento ou indice
lanche.remove("Suco") #remove o valor/conteudo e não o indice
print(lanche)
valores=[1,7,3,7,2,8,1,9,10]
valores.sort(reverse=True)#sort organiza de forma crescente e com reverse true decrescente
print(valores)