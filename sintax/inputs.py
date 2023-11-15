# Pegando dados com Input

#Input tipo str
nome = input("Digite seu primeiro Nome")
sobre_nome = input("Digite seu sobrenome")
print(nome + sobre_nome)


#Input tipo inteiro
idade = int(input("Qual sua idade"))
if idade > 18:
    print("Maior de idade")
else:
    print("mernor de idade")
    

#Input tipo float   
vendas_01 = input("Valor da vendas do dia")
vendas_02 = input("Valor da vendas do dia")
print(f"Valor total das vendas é: {float(vendas_01) + float(vendas_02)}")
