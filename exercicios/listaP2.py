teste=[]
teste.append("Gustavo")
teste.append(40)
galera=[]
galera.append(teste[:])#a partir do momento que eu adionei a lista no append eu criei uma ligação
teste[0]="Maria"
teste[1]=22
galera.append(teste)
print(galera)