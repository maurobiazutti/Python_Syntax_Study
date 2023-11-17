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
       
############################################################################

#A Fórmula para calcular juros compostos é:

 # M = C * (1 + i)^t

# Onde:
# M = montante final
# C = capital
# i = taxa de juros
# t = tempo em meses

# # Captura de Dados
# Capital = float(input("Qual o Valor do Capital?"))
# Taxa_juros_i = float(input("Qual o Valor da Taxa de juros?"))
# tempo = float(input("Quanto tempo em meses?"))

# # Calculo do montant
# montante = Capital * (1 + ((6/100) / 12))**tempo

# #Print do resultado
# print(f'{montante:,.2f}')

#############################################################################

# Quanto cada funcionario vendeu?
# Quantidade de vendas de cada funcionario?
# Valor total de vendas?
# Qual foi o funcionario que mais vendeu?
# Qual foi o funcionario que menos vendeu?

vendas = {
    "Andre": [1000, 500, 300, 5000, 1500, 80, 3000],
    "Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500, 10000],
    "Alan": [800, 100],
    "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180]
}

total_vendas = 0
mais_vendeu = 0
menos_vendeu = 1000000
for venda in vendas:
    print(f"O funcionário {venda.upper()} vendeu  R${sum(vendas[venda])}")
    print(f'O funcionário {venda.upper()} fez um total de {len(vendas[venda])}')
    total_vendas += sum(vendas[venda])
    
    if mais_vendeu < sum(vendas[venda]):
        mais_vendeu = sum(vendas[venda])
        nome_mais_vendeu = venda
        
    if menos_vendeu > sum(vendas[venda]):
        menos_vendeu = sum(vendas[venda])
        nome_menos_vendeu = venda
        
        
    print("---------------------------------------------")
   
print(f'Total de vendas foi R${total_vendas}')  
print(f'O Funcionario que mais vendeu foi {nome_mais_vendeu.upper()} = {mais_vendeu}')
print(f'O Funcionario que menos vendeu foi {nome_menos_vendeu.upper()} = {menos_vendeu}')

# print("reatorio")

