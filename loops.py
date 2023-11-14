# Loops in Python

# for i in range(5):
#     print("Python")
    
precos = [1500, 1000, 800, 5000]
imposto = 1.1

for preco in precos:
    preco_com_imposto = imposto * preco
    print(f"{preco_com_imposto:,.2f}")
    
