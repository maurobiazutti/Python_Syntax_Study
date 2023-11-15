# Cada vendedor ganha R$2 e 1% do valor da venda
# Calcular o valor total de bonus pago e o bonus de cada vendedor
vendas = {
    "Andre": [1000, 500, 300, 5000, 1500, 80, 3000],
    "Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
    "Alan": [800, 100],
    "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180]
}
 # Para resolver preciso saber:
 # numero de vendas de cada vendedor * 2
 # valor das vendas * 1.01
 
def calcula_bonus(lista):
    qtde = len(lista) #tamanho da lista
    bonus1 = qtde * 2 
    valor_total_vendas = sum(lista) #soma itens da lista
    bonus2 = valor_total_vendas * 0.01
    bonus = bonus1 + bonus2
    return bonus


total_bonus_pago = 0
for vendedor in vendas:
    lista_vendas = vendas[vendedor] 
    bonus = calcula_bonus(lista_vendas)
    total_bonus_pago = total_bonus_pago + bonus
    print(f"Vendedor: {vendedor}, Bonus de R${bonus}")
    
print(f"O Total de bonus pago foi de R${total_bonus_pago:,.2f}")
       
