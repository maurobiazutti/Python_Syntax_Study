#Functions in Python

precos = [1500, 1000, 800, 5000, 2000]

def calcula_imposto(preco):
    if preco > 2000:
        imposto = preco * 0.3 
    elif preco > 1000:
        imposto = preco * 0.15
    else:
        imposto = preco * 0.10
    
    print(f"Preço: {preco}, Imposto: {imposto}")
    return imposto

# Variação da mesma função vantagem onde pode ser mudado o valor dos impostos
def calcula_imposto(preco, aliquota01=0.3, aliquota02=0.15, aliquota03=0.1):
    if preco > 2000:
        imposto = preco * aliquota01
    elif preco > 1000:
        imposto = preco * aliquota02
    else:
        imposto = preco * aliquota03
    
    print(f"Preço: {preco}, Imposto: {imposto}")
    return imposto
    


total_de_imposto = 0
for preco in precos:
    imposto = calcula_imposto(preco)
    total_de_imposto = total_de_imposto + imposto
    
print(f"O total de imposte é: {total_de_imposto}")


