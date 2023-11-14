# Metodos de Array

vendas = [100, 50, 80, 120, 170]
produtos = ["celular", "monitor", "teclado", "memoria", "fone"]


print(vendas) # Saída 100

# Pegar itens do array por posição do indece 
print(vendas[0]) # Saída 100
print(vendas[1]) # Saída 50
print(vendas[-1]) # Saída 170
print(vendas[-2]) # Saída 120
print(produtos[2:]) # Saída ['teclado', 'memoria', 'fone']
print(produtos[:3]) # Saída ['celular', 'monitor', 'teclado']
print("teclado" in produtos) # Saida True

#Editar valor da lista
produtos[3] = "memoria ram"
print(produtos)

#sum(): Soma os itens da lista
total_de_vendas = sum(vendas)
print(total_de_vendas) # Saída 520

#max(): Retorna o maior valor da lista
maior_vendas = max(vendas)
print(maior_vendas) # Saída 170

#min(): Retorna o menor valor da lista
menor_vendas = min(vendas)
print(menor_vendas) # Saída 50

#len(): Conta a quantidade de itens do array
quantidade_prod = len(produtos)
print(quantidade_prod) # Saida 5

#append(x): Adiciona um elemento ao final da lista.
# produtos = ["celular", "monitor", "teclado", "memoria", "fone"]
produtos.append("mouse")
print(produtos) # Saída ['celular', 'monitor', 'teclado', 'memoria', 'fone', 'mouse']

#extend(): Adiciona os elementos de uma lista como outra lista no final.
lista_01 = [1, 2, 3, 4 ]
lista_02 = ["A", "B", "C", "D"]
lista_01.extend(lista_02)
print(lista_01) # Saída [1, 2, 3, 4, 'A', 'B', 'C', 'D']

#insert(i, x): Insere um elemento x na posição 1 da lista.
lista = [1, 2, 3]
lista.insert(1, 4)
print(lista)  # Saída: [1, 4, 2, 3]

#remove(x): Remove o primeiro elemento da lista que é igual a x.
lista = [1, 2, 3, 4, 2]
lista.remove(2)
print(lista)  # Saída: [1, 3, 4, 2]

#pop([i]): Remove e retorna o elemento na posição i. Se i não for especificado, remove e retorna o último elemento.
lista = [1, 2, 3]
elemento_removido = lista.pop(1)
print(lista)           # Saída: [1, 3]
print(elemento_removido)  # Saída: 2

#index(x): Retorna o índice do primeiro elemento na lista que é igual a x.
lista = [1, 2, 3, 2, 4]
indice = lista.index(2)
print(indice)  # Saída: 1

#count(x): Retorna o número de ocorrências do elemento x na lista.
lista = [1, 2, 3, 2, 4, 2]
posicao = lista.count(2)
print(posicao)  # Saída: 3

#sort(): Ordena os elementos da lista.
lista = [3, 1, 4, 1, 5, 9, 2]

lista.sort()
print(lista)  # Saída: [1, 1, 2, 3, 4, 5, 9]

lista.sort(reverse=True) 
print(lista)  # Saída: [9, 5, 4, 3, 2, 1, 1]

#reverse(): Inverte a ordem dos elementos na lista.
lista = [1, 2, 3, 4]
lista.reverse()
print(lista)  # Saída: [4, 3, 2, 1]
