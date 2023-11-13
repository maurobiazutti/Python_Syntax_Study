#Dicionario não permitem chaves iguais

produto_preco = {"celular": 1500, 
                 "camera": 1000, 
                 "fone": [800, 1500], 
                 "monitor": 2000
                 }
print(produto_preco)# Saída {'celular': 1500, 'camera': 1000, 'fone': [800, 1500], 'monitor': 2000}
print(produto_preco.keys())# Saída dict_keys(['celular', 'camera', 'fone', 'monitor'])
print(produto_preco.values())# Saída dict_values([1500, 1000, [800, 1500], 2000])


# Pegar um item
preco_fone = produto_preco["fone"]
print(preco_fone)# Saída [800, 1500]

# Editar valor
produto_preco["fone"] = 800
preco_fone = produto_preco["fone"]
print(preco_fone)# Saída 800

# Add item
produto_preco["cadeira"] = 1800
cadeira = produto_preco["cadeira"]
print(cadeira)# Saída 1800


# Tamanho
print(len(produto_preco))# Saída 5
quantidade_itens = len(produto_preco)
print(quantidade_itens)# Saída 5

# Deletar item
produto_preco.pop("cadeira")
print(produto_preco)# Saída {'celular': 1500, 'camera': 1000, 'fone': 800, 'monitor': 2000}

#get(chave, valor_padrão): Retorna o valor associado à chave. Se a chave não existir, 
# retorna o valor padrão (ou None se não for fornecido).
meu_dicionario = {"nome": "João", "idade": 25, "cidade": "Exemplo"}
idade = meu_dicionario.get("bairro", "Chave não encontrada")
print(idade) #Saída Chave não encontrada


#update(dicionario): Atualiza o dicionário com elementos de outro dicionário ou pares 
meu_dicionario = {"nome": "João", "idade": 25}
novo_dicionario = {"cidade": "Exemplo", "profissao": "Programador"}
meu_dicionario.update(novo_dicionario)
print(meu_dicionario) # Saída {'nome': 'João', 'idade': 25, 'cidade': 'Exemplo', 'profissao': 'Programador'}

#clear(): Remove todos os elementos do dicionário.
meu_dicionario = {"nome": "João", "idade": 25, "cidade": "Exemplo"}
meu_dicionario.clear()
print(meu_dicionario)  # Saída: {}

# Verificar se tem um item no Dicionario
print("cadeira" in produto_preco) # Saída False
print("celular" in produto_preco) # Saída True
print(2000 in produto_preco.values()) # Saída True

pesquisa = input("Digite o produto")
pesquisa = pesquisa.lower()

if pesquisa in produto_preco:
    preco = produto_preco[pesquisa]
    print(f"O preço do {pesquisa} é {preco}")
else:
    print("Produto não encontrado!")
    
print("##############################")




