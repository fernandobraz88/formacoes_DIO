#LISTAS:

#Armazenar dados 
#construção
frutas = [] #cria uma lista vazia => mais usada
verduras = ["repolho","alface","couve"] #cria uma lista com elementos indexados / iniciando [0]
compras = list() #outra forma de criar lista vazia
numeros = list(range(5)) #cria uma lista a partir de uma class

#ACESSO DIRETO DE ELEMENTO
#lista[i]
print(verduras[0]) #repolho

#lista[-i] => indice negativo acessa por ordem invertida
print(verduras[-1]) #couve/ [-1] coresponde ao ultimo item da lista

#LISTAS ANINHADAS (Matrizes)
#trata-se de uma lista de listas
#tb retratado como vetor bidimensional
compras.append(frutas)
compras.append(verduras)
print(compras) #compras agora é uma lista contendo a lista de frutas e a lista de verduras

#FATIAMENTO - retorno de partes da lista
print(numeros)
print(numeros[:3]) #do inicio até [3](exclud)
print(numeros[3:]) #do [3] até o final
print(numeros[1:3]) #do [1] ao [3](exclud)
print(numeros[0:4:2])# do [0] ao [4](exclud) a cada 2[steps]
print(numeros[::-1]) #retorna a lista com os elementos invertidos

#ITERANDO - Exibe cada item separadamente
for verdura in verduras:
    print(verdura)

#ENUMERATE - Exibe cada item e seu respectivo indice

for indice, verdura in enumerate(verduras):
    print(f'{indice}: {verdura}')

#COMPREENTION - filtra ou modifica diretamente elementos de uma lista para outra

pares = [numero for numero in numeros if numero %2 == 0]
print(pares)
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)

#METODOS:
#.append() => adiciona um novo item a lista
frutas.append("banana")
frutas.append("maçã")
frutas.append("uva")
print(frutas)

#.clear() => limpa uma lista
numeros.clear()
print(numeros)

#.copy() => cria uma copia da lista para que a original nao seja afetada
verduras2 = verduras.copy()
verduras2.append('acelga')
print(verduras)
print(verduras2)

#.count() => conta quantas vezes um elemento aparece na lista
nome = "Fernando"
print(nome.count('n'))

#.extend() => adiciona a lista elementos de uma outra lista
numeros.extend([1,2,3,4,5])
print(numeros)

#.index() => exibe o indice da primeira ocorrencia do valor passado como argumento
print(frutas.index('maçã'))

#.pop() => exclui o ultimo item da lista
#.pop(i) => exclui o elemento do indice repassado

numeros.pop()
numeros.pop(0)
print(numeros)

#.reverse() => inverte a ordem dos itens da lista
numeros.reverse()
print(numeros)

#.sort() => reorganiza a lista em ordem crescente/alfabetica
#.sort(reverse=True) => reorganiza a lista em ordem decrescente
#.sort(key=lambda x: len(x)) => ordem crescente de tamanho
#.sort(key=lambda x: len(x), reverse=True) => ordem decrescente de tamanho