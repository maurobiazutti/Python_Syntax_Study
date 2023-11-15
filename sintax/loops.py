# Loops in Python

for i in range(5):
    print("Python")
    
precos = [1500, 1000, 800, 5000]
imposto = 1.1

for preco in precos:
    preco_com_imposto = imposto * preco
    print(f"{preco_com_imposto:,.2f}")
    
# regra de imposto
# preço até 1000 -> imposto é de 10%
# preço maior do que 1000 -> imposto é de 15%

total_de_imposto = 0
for preco in precos:
    if preco > 1000:
        imposto = preco * 0.15
    else:
        imposto = preco * 0.10
    total_de_imposto = total_de_imposto + imposto
    print(f"Preço: {preco}, Imposto: {imposto}")
    
print(f"O total de imposte é: {total_de_imposto}")



print("####################################################")
# Quanto variou percentualmente cada mês de 2023 em comparação com 2022
# Simular: se a empresa tivesse empatado em 2022 nos meses que ela vendeu menos,
# qual seria o faturamento?
vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000 }
vendas_23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500 }

faturamento_22 = 0
faturamento_23 = 0
faturamento_simulado = 0

for mes in vendas_23:
    valor_mes22 = vendas_22[mes]
    valor_mes23 = vendas_23[mes]
    percentual_mes = (valor_mes23 / valor_mes22) - 1
    print(f"Percentual: {mes} {percentual_mes:.1%}")
    # print(f"meses 22: {valor_mes22}")
    # print(f"meses 23: {valor_mes23}")
    faturamento_22 = faturamento_22 + valor_mes22
    faturamento_23 = faturamento_23 + valor_mes23
    if valor_mes23 < valor_mes22:
        faturamento_simulado = faturamento_simulado + valor_mes22
    else:
        faturamento_simulado = faturamento_simulado + valor_mes23
        

print(f"Faturamento Simulado = R$ {faturamento_simulado}")    
print(f"Faturamento em 22 = R$ {faturamento_22:,.2f}")
print(f"Faturamento em 23 = R$ {faturamento_23:,.2f}")
    
    
    
    