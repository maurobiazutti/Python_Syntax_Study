# Condicional

faturamento = 1000
custo = 1000
lucro = faturamento - custo

if lucro > 0:
    print("Lucro de:", lucro)
else:
    print("Prejuiso de:", lucro)


vendas = 10000

if vendas > 15000:
    bonus = 500
elif vendas > 10000:
    bonus = 150
elif vendas > 9999:
    bonus = 50
else:
    bonus = 0
    
print(bonus)


precos = [1500, 1000, 800, 2000]
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

pesquisa = input("Digite o produto")
pesquisa = pesquisa.lower()

if pesquisa in produtos:
    index_prod = produtos.index(pesquisa)
    valor = precos[index_prod]
    print(f"O preço do {pesquisa} é {valor}")
else:
    print("Produto não encontrado")