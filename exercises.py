# Cada vendedor ganha R$2 e 1% do valor da venda
# Calcular o valor total de bonus pago e o bonus de cada vendedor

vendas = {
    "Andre": [1000, 500, 300, 5000, 1500, 80, 3000],
    "Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
    "Alan": [800, 100],
    "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180]
}

 # Para resolver preciso saber
 # numero de vendas de cada vendedor * 2
 # valor das vendas * 1.01
 
# num_vendas_vendedor = 0
for vendedor in vendas:
    nun_ven = vendas[vendedor] 
    numv = len(nun_ven) 
    print(numv)
    print(nun_ven)
    
    # print(vendedor, vendas[vendedor])
    
# print(vendas[0])

# num = vendas["Andre"]
# print(len(num))